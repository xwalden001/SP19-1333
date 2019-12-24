def pairInTriple(a,b):
    c = a**2 + b**2
    if int(c ** 0.5) ** 2 == c:
        return True
    else:
        c = abs(a * a - b * b)
        if int(c ** 0.5) ** 2 == c:
            return True
    return False


def maxOfTriple(n):
    for i in range(1, n):
        for j in range(1, n):
            if i ** 2 + j ** 2 == n ** 2:
                return True
    return False

print(pairInTriple(3,5))
print(pairInTriple(3,4))
print(pairInTriple(7,5))
print(maxOfTriple(12))
print(maxOfTriple(13))    
