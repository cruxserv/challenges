from collections import Counter


def scramble(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    for i in s2:
        print(i)
        if s2.count(i) <= s1.count(i):
            continue
        else:
            print(False)
            break
        print(True)


scramble('cedewaraaossoqqyt', 'codewars')
