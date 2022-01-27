def maximo (a,b,c):
    if a >= b and b >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
