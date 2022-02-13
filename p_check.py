def p_check(s):
    openers = ["(", "{", "["]
    closers = [")", "}", "]"]
    test = s
    for symbol in test:
        if symbol in openers:
            check = openers.index(symbol)
            must = closers[check]
            if must not in test:
                print(0)
            else:
                print(1)


p_check(“{[]()}”)
