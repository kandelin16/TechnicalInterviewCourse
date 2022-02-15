def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    
    greater = []
    lower = []

    for element in arr:
        if element > pivot:
            greater.append(element)
        else:
            lower.append(element)
    return quicksort(greater) + [pivot] + quicksort(lower)

print(quicksort([9,8,5,10,3,1]))