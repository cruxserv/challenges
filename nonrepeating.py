def first_non_repeating_letter(string):
    nrc = []
    for i in list(string):
        ls = list(string.lower())
        if ls.count(i.lower()) == 1:
            nrc.append(i)
    if nrc:
        return nrc[0]
    else:
        return ''
