array = [1,2,3,4,5, "l", "m"]
import math
def reversal(arr):
    result = []
    for index in range(len(arr)-1, -1, -1):
        result.append(arr[index])
    return result

def reversalOptimized(arr):
    for index in range(0, math.floor(len(arr)/2)):
        temp = arr[index]
        arr[index] = arr[len(arr)-index-1]
        arr[len(arr)-index-1] = temp
    return arr


reversalOptimized(array)


#has serious issues! when the array gets popped the index changes, but the 
input_array = [-1, 2, -3, 4, 5, 7]

def negativeMove(arr):
    indexesToDelete = []
    for ind in range(0, len(arr)):
        if arr[ind] < 0:
            element = arr.pop(ind)
            arr.append(element)
    return arr

negativeMove(input_array)

input = [[2,7,8],[7,1,3],[1,9,5]]
def richestPerson(input):
    richAmount = 0
    for customer in input:
        sum = 0
        for index in range(0, len(customer)):
            sum+= customer[index]
        if sum > richAmount:
            richAmount = sum
    return(richAmount)

def richestPerson2(input):
    richAmount = 0
    for customer in input:
        dasum = sum(customer)
        if dasum > richAmount:
            richAmount = dasum
    return(richAmount)

print(richestPerson2(input))