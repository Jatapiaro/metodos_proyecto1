from Algoritmos.HullDobell import has_complet_sequence

"""
xo = (aXo+c) mod m
"""
xo = lambda a,x,c,m: ((a*x)+c)%m

def congruencial(x,a,c,m,iter=50):
    xn = []
    xni = []
    random = []
    if has_complet_sequence(a,m,c):
        for i in range(0,m):
            xn.append(x)
            ni = xo(a,x,c,m)
            xni.append(ni)
            random.append(ni/m)
    else:
        for i in range(0,iter):
            xn.append(x)
            ni = xo(a,x,c,m)
            xni.append(ni)
            random.append(ni/m)

    return xn,xni,random

