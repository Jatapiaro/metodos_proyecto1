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
    print(len(n))
    l = len(n)
    extract = int((l-4)/2)
    extracOne = extract
    extractTwo = l - extract
    return n[extracOne:extractTwo]



