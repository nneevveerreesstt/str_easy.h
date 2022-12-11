def itc_reverse_str(string):
    res = ""
    for i in range(len(string) - 1, -1, -1):
        res += string[i]
    return res
