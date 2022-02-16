def array_diff(a, b):
    new_list = [i for i in a if i not in b]
    return new_list


# array_diff([1, 2, 2], [2])
# array_diff([1, 2, 3], [1, 2])
