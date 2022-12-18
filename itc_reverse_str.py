def itc_reverse_str(string):
    ln = 0
    for i in string:
        ln += 1
    res = ""
    for i in range(ln - 1, -1, -1):
        res += string[i]
    return res
