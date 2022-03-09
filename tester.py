def scramble(s1, s2):
    for i in s2:
        if s2.count(i) > s1.count(i):
            return False
    return True


scramble('cedewaraaossoqqyt', 'codewars')
