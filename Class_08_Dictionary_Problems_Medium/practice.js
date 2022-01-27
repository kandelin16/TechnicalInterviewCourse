// given an array of size n, return the majority element

input = [3,2,3] // returns 3
input2 = [2,2,2,1,1,2] // returns 2

function majorityElement(arr) {
    output = {}
    for (num of arr) {
        if (num in output) {
            output[num] ++
        } else {
            output[num] = 1
        }
    }
    for (num of arr) {
        if ((Math.floor(output[num])) >= (Math.floor(arr.length / 2))) {
            return num
        }
    }
}

console.log(majorityElement(input))
console.log(majorityElement(input2))