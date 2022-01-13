# Write a function that finds the minimum and maximum in an array 

input_array = [1, 2, 7, 9, -11, 10, 20, 1037]
# Output = -11, 1037

import math

def minmax(arr):
    max = 0
    min = math.inf
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    return [min, max]

print(minmax(input_array))