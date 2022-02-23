def validate_pin(pin):
    if len(list(pin)) == 4 or len(list(pin)) == 6:
        try:
            [int(x) for x in pin]
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)


# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()
