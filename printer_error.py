def printer_error(s):
    errors = 0
    error_codes = ['n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letters in s:
        if letters in error_codes:
            errors += 1
    print(f"{errors}/{len(s)}")


printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")
