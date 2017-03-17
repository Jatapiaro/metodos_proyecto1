from Algoritmos.HullDobell import has_complete_sequence

"""
xo = (aXo+c) mod m
"""
xo = lambda a,x,c,m: ((a*x)+c)%m

def congruencial_lineal(x,a,c,m,iter=50):
    xn = []
    xni = []
    random = []
    for i in range(0,iter):
        xn.append(x)
        ni = xo(a, x, c, m)
        xni.append(ni)
        random.append(ni / m)
        x = ni
        if ni in xn:
            break
    return xn,xni,random

def congruencial_mixto(x,a,c,m,iter=50):
    xn = []
    xni = []
    random = []
    if has_complete_sequence(a,m,c):
        for i in range(0,m):
            xn.append(x)
            ni = xo(a,x,c,m)
            xni.append(ni)
            random.append(ni/m)
            x = ni
    else:
        for i in range(0,iter):
            xn.append(x)
            ni = xo(a,x,c,m)
            xni.append(ni)
            random.append(ni/m)
            x = ni

    return xn,xni,random

