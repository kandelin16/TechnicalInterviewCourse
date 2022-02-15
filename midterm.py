old_dict = { 'A' : [1, 2, 3], 'B' : [1, 7, 3], 'C' : [100, 3, 7], 'D' : [6, 50, 4]}
output = [['C', 110], ['D', 60], ['B', 11], ['A', 6]]

# Given a dictionary, sort the keys by the sum of their values in descending order. Return an array with the sorted pairs.

def sortKeysByValues(d):
    d2 = {key: sum(value) for key, value in d.items()}
    return {key:value for key, value in sorted(d2.items(), key=lambda item : item[1], reverse=True)}

#print(sortKeysByValues(old_dict))


#Write a function that calculates the sum of an array of numbers using recursion. You must use recursion to gain full credit for this question.

input = [3,6,2,9,9,4]
output = 33

#def add(arr, sum)
# output += arr[0]
# output += function(arr[1]

def addRecursively(arr, sum):
    if (len(arr) == 1):
        return sum + arr[0]
    sum += arr[0]
    sum += (addRecursively(arr[1:], sum) - sum)
    return sum

#print(addRecursively(input, 0))

# Given a n x m binary matrix image, flip the image horizontally, then invert it, then return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0, 1, 1] results in [1, 0, 0].
# Examples:

input =  [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
# After H Flip = [[0,1,1], [1,0,1], [0,0,0]]
# Output = [[1, 0, 0,], [0, 1, 0], [1, 1, 1]]
# Explanation:
# First reverse each row: [[0, 1, 1], [1, 0, 1], [0, 0, 0]]
# Then invert the image: [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

def imageConversion(arr):
    holder = []
    miniHolder = []
    returnable = []
    
    for index, array in enumerate(arr):
        holder += list(reversed(array))

    for index, element in enumerate(holder):
        miniHolder.append(1-element)
        if len(miniHolder) == 3:
            returnable.append(miniHolder)
            miniHolder = []
    
    return returnable

print(imageConversion(input))