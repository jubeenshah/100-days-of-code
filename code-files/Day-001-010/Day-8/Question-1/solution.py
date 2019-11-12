def divisibleSumPairs(n, k, ar):
    target = k
    #ar.sort()
    counter = 0
    for i in range(len(ar)-1):
        #print(ar[i:],i)
        for j in range(1+i,len(ar)):
            if i < j and (ar[i]+ar[j])%target == 0:
                #print(i,j,i+j,(i+j)%target)
                counter += 1
    return counter
    """
    target = k
    ar.sort()
    dictMod = {}
    
    for value in range(k):
        dictMod[value] = []
    print(dictMod)
    for element in ar:
        modValue = element % target
        if modValue in dictMod:
            dictMod[modValue].append(element)
    print(dictMod)
    """
   
    
      

divisibleSumPairs(2,3, ar = list(map(int, input().rstrip().split())))