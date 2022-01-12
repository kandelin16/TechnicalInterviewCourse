# Given an array of integers, find if the array contains any duplicates
# Your function should return false if every element is distinct.
# This problem came from leetcode.com

input_array = [1, 2, 3, 3, 4]
# Output = True

def duplicates(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return True
    
    return False

def duplicatesOptimal(array):
    runningDict = {}
    for int in array:
        if int in runningDict:
            return True
        else:
            runningDict[int] = 1
    return False
        

print(duplicates(input_array))
print(duplicates([1,2,3]))

print(duplicatesOptimal(input_array))
print(duplicatesOptimal([1,2,3]))