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

tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
  ("suraj", 20), ("akhil", 25), ("ashish", 30)]

def tupToDict(tups):
    out = {tup[0]:tup[1] for tup in tups}
    return out

print(tupToDict(tups))

test_dict = {'B' : 4, 'Y' : 2, 'U' : 5}

def dictReverse(d1):
    d2 = {key:value for key, value in reversed(d1.items())}
    return d2

print(dictReverse(test_dict))

test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}

def subDictSort(d):
    output = {}
    min = 0
    for subDict in d:
        d[subDict] = {key:value for key, value in sorted(d[subDict].items(), key=lambda item: item[1], reverse=True)}
    return d

print(subDictSort(test_dict))