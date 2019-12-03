def saveThePrisoner(n, m, s):
    a=0
    a=(m+s-1)%n
    if a==0:
        return n
    else:
        return a
    
saveThePrisoner(715950220, 876882456, 195550680)