def itc_equal_reverse(string):
    res = ""
    ln = 0
    for i in string:
        ln += 1
    for i in range(ln - 1, -1, -1):
        res += string[i]
    if string == res:
        return True
    else:
        return False
