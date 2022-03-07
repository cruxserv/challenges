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

    r = hex(r)[2:]
    g = hex(g)[2:]
    b = hex(b)[2:]
    if len(r) == 1:
        r = '0' + r
    if len(b) == 1:
        b = '0' + b
    if len(g) == 1:
        g = '0' + g
    res = r+g+b
    return res.upper()

# def rgb(r, g, b):
#     def get_hex(s):
#         if s > 255: s = 255
#         if s < 0: s = 0
#         return hex(s)[2:].upper() if len(hex(s)[2:]) > 1 else "0" + hex(s)[2:]
#     return get_hex(r) + get_hex(g) + get_hex(b)
