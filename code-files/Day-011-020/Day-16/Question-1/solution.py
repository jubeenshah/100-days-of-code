import math
def pageCount(n,p):
    if n < p:
        return 0
    if p == 1:
        return 0
    if n % 2 != 0:
        if (n == p or p == n-1):
            return 0
        else:
            print(min(math.floor(p/2),math.floor((n-p)/2)))
    if n % 2 == 0:
        print(min(math.floor(p/2),math.ceil((n-p)/2)))
        


pageCount(18183,18042)