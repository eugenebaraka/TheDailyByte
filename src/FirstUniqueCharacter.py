# This question is asked by Microsoft. Given a string, return the index of its 
# first unique character. If a unique character does not exist, return -1.

# Ex: Given the following strings...

# "abcabd", return 2
# "thedailybyte", return 1
# "developer", return 0

def first_unique_char(s:str) -> int:
    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    uniquechars = {k:v for k,v in counts.items() if v == 1}

    if len(uniquechars) > 0:
        firstchar = next(iter(uniquechars.keys()))
        return s.index(firstchar)
    
    return -1

# Tests
print(first_unique_char("abcabd"))
print(first_unique_char("thedailybyte"))
print(first_unique_char("developer"))