def itc_first_end_three(string):
    ln = 0
    new_str = ""
    for i in string:
        ln += 1
    if ln <= 1:
        return "-1"
    for i in range(1, ln, 2):
        new_str += string[i]
    return new_str
