# This question is asked by Microsoft. Given an array of strings, 
# return the longest common prefix that is shared amongst all strings.
# Note: you may assume all strings only contain lowercase alphabetical characters.

# Ex: Given the following arrays...

# ["colorado", "color", "cold"], return "col"
# ["a", "b", "c"], return ""
# ["spot", "spotty", "spotted"], return "spot"

def longest_common_prefix(l:list):

    # initialize empty string to store prefix
    prefix = ""

    for char in zip(*l):
        if len(set(char)) == 1:
            prefix += char[0]
        else:
            break

    return prefix


# Tests
print(longest_common_prefix(l=["colorado", "color", "cold"]))
print(longest_common_prefix(l=["a", "b", "c"]))
print(longest_common_prefix(l=["spot", "spotty", "spotted"]))
