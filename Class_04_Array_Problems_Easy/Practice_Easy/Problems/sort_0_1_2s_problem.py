# Write a function that sorts 0s, 1s, and 2s

input_array = [0, 1, 2, 0, 2, 2, 1, 1, 0]
# Output = [0, 0, 0, 1, 1, 1, 2, 2, 2]

def sort(arr):
    zero = []
    one = []
    two = []
    for i in arr:
        if i == 0:
            zero.append(i)
        elif i==1:
            one.append(i)
        elif i==2:
            two.append(i)
    
    complete = zero + one + two
    return complete

print(sort(input_array))