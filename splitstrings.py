def solution(s):
    output = []
    while len(list(s)) > 2:
        output.append(s[:2])
        s = s[2:]
        continue
    if len(list(s)) == 2:
        output.append(s)
    if len(list(s)) == 1:
        output.append(s+'_')
    return output
