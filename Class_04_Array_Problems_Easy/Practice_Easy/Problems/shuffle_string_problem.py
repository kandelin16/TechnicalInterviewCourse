# You are given a string s and an integer array indices of the same length. 
# The string s will be shuffled such that the character at the ith position 
# moves to indices[i] in the shuffled string. Return the shuffled string.

# Input: s = "codeleet", indices = [4,5,6,7,0,1,2,3]
# Output: "leetcode"

input_string = "ttbdisschoeee"
indices = [7, 9, 3, 10, 4, 5, 0, 8, 11, 2, 12, 6, 1]

def shuffle(string, ind):
    new = ""
    for i in ind:
        new += input_string[i]
    return new

print(shuffle(input_string, indices))