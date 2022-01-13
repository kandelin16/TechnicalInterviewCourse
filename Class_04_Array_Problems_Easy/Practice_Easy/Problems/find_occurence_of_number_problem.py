# Write a function that finds the occurrence of a number in an array

input_array = [1, 2, 5, 3, 5, 5, 5, 7, 5 , 5, -5]
input_target = 5
# Ouptut = 6

def occ(arr, targ):
    resultDict = {}
    for num in arr:
        if num in resultDict:
            resultDict[num] +=1
        else:
            resultDict[num] = 1
    return resultDict[targ]

def occ2(arr, targ):
    count = 0
    for num in arr:
        if num == targ:
            count+=1
    return count

print(occ(input_array, input_target))
print(occ2(input_array, input_target))