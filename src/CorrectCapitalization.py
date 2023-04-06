# This question is asked by Google. Given a string, return whether or 
# not it uses capitalization correctly. A string correctly uses 
# capitalization if all letters are capitalized, no letters are 
# capitalized, or only the first letter is capitalized.

# Ex: Given the following strings...

# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true


def correct_capitalization(s:str) -> bool:
    return s[0].isupper() or s.islower()

# Tests
print(correct_capitalization("USA"))
print(correct_capitalization("Calvin"))
print(correct_capitalization("compUter"))
print(correct_capitalization("coding"))


