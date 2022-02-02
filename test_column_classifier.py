from column_classifier import ColumnClassifier
import pandas as pd


def test_is_lp():
    print("============= test is lp ===========")
    column_classifier = ColumnClassifier()
    expected_r = True
    result = column_classifier.is_lp("1.0")
    print(expected_r == result)
    result = column_classifier.is_lp("  1,5  ")
    expected_r = True
    print(expected_r == result)
    result = column_classifier.is_lp("  1t  ")
    expected_r = False
    print(expected_r == result)
    print("============= end test ============")


def test_is_ilosc():
    print("============= test ilosc ===========")
    column_classifier = ColumnClassifier()
    expected_r = True
    result = column_classifier.is_lp("1.0")
    print(expected_r == result)
    result = column_classifier.is_lp("  1,5  ")
    expected_r = True
    print(expected_r == result)
    result = column_classifier.is_lp("  1t  ")
    expected_r = False
    print(expected_r == result)
    print("============= end test ============")


def test_is_opakowanie():
    print("============= test opakowanie ===========")
    column_classifier = ColumnClassifier()
    expected_r = False
    result = column_classifier.is_opakowanie("1.0")
    print(expected_r == result)
    result = column_classifier.is_opakowanie("op.")
    expected_r = True
    print(expected_r == result)
    result = column_classifier.is_opakowanie("ampułka")
    expected_r = True
    print(expected_r == result)
    print("============= end test ============")


def test_column_avg_len_counter():
    # list of strings
    avg_1 = ['Geeks', 'For', 'Geeks', 'is',
             'portal', 'for']
    avg_2 = ["kot kot", "pies kot", "zagiel kogo", "lol lol", "k k", "tak tak" "nan"]
    df = pd.DataFrame(avg_1)
    df.columns = ["avg_1"]
    df["avg_2"] = avg_2
    print("============= test avg_lenght ===========")
    column_classifier = ColumnClassifier()
    result = column_classifier.avg_word_in_columns(data_frame=df)
    expected_r = [("avg_1", 1.), ("avg_2", 2.)]
    print(result == expected_r)
    print("============= end test ============")


def all_test():
    test_is_lp()
    test_is_ilosc()
    test_is_opakowanie()
    test_column_avg_len_counter()


all_test()
