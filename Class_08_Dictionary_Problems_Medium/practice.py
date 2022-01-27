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

# print(twoSum(arr, targ))
# print(twoSum(arr2, targ2))

# {2:0, 7:1, 11:2, 15:3}

sentence1 = "this apple is sweet"
sentence2 = "this apple is sour"

def uncommonWords(sen, sen2):
    freq = {}
    output = []
    sen = sen.split(" ") + sen2.split(" ")
    for element in sen: #9
        if element in freq:
            freq[element] +=1
        else:
            freq[element] = 1
    for element in freq:
        if freq[element] == 1:
            output.append(element)

    return(output)

print(uncommonWords(sentence1, sentence2))

# O(length of array 1 + length of array 2)
# O(length of combined array)