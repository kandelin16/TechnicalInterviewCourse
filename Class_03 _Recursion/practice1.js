function palindrome(string) {
    if (string[0] == string[string.length - 1]) {
        palindrome(string.substring(1, string.length - 2))
    }
    else {
        return false
    }
    return true
}

console.log(palindrome("racecar"))
console.log(palindrome("hello"))