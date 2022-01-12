# Say you have an array for which the ith element is the price of a given stock on day i
# If you were only permitted to complete at most one transaction (i.e, buy one and 
# sell one share of the stock) design an algorithm to find the maximum profit
# This problem came from leetcode.com

input_array = [7, 1, 5, 3, 6, 4]
# Output = 5
import math

def TradeBot(array):
    floatMin = [1000000000, 0]
    floatMax = [0,0]
    for index, price in enumerate(array):
        if price < floatMin[0]:
            floatMin = [price, index]
        if price > floatMax[0] and index > floatMin[1]:
            floatMax = [price, index]
    return floatMax[0] - floatMin[0]

def TradeBotOptimized(array):
    floatMin = [math.inf, 0]
    floatMax = [0,0]

    if len(array) == 0:
        return 0

    for index, price in enumerate(array):
        if price < floatMin[0]:
            floatMin = [price, index]
        if price > floatMax[0] and index > floatMin[1]:
            floatMax = [price, index]
    return floatMax[0] - floatMin[0]

print(TradeBot(input_array))

print(TradeBot([10,0,25,4,5]))

print(TradeBotOptimized(input_array))

print(TradeBotOptimized([10,0,25,4,5]))