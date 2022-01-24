# Search an array of numbers to find a target number using binary search.
# The function should return the index of the target number if the target number is found
# or a -1 if the target is not found in the array.

input_array = [1, 2, 5, 9, 12, 15, 21, 28, 99, 100, 117]
input_target = 5
targ2 = 15
targ3 = 99
targ4 = 3
# Output = 2

def binarySearch(arr, targ):
    lowBound = 0
    highBound = len(arr) -1
    while arr[lowBound] != targ or arr[highBound] != targ:
        midBound = (lowBound + highBound)//2
        if arr[midBound] == targ:
            return midBound
        elif arr[midBound] > targ:
            highBound = midBound
        elif arr[midBound < targ]:
            lowBound = midBound
    return -1
        
print(binarySearch(input_array, input_target))
print(binarySearch(input_array, targ2))
print(binarySearch(input_array, targ3))