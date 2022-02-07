from reader import Reader
from line_classifier import LineClassifier
from column_classifier import ColumnClassifier

line_classifier = LineClassifier()
column_classifier = ColumnClassifier()
reader = Reader(line_classifier=line_classifier, column_classifier=column_classifier)


def processing_excel(path, save_path, start=0):
    return reader.final_fun(path=path, save_path=save_path, start=start)
