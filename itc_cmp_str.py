def itc_cmp_str(str1, str2, num):
    ln1 = 0
    ln2 = 0 
    for i in str1:
        ln1 += 1
    for i in str2:
        ln2 += 1
    t_str = ""
    f_str = ""
    if ln1 < num or num < 0:
        return str1
    for i in range(num):
        t_str += str1[i]
    for i in range(ln2):
        t_str += str2[i]
    for i in range(num, ln1):
        t_str += str1[i]
    for i in range(ln1):
        f_str += t_str[i]
    return f_str
