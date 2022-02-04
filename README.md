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
<br />
<br />
<br />
<br />
Pomysł na działą nie programu jest nastepujący
<br />

otwarcie pliku i zapisanie go jako dataframe (pandas) <br />
przeglodniecie dataframe i znalezienie tabelek <br />
zapisanie tych tabelek odzielnie <br />

nastepnie nadanie nagłówków tabelką <br />
pogrupowanie tabelek o takich samych nagłówkach<br />
<br />
scalene pogurpowanych tabelek <br />
nadanie ujednoliconej nazwy kolumn scalonym tabelką <br />
<br />
zwrócenie scalonych tabelek jako data_frame<br />
zapisanie do pliku csv <br />
<br />
<br />
<br />
Co odopowiada za co w programie <br />

Reader:<br />
        najważniejsza cześć programu w niej znajduje się funkcja która przyjmuje <br />
        ścieżke do pliku i zwraca scalone data_frame <br />
<br />
find_start_end_table_index<br />
                 ma za zadanie wykryc tabelke (jej koniec i początek) <br />
<br />
make_class_row<br />
                 korzysta z line_classifier aby każdemu wierszu nadać klase która jest pomocna przy znajdywaniu <br />
                 poczatku i konca tabeli . obecnie są to klasy (start_2,start_1,start_0,non-recognize,empty) <br />
                 start_i - prawdopodobnie dane znajdują się o "i" miejsc w du<br />
<br />
<br />
<br />
LineClassifier: <br />
                ma za zadanie przydzielić klase wierszą <br />
                np. czy wiersz jest pusty czy wiersz wygloda jak by zaraz miała zacząć się tabelka itp <br />
<br />           
<br />        
ColumnClasifier:<br />
                ma za zadanie przydzielić nazwy kolumn <br />
                na razie przydziela głównie za pomocą wierszy nad tabelką <br />
                docelowo bedzie jeszcze korzystał z całej kolumny <br />
                aby uwiarygonić poprzedni wynik bądz znaleść nazwe <br />
                jeśli poprzednia metoda nie znalazła <br />
                (to ma sens raczej dla dużych plików gdzie można <br />
                np. poprzez zliczanie wystopień nazw w kolumnach <br />
                przewidzieć jaka to jest kolumna. np w kolumnie <br />
                która powinna być oznaczona jako "opakowanie" <br />
                będą czesto pojawiać się nazwy opakowań a w innych kolumnach już nie tak czesto albo wcale) <br />
                <br />
                <br />
standard_string:<br />
                po prostu pomaga w formatowaniu wszystkich stringów w ten sam sposób w programie<br />
                co na razie nie jest w pełni używane gdyż w niektórych miejsach wciaż jest lekki bałagan<br />
                <br />
                jak także posiada metode która zwraca czy dwa stringi są do siebie podobne <br />
                pomocne przy ustalaniu czy dwie tabelki są takie same <br />
                (czy mają takie same opisy kolumn lub bardzo podobne gdyż czasem w nagłówkach kolumna mogą być literówki <br />
                lecz wciaż powinny być uznane za takie same kolumny)<br />
                




