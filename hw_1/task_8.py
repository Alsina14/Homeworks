def equation(x: str):
    """receives an input string with an equation of the form '5 + 6 = 11'
    and returns True or False"""
    k = x.split()
    s = 0
    if k[1] == '+':
        s = float(k[0]) + float(k[2])
    elif k[1] == '-':
        s = float(k[0]) - float(k[2])
    elif k[1] == '*':
        s = float(k[0]) * float(k[2])
    elif k[1] == '/':
        s = float(k[0]) / float(k[2])
    return s == float(k[4])
   