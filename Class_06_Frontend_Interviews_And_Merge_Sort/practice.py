#[3,2,3] -> 3
#[2,2,1,1,1,2,2] -> 2
input = [3,2,3]
def majorityElement(arr):
    returnDict = {}
    for element in arr:
        if element in returnDict:
            returnDict[element] += 1
        else:
            returnDict[element] = 1
    for key in returnDict:
        if returnDict[key] > (len(arr)//2):
            return key

print(majorityElement(input))

# def majorityElementMergeSort(arr):
#     merge2(arr, 0, len(arr) -1)
#     return arr

# def merge2(arr, first, last):

