from Algoritmos.HullDobell import has_complete_sequence

"""
xo = (aXo+c) mod m
"""

xo = lambda a,x,c,m: float((a*x)+c)%m

xi = lambda a,x,m: float(a*x)%m

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
    for i in range(0,iter):
        xn.append(x)
        ni = xo(a,x,c,m)
        xni.append(ni)
        random.append(ni/m)
        x = ni
    return xn,xni,random


def congruencial_multiplicativo(x,a,m,iter=20):
    xn = []
    xni = []
    random = []
    for i in range(0,iter):
        xn.append(x)
        ni = xi(a, x, m)
        xni.append(ni)
        random.append(ni / m)
        x = ni
        if ni in xn:
            break
    return xn,xni,random

