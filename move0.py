def move_zeros(a):
    l = 0

    for r in range(len(a)):
        if a[r]:
            a[l], a[r] = a[r], a[l]
            l += 1

    return a
