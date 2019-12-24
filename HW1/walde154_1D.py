def pairInTriple(a,b):
    asq = a**2
    bsq = b**2
    c = (asq + bsq)
    if asq + bsq == int(c**.5)**2:
        return True
    else:
        c = abs(asq - bsq)
        if c == int(c**.5)**2:
            return True
    return False
def maxOfTriple(x):
    for y in range(1,x):
        for z in range(1,x):
            if y**2 + z**2 == x **2:
                return True
    return False
