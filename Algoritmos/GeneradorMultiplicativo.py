xo = lambda a,x,m: (a*x)%m

def congruencial_multiplicativo(x,a,m,iter=50):
    xn = []
    xni = []
    random = []
    for i in range(0,iter):
        xn.append(x)
        ni = xo(a, x, m)
        xni.append(ni)
        random.append(ni / m)
        x = ni
        if ni in xn:
            break
    return xn,xni,random