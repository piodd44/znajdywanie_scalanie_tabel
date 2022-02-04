import numpy as np
import pandas as pd
from line_classifier import LineClassifier
from column_classifier import ColumnClassifier
from string_standard import make_standard_string
from table import Table

column_classifier = ColumnClassifier()
number_list = [str(x) for x in range(10)]


def open_xlms(path):
    xl = pd.ExcelFile(path)
    res = len(xl.sheet_names)
    data_frame = pd.read_excel(path)
    return data_frame


def give_table_list_from_xlms(path, start_sheet=0):
    xl = pd.ExcelFile(path)
    counter = 0
    error_list = []
    line_classifier = LineClassifier()
    table_df_list = []
    for name_of_sheet in xl.sheet_names:
        counter += 1
        # to dla testwów żeby nie czekać zbyt długo na wynik
        if counter > 30:
            break
        # tu wcześniej można bywykryć od kiedy zacząć , na razie na sztywno
        if counter > start_sheet:
            print("cunter==", counter, name_of_sheet)
            "tu jest coś bardzo nie optymalnego w wczytywaniu bo"
            "to zajmuje najwiecej czasu i to dużo wiecej niż całą reszta"
            "to wczytania wszystkich pakietów potrzeba nawet 2-3 min "
            "a reszta dzieje się w ciągu 1s "
            data_frame = pd.read_excel(path, sheet_name=name_of_sheet, header=None)
            data_frame = data_frame.dropna(how="all", axis=1)
            "dlatego że czasem odwołuje się do ujemnch ideków wzgledem jakiś zanelzionych"
            "i żeby uniknoć ciągłego sprawdzania czy dany indeks istnieje "
            "po prostu dodając 3 linijki sprawiam że na pewno istnieje"
            empty_row = pd.DataFrame(columns=data_frame.columns, index=[0, 1, 2])
            data_frame = pd.concat([empty_row, data_frame], ignore_index=True)
            start_end_index = find_start_end_table_index(data_frame=data_frame, line_classifier=line_classifier)
            if len(start_end_index) != 0:
                all_good_row = []
                for start, end in start_end_index:
                    good_row_list = []
                    "zapisujemy wiersze które mogą być pomocne przy ustalaniu nazw kolumn"
                    help_headers = help_headers_df(start=start, data_frame=data_frame)
                    "przygotowujemy index kolumn z danymi"
                    [good_row_list.append(x) for x in range(start, end + 1)]
                    [all_good_row.append(x) for x in range(start, end + 1)]
                    cur_table_df = data_frame[data_frame.index.isin(good_row_list)]
                    table = Table(data_df=cur_table_df, help_df=help_headers, pack=name_of_sheet)
                    table_df_list.append(table)

                last_row_i = -1
                "lekkie sprawdzenie czy przypadkiem tabelki się nie nakładają"
                "gdyż to oznacza że coś złego stało się podczas szukania"
                "konców i poczatków tabelki"
                "docelowo jakiś wyjątek"
                for x in all_good_row:
                    if x <= last_row_i:
                        print("==================bład ====================")
                        print(x, last_row_i)
                    else:
                        error_list.append((name_of_sheet, x))
                    last_row_i = x
    if len(table_df_list) == 0:
        exit("nie wykryto żadnej tabeli")
    print("skończyłem give_table_list_from_xlms")
    return table_df_list


def help_headers_df(start, data_frame):
    if start - 3 >= 1:
        return data_frame[start - 3:start]
    elif start - 2 >= 1:
        return data_frame[start - 2:start]
    elif start - 1 >= 1:
        return data_frame[start - 1:start]
    else:
        return data_frame[start:start]


def choose_name_from_lines(data_frame):
    nan_list_counter = []
    row_list = []
    for index_r, row in data_frame.iterrows():
        nan_cunter = 0
        row_list.append(row.values)
        for x in row.values:
            standard = make_standard_string(x)
            if standard == "nan":
                nan_cunter += 1
        nan_list_counter.append(nan_cunter)
    "to na pewno do zmian"
    bigest = np.argmax(nan_list_counter)
    name = ""
    for x in row_list[bigest]:
        standard = make_standard_string(x)
        if standard != "nan":
            return standard
    return name


"plan taki ze wybieramy possible start ten dalszy o jeden jeśli jest"


def find_start_end_table_index(data_frame, line_classifier):
    row_class_list = make_class_row(data_frame=data_frame, line_classifier=line_classifier)
    for x in row_class_list:
        # print(x)
        pass
    initial_index = 0
    start_end_list = []
    while True:
        start_index = find_next_start(start_index=initial_index, row_list_class=row_class_list)
        initial_index = start_index
        if initial_index == -1:
            return start_end_list
        end_index = find_end(start_index=initial_index, row_list_class=row_class_list)
        if start_index == -1 and end_index == -1:
            return start_end_list
        else:
            start_end_list.append((start_index, end_index))


def find_next_start(start_index, row_list_class):
    cur_index = start_index
    row_index, row_class, row_value = row_list_class[cur_index]
    last_class = row_class
    while True:
        row_index, row_class, row_value = row_list_class[cur_index]
        if row_class == "empty":
            pass
        elif row_class == "non-recognize":
            if last_class == "start_1":
                return cur_index
            # print(row_value)
            pass
        cur_index += 1
        last_class = row_class
        if cur_index > len(row_list_class) - 1:
            return -1
    pass


def find_end(start_index, row_list_class):
    cur_index = start_index
    row_index, row_class, row_value = row_list_class[cur_index]
    numeric_column_index = 0
    for i, x in enumerate(row_value):
        if type(x) is int:
            numeric_column_index = i
            break
    # print(numeric_column_index, row_value)
    while True:
        cur_index += 1
        row_index, row_class, row_value = row_list_class[cur_index]
        if type(row_value[numeric_column_index]) is not int:
            return cur_index - 1


def make_class_row(data_frame, line_classifier):
    possible_start_0 = []
    possible_start_1 = []
    possible_start_2 = []
    possible_start_list = []
    row_class_list = []
    for index_r, row in data_frame.iterrows():
        # print("========== wiersz  start =========")
        row_list = list(row)
        # print(index_r, row_list)
        possible_class = line_classifier.get_row_class(row_list)
        # print("row list==",row_list)
        if possible_class == "start_2":
            possible_start_2.append((index_r, row_list))
            possible_start_list.append((index_r, 2))
        if possible_class == "start_1":
            possible_start_list.append((index_r, 1))
            possible_start_1.append((index_r, row_list))
        if possible_class == "start_0":
            possible_start_list.append((index_r, 0))
            possible_start_0.append((index_r, row_list))
        row_class_list.append((index_r, possible_class, row_list))
    return row_class_list


def show_row_(data_frame):
    for index_r, row in data_frame.iterrows():
        # print("========== wiersz  start =========")
        print(index_r, row.values)


"konców bedziemy szukać idąc od spodziewanych początków do np nan albo czegoś co już nie jest liczbą (jesli sa numerowane ) "


def close_index_choose(pack):
    # print(pack)
    return pack[-1][0] + pack[-1][1]


def make_good_columns(data_frame):
    data_frame = column_classifier.most_probably_names(data_frame)
    if "empty" in data_frame.columns:
        data_frame = data_frame.drop(['empty'], axis=1)
    return data_frame


"tu już mamy dobrze jedną data_frame z danymi"
"docelowo bedziemy zwracać liste taki data_frame "
"jeżeli zostaną wykryte rózne tabelki"
"obecnie przy róznych tabelkach program się wyłacza"


def give_data_frame_list(table_list):
    for table in table_list:
        name = choose_name_from_lines(table.help_df)
        table.name = name
        headers = column_classifier.headers_from_upper_row(help_headers_list=table.help_df)
        table.headers = headers
    grouped_table = group_table_by_headers(table_list)
    data_df_list = []
    for i, table_list in enumerate(grouped_table):
        for table in table_list:
            data_df = table.data_df
            try:
                data_df.columns = table.headers
            except:
                print(i, table.headers)
            data_df_list.append(data_df)
    for i, table_group in enumerate(grouped_table):
        print("=================")
        print("nagłówek grupy ", i)
        print(table_group[0].headers)
        print("=================")
    print(len(data_df_list))
    return data_df_list


"dostaje tabelki w trakcie działania funkcji give_data_frame_list, tabelki mają nadane nagłówki "
"funkcja ma zwrócić liste pogrupowanych tabelek"
"czyli liste list "
"[[tabelki grupy 1],[tabelki grupy 2],[tabelki grupy 3]]"

"zakładamy przechodność relacji podobieństwa nagłówków"
"czyli jeśli a~b i b~c to a~c co tak naprawde może nie być prawdą gdyż "
"kkkkk~kkkka, kkkka~kkkaa ale kkkkk~/~kkkaa"
"dzieki temu możemy też założyc że każdy nagłowek należy tylko do jednej grupy"


def group_table_by_headers(table_list):
    group_list = [[table_list[0]]]

    for table in table_list:
        new_group = True
        h1 = table.headers
        for group in group_list:
            h2 = group[0].headers
            if column_classifier.the_same_headers(header_1=h1, header_2=h2):
                group.append(table)
                new_group = False
        if new_group:
            group_list.append([table])
    print(group_list)
    print(len(group_list))
    # exit("tu się kończy ")
    return group_list


"teraz funcka ni zwraca tego co powinna w sumie ale już zapisuje odzielnie rodzaje tabelek"
"na końcu najelepiej żeby próbowała je scalic"


def final_fun(path, save_path, start=0):
    table_list = give_table_list_from_xlms(path=path, start_sheet=start)
    df_good_list = give_data_frame_list(table_list)
    for i, df_good in enumerate(df_good_list):
        df_good_name = make_good_columns(data_frame=df_good)
        if save_path[-3:] == "csv":
            df_good_name.to_csv("_" + str(i) + "_" + save_path)
        else:
            save_path = save_path + ".csv"
            df_good_name.to_csv("_" + str(i) + "_" + save_path)
    return df_good_name

# test_1()
# column_classifier = ColumnClassifier(open_xlms("output.xlsx"))
# test_3()
# test_4()
# test_zad_1()
# test_zad_2()
# test_zad_3()
# test_zad_4()
# test_zad_5()
