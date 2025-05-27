from typing import List


def maxProfit(prices: List[int]) -> int:
    maxProfitValue=0
    minPrice = float('inf') # initializing the minPrice to positive infinity.
    for i in prices:
            minPrice = min(minPrice,i)
            maxProfitValue = max(maxProfitValue,i-minPrice)
    return maxProfitValue

    # maxProfitValue=0
    # for i in range(len(prices)):
    #         profitDiff = prices[i+1]-prices[i]
    #         maxProfitValue = max(maxProfitValue,profitDiff)
    # return maxProfitValue
print(maxProfit([10,1,5,6,7,1])) #output =6
