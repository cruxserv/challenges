def rgb(r, g, b):
    if r < 0:
        r = 0
    if r > 255:
        r = 255
    if g < 0:
        g = 0
    if g > 255:
        g = 255
    if b < 0:
        b = 0
    if b > 255:
        b = 255

    r = hex(r)[2:4]
    g = hex(g)[2:4]
    b = hex(b)[2:4]
    if len(r) == 1:
        r = '0' + r
    if len(b) == 1:
        b = '0' + b
    if len(g) == 1:
        g = '0' + g
    res = r+g+b
    print(res.upper())

    # print(letters)
# rgb(255, 255, 255)


rgb(0, 0, 0)
# rgb(1, 2, 3)
