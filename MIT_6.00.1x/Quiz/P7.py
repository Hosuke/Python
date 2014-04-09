# By Huang Geyang
def McNuggets(n):
    c = 3 - n % 3
    if c!= 3:
        n -= c*20
    else:
        c = 0
    b = n // 3 % 2
    n -= b*9
    a = n // 6
    return a >= 0
