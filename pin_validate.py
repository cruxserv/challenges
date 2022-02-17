def validate_pin(pin):
    if len(list(pin)) == 4 or len(list(pin)) == 6:
        try:
            [int(x) for x in pin]
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)


validate_pin("-12345")

validate_pin("1.234")

validate_pin("a234")

validate_pin(".234")
