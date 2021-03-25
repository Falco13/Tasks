def slice_less(my_list, lesser):
    return sorted(filter(lambda x: x > lesser, my_list))[::-1]


print(slice_less([5, 2, 9, 7, 11, 56, 31, 45, 39, 16, 28, 13, 1, 19], 17))
