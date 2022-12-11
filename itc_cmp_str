def itc_cmp_str(string_1, string_2, number):
    l1 = len(string_1)
    l2 = len(string_2)
    res = ""
    if l1 < number or number < 0:
        print(string_1)
    else:
        for i in range(0, number-1):
            res = res + string_1[i]
        res += string_2
        for i in range(len(string_1)-number-1, len(string_1)):
            res += string_1[i]
    return res
