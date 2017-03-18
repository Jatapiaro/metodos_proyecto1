def add_zeroes(n,seedl):
    if len(str(n)) <= seedl:
        return str(n).zfill(seedl)
    else:
        l = len(str(n))
        if(l%2!=0):
            l = l+1
            return str(n).zfill(l)
        else:
            return str(n)

def extract_center(n,seedl):
    ##print(len(n))
    l = len(n)
    extract = int((l-seedl)/2)
    extracOne = extract
    extractTwo = l - extract
    return n[extracOne:extractTwo]

def centros_cuadrados(x,iter=50):
    seedl = len(str(x))
    div = float(pow(10,seedl))
    xn = []
    operador = []
    aleatorio = []
    random = []
    for i in range(0,iter):
        xn.append(x)
        nz = add_zeroes(x*x,seedl)
        operador.append(nz)
        nz = extract_center(nz,seedl)
        nzi = int(nz)
        aleatorio.append(nzi)
        random.append(float(nzi/div))
        x = nzi
        if nzi in xn:
            break
    return xn,operador,aleatorio,random



