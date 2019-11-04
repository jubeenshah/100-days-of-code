def sockMerchant(n, ar):
    globalArr = []
    numPairs = 0
    for i in ar:
        #print(globalArr)
        if i in globalArr:
            numPairs += 1
            globalArr.remove(i)
        else:
            globalArr.append(i)
    return numPairs


ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = len(ar)

x = sockMerchant(n,ar)
print(x)