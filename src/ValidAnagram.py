# This question is asked by Facebook. Given two strings s and t return 
# whether or not s is an anagram of t.
# Note: An anagram is a word formed by reordering the letters of another word.

# Ex: Given the following strings...

# s = "cat", t = "tac", return true
# s = "listen", t = "silent", return true
# s = "program", t = "function", return false


def valid_anagram(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    chars_s = {}
    chars_t = {}

    for char in s:
        chars_s[char] = chars_s.get(char, 0) + 1

    for char in t:
        chars_t[char] = chars_t.get(char, 0) + 1

    return chars_s == chars_t
   




# Tests
print(valid_anagram(s = "cat", t = "tac"))
print(valid_anagram(s = "listen", t = "silent"))
print(valid_anagram(s = "program", t = "function"))