import numpy as np
import pandas as pd

import string_standard
from string_standard import make_standard_string, string_similarity
from my_dictionary import MyDictionary

expected_name_1 = ['oznaczenie zadania', 'tytuł zadania', 'lp', 'opis', 'inn', 'postać', 'opakowanie', 'dawka', 'moc',
                   'ilość',
                   'jednostki', 'inne']

"można spróbować zrobić słownik dla kolumn i " \
"potem zliczać słowa pasujące do kolumny" \
" i w ten sposób decydowac która to jest kolumna"
"słownik zrobić z pewnych danych"

numerical = [str(x) for x in range(10)]

class ColumnClassifier:
    def __init__(self):
        self.dictionary = MyDictionary()

    def is_lp(self, word):
        word = make_standard_string(word)
        word = word.replace(".", "").replace(",", "")
        if word == "":
            return False
        for x in word:
            if x in numerical:
                pass
            else:
                return False
        return True

    def is_ilosc(self, word):
        word = make_standard_string(word)
        word = word.replace(".", "").replace(",", "")
        if word == "":
            return False
        for x in word:
            if x in numerical:
                pass
            else:
                return False
        return True

    def is_opakowanie(self, row):
        if row == "":
            return False
        row = make_standard_string(row)
        splited_row = row.split()
        for word in splited_row:
            standard_word = make_standard_string(word)
            if standard_word in self.dictionary.opakowanie_set:
                pass
            else:
                return False
        return True

    def word_in_row(self, row):
        splited_row = row.split()
        return len(splited_row)

    def avg_word_in_columns(self, data_frame):
        all_counter_list = []
        for column in data_frame:
            list_row_in_col = data_frame[column]
            len_of_all_row = 0
            non_empty_row = 0
            for row in list_row_in_col:
                standard = make_standard_string(row)
                words_in_row = standard.split()
                if standard != "nan":
                    non_empty_row += 1
                for word in words_in_row:
                    standard_word = make_standard_string(word)
                    if standard_word != "nan":
                        len_of_all_row += 1
            if non_empty_row == 0:
                all_counter_list.append(0)
            else:
                avg_len = len_of_all_row / non_empty_row
                all_counter_list.append(avg_len)
        return all_counter_list

    def count_word_class_in_columns(self, data_frame):
        all_counter_list = []
        for column in data_frame:
            list_row_in_col = data_frame[column]
            counter_is_lp = 0
            counter_is_ilosc = 0
            counter_is_opakowanie = 0
            value_for_lp = 0
            value_for_ilosc = 0
            for row in list_row_in_col:
                standard = make_standard_string(row)
                words_in_row = standard.split()
                for word in words_in_row:
                    standard_word = make_standard_string(word)
                    try:
                        if self.is_lp(standard_word):
                            counter_is_lp += 1
                            value_for_lp += float(standard_word.replace(",", "."))
                        if self.is_ilosc(standard_word):
                            counter_is_ilosc += 1
                            value_for_ilosc += float(standard_word.replace(",", "."))
                    except:
                        print(standard_word)
                    if standard_word != "nan":
                        if self.is_opakowanie(standard_word):
                            counter_is_opakowanie += 1
            all_counter_list.append(
                (column, ("lp", counter_is_lp, value_for_lp), ("ilość", counter_is_ilosc, value_for_ilosc),
                 ("opakowanie", counter_is_opakowanie)))
        return all_counter_list

    def non_nan_in_row(self, row):
        for word_row in row:
            word_standard = make_standard_string(word_row)
            if word_standard == "nan":
                return False
        return True

    def non_numerical(self, row):
        for word_row in row:
            if type(word_row) is int or type(word_row) is float:
                return False
            word_standard = make_standard_string(word_row)
            if word_standard in numerical:
                return False
        return True

    def try_find_in_dict(self, word):
        standard_word = make_standard_string(word)
        if standard_word == "":
            return False, ""
        standard_word = standard_word.split()[0]
        standard_word = make_standard_string(standard_word)
        if standard_word in self.dictionary.lp_set:
            return True, "lp"
        if standard_word in self.dictionary.opakowanie_set:
            return True, "opakowanie"
        if standard_word in self.dictionary.get_ilosc_set():
            return True, "ilość"
        if standard_word in self.dictionary.get_nazwa_set():
            return True, "nazwa"
        if standard_word in self.dictionary.get_opis_set():
            return True, "opis"
        print("standard_word=====", standard_word)
        return False, "non_in_dictionary"

    def most_probably_names(self, data_frame):
        tuple_name_bool_list = []
        name_list = []
        avg_words_list = self.avg_word_in_columns(data_frame)
        headers = data_frame.columns
        for i, headers in enumerate(headers):
            # print(headers)
            if avg_words_list[i] != 0:
                tuple_name_bool_list.append(self.try_find_in_dict(headers))
            else:
                "nawet jeśli koumna ma opis w porzatku to jeśli jest całkowicie pusta to i tak nie trzeba jej pamietac (tak mi się przynajmniej na razie wydaje ) "
                tuple_name_bool_list.append((True, "empty"))
        all_have_name = True
        for name in tuple_name_bool_list:
            name_list.append(name[1])
            if name[0]:
                pass
            else:
                all_have_name = False
        if all_have_name:
            try:
                if self.not_conflicting_names(name):
                    pass
                else:
                    print("sprzeczne nazwy")
            except:
                # print(headers_from_help)
                exit()
        before_change = data_frame.columns
        after_change = list(before_change.copy())
        for i, name in enumerate(name_list):
            after_change[i] = name
        data_frame.columns = after_change
        print("zwacam jedne nazwy")
        return data_frame

    def headers_from_upper_row(self, help_headers_list):
        headers_from_help = self.find_most_probably_table_headers(help_headers_list)
        return headers_from_help

    "na razie pusta implementacja dla samej idei"
    "po prostu sprawdzamy czy nadane nazwy nie są sprzeczne"
    "czyli czy np nie ma dwóch tak samo nazwanych kolumn"
    "jezeli są sprzeczne to wtedy próbujemy rostrzygnoć"
    "w inny sposób "
    "a nawet dla nie sprzecznych warto dołożyc metoda która sprawdzi czy tez daje nawzy takie same  "

    def not_conflicting_names(self, tuple_name_bool_list):
        return True

    def to_do_wyzej_ale_na_razi_nie(self, data_frame):
        avg_words_list = self.avg_word_in_columns(data_frame)
        counter_class = self.count_word_class_in_columns(data_frame)
        opis_probably_index = np.argmax(avg_words_list)
        name_list = []
        non_empty_columns = []
        for i, x in enumerate(avg_words_list):
            if x == 0:
                name_list.append("empty")
            else:
                name_list.append("progres")
        print(name_list)
        lp_propably_index = 0
        for x in counter_class:
            print(x)
        print(opis_probably_index)
        print(avg_words_list)

    def find_most_probably_table_headers(self, headers_data_frame):
        "jak tabelka ma wszystkie nazwy to nie ma nan"
        # print("w funkcji find most")
        headers_from_help = []
        for i, row in headers_data_frame.iterrows():
            if self.non_nan_in_row(row=row) and self.non_numerical(row=row):
                headers_from_help = row.values
        return headers_from_help

    def the_same_headers(self, header_1, header_2, p=90):
        "tabelki nie mogą mieć takich samych kolumn jesli mają ich różną ilośc"
        if len(header_1) != len(header_2):
            return False
        similarity_list = []
        "liczyby średnie podobieństwo opisu kolum"
        "domyślnie zwracamy True jeśli jest ono wieksze "
        "od 90 według biblioteki fuzzywuzzy"
        for h_1, h_2 in zip(header_1, header_2):
            similarity_list.append(string_similarity(h_1, h_2))
        avg_sim = np.average(similarity_list)
        # print(avg_sim)
        if avg_sim >= p:
            return True
