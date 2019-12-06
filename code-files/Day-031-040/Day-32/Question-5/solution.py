dictOfFactorials = {}
def factorials(n):
    #print(dictOfFactorials)
    if n in dictOfFactorials:
        return dictOfFactorials[n]
    if n == 0 or n == 1:
        return 1
    dictOfFactorials[n] = n * factorials(n-1)
    return (n * factorials(n-1))
factorials(203)