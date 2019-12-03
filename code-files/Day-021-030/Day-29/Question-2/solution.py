from collections import Counter
numberOfShoes = int(input())
listOfShoeSizes = list(map(int,input().split(' ')))
numberOfCustomers = int(input())
purchaseList = []
for eachCustomer in range(numberOfCustomers):
    purchaseList.append(list(map(int,input().split(' '))))

def calculateMoneyEarned(purchaseList, listOfShoeSizes,numberOfCustomers,numberOfShoes):
    #print(purchaseList,listOfShoeSizes,numberOfCustomers,numberOfShoes)
    dictOfAvailableShoeSizes = Counter(listOfShoeSizes)
    moneyEarned = 0
    for eachPurchaseItem in purchaseList:
        if (eachPurchaseItem[0] in dictOfAvailableShoeSizes and dictOfAvailableShoeSizes[eachPurchaseItem[0]] > 0):
            dictOfAvailableShoeSizes[eachPurchaseItem[0]] -= 1
            moneyEarned += eachPurchaseItem[1]
        else:
            continue
    print(moneyEarned)

calculateMoneyEarned(purchaseList,listOfShoeSizes,numberOfCustomers,numberOfShoes)