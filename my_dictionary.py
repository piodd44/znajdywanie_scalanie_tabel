class MyDictionary:
    def __init__(self):
        self.opakowanie_set = set({})
        self.__create_opakowanie_set__()
        self.lp_set = set({})
        self.__create_lp_set__()
        self.ilosc_set = set({})
        self.__create_ilosc_set__()
        self.nazwa_set = set({})
        self.__create_nazwa_set__()
        self.opis_set = set({})
        self.__create_opis_set__()

    def __create_opakowanie_set__(self):
        opakowanie = ["opakowanie", "op", "op."]
        opakowanie += ["ampułka", "amp", "amp."]
        opakowanie += ["fiolka", "fiol", "fiol."]
        opakowanie += ["tupka"]
        opakowanie += ["szt"]
        opakowanie += ["gram"]
        opakowanie += ["wstrzykiwacz"]
        opakowanie += ["wkład", "wkł", "wkł."]
        opakowanie += ["butelka", "but", "but."]
        opakowanie += ["kapsułka", "kaps", "kaps."]
        opakowanie += ["fl", "fl."]
        opakowanie += ["szaszetka", "sasz", "sasz."]
        opakowanie += ["tabletka", "tabl", "tabl."]
        opakowanie += ["czopek", "czop", "czop."]
        opakowanie += ["poj", "poj."]
        opakowanie += ["drażetka", "draż"]
        opakowanie += ["plaster"]
        opakowanie += ["j.m.", "j.m", "jm", "jednostka", "jednostki", "miary"]
        for x in opakowanie:
            self.opakowanie_set.add(x)

    def __create_lp_set__(self):
        lp = ["LP.", "lp.", "lp", "l.p.", "lp"]
        for x in lp:
            self.lp_set.add(x)

    def __create_ilosc_set__(self):
        ilosc = ["ilość.", "ilość", "ilosc", "ilośc", "ilosć"]
        for x in ilosc:
            self.ilosc_set.add(x)

    def __create_nazwa_set__(self):
        nazwa = ["nazwa"]
        for x in nazwa:
            self.nazwa_set.add(x)

    def __create_opis_set__(self):
        nazwa = ["opis"]
        for x in nazwa:
            self.opis_set.add(x)

    def get_opakowanie_set(self):
        return self.opakowanie_set

    def get_lp_set(self):
        return self.lp_set

    def get_ilosc_set(self):
        return self.ilosc_set

    def get_nazwa_set(self):
        return self.nazwa_set

    def get_opis_set(self):
        return self.opis_set
