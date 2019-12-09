def equalizeArray(arr):
    if not arr:
        return 0
    dictOfArray = {x:0 for x in arr}
    for eachElement in arr:
        dictOfArray[eachElement] += 1
    dictOfArray = (sorted(dictOfArray.items(), key=lambda lv: lv[1]))
    maxElement,maxValue = dictOfArray[-1][0],dictOfArray[-1][1]
    dictOfArray = dict(dictOfArray)
    print(dictOfArray,maxElement,maxValue)
    numberOfRemovals = 0
    for element, value in dictOfArray.items():
        #print(dictOfArray)
        while dictOfArray[element] != 0:
            #print(dictOfArray)
            if value <= maxValue and element !=maxElement:
                numberOfRemovals += 1
                dictOfArray[element] -= 1
                #print(element)
            else:
                break
    return numberOfRemovals
        

equalizeArray([1,2]*100)