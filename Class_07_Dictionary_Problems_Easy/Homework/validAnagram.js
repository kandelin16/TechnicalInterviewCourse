/**
 * Given two strings s and t, return true if t is an anagram of s, and false otherwise. Use a dictionary.
 * 
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
 * typically using all the original letters exactly once.
 * 
 * Input: s = "anagram", t = "nagaram"
 * Output: true
 * 
 * Input: s = "rat", t = "car"
 * Output: false
 * 
 * Source: https://leetcode.com/problems/valid-anagram/
 */

const s = 'anagram'
const t = 'nagaram'

function anagram(str1, str2) {
    if (str1.length != str2.length) {
        return false
    }
    dict1 = {}
    dict2 = {}
    for (i=0; i < str1.length; i++) {
        if (dict1.hasOwnProperty(str1[i])) {
            dict1[str1[i]] ++
        }
        else {
            dict1[str1[i]] = 1
        }
    }
    for (i=0; i < str2.length; i++) {
        if (dict2.hasOwnProperty(str2[i])) {
            dict2[str2[i]] ++
        }
        else {
            dict2[str2[i]] = 1
        }
    }
    for (i=0; i < str1.length; i++) {
        if (dict1[str1[i]] != dict2[str1[i]]) {
            return false
        }
    }
    return true
}

console.log(anagram(s, t))