# Write a function that finds the missing number in an array

input_array = [1, 2, 3, 4, 6, 7]
# Output = 5

def missNum(arr):
    for ind, num in enumerate(arr):
        if (arr[ind +1] - num) != 1:
            return num + 1

print(missNum(input_array))
