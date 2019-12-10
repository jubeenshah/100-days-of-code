dictOfFactorial = {}
def factorial(n)->int:
    if n == 0 or n == 1:
        return 1
    if n in dictOfFactorial:
        print(n,dictOfFactorial[n])
        return dictOfFactorial[n]
    dictOfFactorial[n] = n * factorial(n-1)
    return n * factorial(n-1)
factorial(15)

def numberOfZeros(n)->int:
    getFactorial = factorial(n)
    trailingZeros = 0
    #print(getFactorial)
    while getFactorial>0:
        #print(getFactorial)
        if getFactorial % 10 == 0:
            trailingZeros += 1
            getFactorial = getFactorial // 10
        else:
            break
    return trailingZeros
numberOfZeros(10)