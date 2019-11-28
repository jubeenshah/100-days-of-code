def utopianCycle(n):
    height = 0
    dictOfHeights = {}
    for i in range(n+1):
        if i % 2 != 0:
            height *= 2
        else:
            height += 1
        dictOfHeights[i] = height
    #print(dictOfHeights)
    return height
utopianCycle(5)