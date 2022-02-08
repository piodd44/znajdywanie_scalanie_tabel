from reader import Reader
from line_classifier import LineClassifier
from column_classifier import ColumnClassifier

line_classifier = LineClassifier()
column_classifier = ColumnClassifier()
reader = Reader(line_classifier=line_classifier, column_classifier=column_classifier)

"jeśli podamy ścieżke zapiu to wyniki zostana zapisane w formacie csv a jeśli nie to nie zostaną zapisane"
"jeśli nie zapisujemy to funkcja jedynie zwróci liste data_frame z pandas"
"liste gdyż jeśli wykryje rózne tabele to je pogrupuje i każdą grupe scali osobno"

"start oznacza od którego pod arkusza ma zacząć poszukiwania ( w sumie pewnie warto było by dodać jeszcze end ) "


def processing_excel(path, save_path=None, start=0):
    if save_path is None:
        save = False
    else:
        save = True
    return reader.final_fun(path=path, save_path=save_path, start=start, save=save)
