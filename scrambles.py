def scramble(s1, s2):
    for l in set(s2):
        if s2.count(l) > s1.count(l):
            return False
    return True
