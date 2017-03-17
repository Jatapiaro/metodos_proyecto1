def add_zeroes(n):
    if len(str(n)) <= 4:
        return str(n).zfill(4)
    else:
        l = len(str(n))
        if(l%2!=0):
            l = l+1
            return str(n).zfill(l)
        else:
            return str(n)

def extract_center(n):
    ##print(len(n))
    l = len(n)
    extract = int((l-4)/2)
    extracOne = extract
    extractTwo = l - extract
    return n[extracOne:extractTwo]

def centros_cuadrados(x,iter=50):
    xn = []
    operador = []
    aleatorio = []
    random = []
    for i in range(0,iter):
        xn.append(x)
        nz = add_zeroes(x*x)
        operador.append(nz)
        nz = extract_center(nz)
        nzi = int(nz)
        aleatorio.append(nzi)
        random.append((nzi/10000))
        x = nzi
        if nzi in xn:
            break
    return xn,operador,aleatorio,random



