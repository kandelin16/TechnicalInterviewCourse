# Write a merge sort algorithm to sort an array. 
# The function should return the sorted array.

# two examples
array1 = [45, 98, 3, 24, 15, 77, 9, 50] # output: [3, 9, 15, 24, 45, 50, 77, 98]
array2 = [18, 16, 27, 4, 12] # output: [4, 12, 16, 18, 27]
import math

def mergeSort(arr):
    mergeSortTwo(arr, 0, len(arr)-1)
    return arr

def mergeSortTwo(arr, first, last):
    if first < last:
        middle = (first + last) //2
        mergeSortTwo(arr, first, middle)
        mergeSortTwo(arr, middle+1, last)
        merge(arr, first, middle, last)
    return arr

def merge(arr, first, middle, last):
    left = arr[first:middle+1]
    right = arr[middle+1:last+1]
    left.append(math.inf)
    right.append(math.inf)
    i = j = 0
    for k in range(first, last +1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
    return arr

print(mergeSort(array1))
print(mergeSort(array2))