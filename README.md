# znajdywanie_scalanie_tabel

Program ma za zadanie znajdować i scalać tabele oraz nadawać im z góry zadane nazwy kolumn 
tak aby np. ułatwić zapis ich do bazy danych 

Obecnie program powinnień radzić sobie z znajdywaniem tabel 
oraz oceną czy tabele posiadają takie same kolumny 
generalnie czy są takie same 
obecnie jednak program po prostu przerywa działanie jeśli tabele
nie są takie same lecz docelowo bedzie grupować tabele które 
są takie same i je bedzie scalac i nadawać im odpowiednie nazwy kolumn


Program stara się nadać ujednolicone nazwy kolumn lecz 
za pewne jeszcze nie działą to w pełni dobrze




Pomysł na działą nie programu jest nastepujący

otwarcie pliku i zapisanie go jako dataframe (pandas) 
przeglodniecie dataframe i znalezienie tabelek 
zapisanie tych tabelek odzielnie 

nastepnie nadanie nagłówków tabelką 
pogrupowanie tabelek o takich samych nagłówkach

scalene pogurpowanych tabelek 
nadanie ujednoliconej nazwy kolumn scalonym tabelką 

zwrócenie scalonych tabelek jako data_frame
zapisanie do pliku csv 



Co odopowiada za co w programie 

Reader:
        najważniejsza cześć programu w niej znajduje się funkcja która przyjmuje 
        ścieżke do pliku i zwraca scalone data_frame 

find_start_end_table_index
                 ma za zadanie wykryc tabelke (jej koniec i początek) 

make_class_row
                 korzysta z line_classifier aby każdemu wierszu nadać klase która jest pomocna przy znajdywaniu 
                 poczatku i konca tabeli . obecnie są to klasy (start_2,start_1,start_0,non-recognize,empty) 
                 start_i - prawdopodobnie dane znajdują się o "i" miejsc w du



LineClassifier: ma za zadanie przydzielić klase wierszą 
                np. czy wiersz jest pusty czy wiersz wygloda jak by zaraz miała zacząć się tabelka itp 
                
                
ColumnClasifier:
               &ensp ma za zadanie przydzielić nazwy kolumn 
                na razie przydziela głównie za pomocą wierszy nad tabelką 
                docelowo bedzie jeszcze korzystał z całej kolumny 
                aby uwiarygonić poprzedni wynik bądz znaleść nazwe 
                jeśli poprzednia metoda nie znalazła 
                (to ma sens raczej dla dużych plików gdzie można 
                np. poprzez zliczanie wystopień nazw w kolumnach 
                przewidzieć jaka to jest kolumna. np w kolumnie 
                która powinna być oznaczona jako "opakowanie" 
                będą czesto pojawiać się nazwy opakowań a w innych kolumnach już nie tak czesto albo wcale) 
                
                
standard_string:
                po prostu pomaga w formatowaniu wszystkich stringów w ten sam sposób w programie
                co na razie nie jest w pełni używane gdyż w niektórych miejsach wciaż jest lekki bałagan
                
                jak także posiada metode która zwraca czy dwa stringi są do siebie podobne 
                pomocne przy ustalaniu czy dwie tabelki są takie same 
                (czy mają takie same opisy kolumn lub bardzo podobne gdyż czasem w nagłówkach kolumna mogą być literówki 
                lecz wciaż powinny być uznane za takie same kolumny)
                




