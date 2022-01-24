array = [1,3,5,7,9,11,15]
import enum
import math
def binarySearch(arr, targ):
    lower = 0
    upper = len(arr) -1
    while lower <= upper:
        middle = (lower + upper) // 2
        if arr[middle] == targ:
            return middle
        elif arr[middle] < targ:
            lower = middle + 1
        else:
            upper = middle - 1
    
    return "Not Found"

# print(binarySearch(array, 3))
# print(binarySearch(array, 9))
# print(binarySearch(array, 6))



input_array = [3,4,5,6,1,2]
input_array = [5,2,3,4]
input_array = [1,2,3,4]

def problem1(arr):
    # minimum = math.inf
    lower = 0
    upper = len(arr) -1
    while lower <= upper:
        middle = (lower + upper) // 2
        if arr[middle] < arr[middle -1]:
            return arr[middle]
        elif arr[middle] > arr[upper]:
            lower = middle + 1
        else:
            upper = middle - 1



#print(problem1(input_array))

arrey = [1,2,3,4]
# output = [24,12,8,6]

def problem5(arr):
    output = []
    for index in range(0, len(arr)):
        product = 1
        for index2, element2 in enumerate(arr):
            if index2 != index:
                product *= element2 
        output.append(product)
    return output

print(problem5(arrey))