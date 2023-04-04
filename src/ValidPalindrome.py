# This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

# Ex: Given the following strings...

# "level", return true
# "algorithm", return false
# "A man, a plan, a canal: Panama.", return true

def valid_palindrome(mystring:str) -> str:
    # remove non-alpha numerics
    my_string = "".join(e for e in mystring if e.isalnum())
    # lower case
    my_string = my_string.lower()
    return my_string == my_string[::-1]

# Tests
print(valid_palindrome("level"))
print(valid_palindrome("algorithm"))
print(valid_palindrome("A man, a plan, a canal: Panama."))