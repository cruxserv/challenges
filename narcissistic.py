def narcissistic(value):
    a = [int(x) for x in str(value)]
    total = 0
    for i in a:
        total += i**(len(a))
    return True if total == value else False

# def narcissistic( value ):
    # return value == sum((int(x)**(len(str(value)))) for x in str(value))
