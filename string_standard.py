from fuzzywuzzy import fuzz


def make_standard_string(before):
    result = str(before)
    result = result.lower().strip()
    return result


def non_dot_string(before):
    result = before.replace(".", "").replace(",", "").replace("/", "")
    return result


def string_similarity(s1, s2):
    s1 = make_standard_string(s1)
    s2 = make_standard_string(s2)
    s1 = non_dot_string(s1)
    s2 = non_dot_string(s2)
    dif_ration = fuzz.ratio(s1, s2)
    return dif_ration


