# This question is asked by Facebook. Given a string and the ability to delete at most one character, 
# return whether or not it can form a palindrome.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

# Ex: Given the following strings...

# "abcba", return true
# "foobof", return true (remove the first 'o', the second 'o', or 'b')
# "abccab", return false

def valid_palindrome_with_removal(s: str) -> bool:
    # use two pointers
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            without_left = s[:left] + s[left+1:]
            without_right = s[:right] + s[right+1:]
            return without_left == without_left[::-1] or without_right == without_right[::-1]
        left += 1
        right -= 1

    return True


# Tests
print(valid_palindrome_with_removal(s="abcba"))
print(valid_palindrome_with_removal(s="foobof"))
print(valid_palindrome_with_removal(s="abccab"))
        

        

