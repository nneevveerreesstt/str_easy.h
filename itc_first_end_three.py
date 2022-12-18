def itc_first_end_three(string):
    ln = 0
    for i in string:
        ln += 1
    if ln > 5:
        print(string[0] + string[1] + string[2] + string[ln-3] + string[ln-2] + string[ln-1])
    else:
        for i in range(ln):
            print(string[0], end="")
