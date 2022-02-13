# 89,1 = 8**1+9**2
def dig_pow(n, p):
    total = 0
    digits = [int(d) for d in str(n)]

    for i in range(len(digits)):
        x = digits[i]**(p+i)
        total = total + x
    if total % n == 0:
        return(total//n)
    else:
        return(-1)
