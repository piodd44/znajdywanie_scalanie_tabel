from reader import final_fun


def test_3():
    path = "zad4.xlsx"
    save_path = 'test_4_5.csv'
    final_fun(path=path, save_path=save_path)


def test_4():
    path = "test_1.xlsx"
    save_path = 'test_1_4.csv'
    final_fun(path=path, save_path=save_path)


def test_zad_1():
    path = "zad_1.xlsx"
    save_path = 'my_zad_1.csv'
    final_fun(path=path, save_path=save_path)


def test_zad_2():
    path = "zad_2.xlsx"
    save_path = 'my_zad_2.csv'
    final_fun(path=path, save_path=save_path)


def test_zad_3():
    path = "zad_3.xlsx"
    save_path = 'my_zad_3.csv'
    final_fun(path=path, save_path=save_path)


def test_zad_4():
    path = "zad_4.xlsx"
    save_path = 'my_zad_4.csv'
    final_fun(path=path, save_path=save_path)


def test_zad_5():
    path = "zad_5.xlsx"
    save_path = "my_zad_5.csv"
    final_fun(path=path, save_path=save_path)


test_zad_2()
#test_zad_3()
#test_zad_4()
#test_zad_5()