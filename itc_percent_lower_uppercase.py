def itc_percent_lower_uppercase(string):
    up = 0
    low = 0
    ln = 0
    for i in string:
        ln += 1
    for i in range(ln):
        if "A" <= string[i] <= "Z":
            up += 1
        elif "a" <= string[i] <= "z":
            low += 1
    return (up/low)*100
