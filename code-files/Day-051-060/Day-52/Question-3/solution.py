prices = [7,1,5,3,6,4]
def maxProfit(prices):
    maxProfitPrice, buyPrice = float('-inf'), float('inf')
    for currentPrice in prices:
        if currentPrice < buyPrice:
            buyPrice = currentPrice
        if currentPrice - buyPrice > maxProfitPrice:
            maxProfitPrice = currentPrice - buyPrice
    return maxProfitPrice

maxProfit(prices)