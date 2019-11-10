def maximumToys2(prices, k):
    pricesList = prices.copy()
    budget = k
    numberOfToys = 0
    
    while k >= 0 and pricesList:
        minCost = min(pricesList)
        pricesList.remove(minCost)
        if k - minCost >=0:
            k -= minCost
            numberOfToys += 1
    print(pricesList, budget, numberOfToys)
    return numberOfToys

#maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)
maximumToys2([1, 2, 3, 4], 7)


def maximumToys(prices, k):
    pricesList = prices.copy()
    budget = k
    numberOfToys = 0
    pricesList.sort()
    #print(pricesList)
    for i in range(len(pricesList)):
        minCost = pricesList[i]
        if minCost >= k:
            break
        if k - minCost >=0:
            k -= minCost
            numberOfToys += 1
    #print(pricesList, budget, numberOfToys)
    return numberOfToys

#maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)
maximumToys([1, 2, 3, 4], 7)