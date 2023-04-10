# This question is asked by Amazon. Given a string representing your stones and another string representing a 
# list of jewels, return the number of stones that you have that are also jewels.

# Ex: Given the following jewels and stones...

# jewels = "abc", stones = "ac", return 2
# jewels = "Af", stones = "AaaddfFf", return 3
# jewels = "AYOPD", stones = "ayopd", return 0


def jewels_and_stones(jewels:str, stones:str) -> int:
    return len([s for s in stones if s in jewels])

# Time complexity O(n)
# Space complexity O(n)

def jewels_and_stones(jewels: str, stones: str) -> int:
    # create unique jewels, membership testing in a set is faster than searching a string (O(1))
    jewel_set = set(jewels) 
    return sum(1 for stone in stones if stone in jewel_set)

# Time complexity: also O(n) -- still have to examine each character in stones
# Space complexity O(n) # set created


# Tests
print(jewels_and_stones(jewels="abc", stones="ac"))
print(jewels_and_stones(jewels="Af", stones="AaaddfFf"))
print(jewels_and_stones(jewels="AYOPD", stones="ayopd"))