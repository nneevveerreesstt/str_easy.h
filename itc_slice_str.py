def itc_slice_str(string, start, end):
    ln = 0
    for i in string:
        ln += 1
    res = ""
    if start < 0:
        start = 0
    if start > end:
        return string
    i = start 
    while i <= end and i < ln:
        res += string[i]
        i += 1
    return res
