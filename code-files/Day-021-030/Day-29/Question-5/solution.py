def andOperation(n,k):
    currentMax = float('-inf')
    listOfNumber = [x for x in range(1,n+1)]
    for i in range(n):
        for j in range(i,n):
            if i != j:
                #print(listOfNumber[i],"&",listOfNumber[j],"=",listOfNumber[i]&listOfNumber[j])
                test = listOfNumber[i]&listOfNumber[j]
                if test> currentMax and test < k:
                    currentMax = test
    print(currentMax)
andOperation(955, 236)