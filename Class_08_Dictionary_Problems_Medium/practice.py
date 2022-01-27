arr = [2,7,11,15] #[0,1,2,3]
targ = 9
arr2 = [3,-5,7,10]
targ2 = 2

def twoSum(arr, targ):
    dict = {}
    for index, num in enumerate(arr):
        dict[num] = index 
    for element in dict:
        if ((targ-element) in dict):
            return dict[element], dict[targ-element]

print(twoSum(arr, targ))
print(twoSum(arr2, targ2))

# {2:0, 7:1, 11:2, 15:3}