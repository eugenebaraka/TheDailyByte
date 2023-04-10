# This question is asked by Amazon. Given a string representing your stones and another string representing a 
# list of jewels, return the number of stones that you have that are also jewels.

# Ex: Given the following jewels and stones...

# jewels = "abc", stones = "ac", return 2
# jewels = "Af", stones = "AaaddfFf", return 3
# jewels = "AYOPD", stones = "ayopd", return 0


def jewels_and_stones(jewels:str, stones:str) -> int:
    return len([s for s in stones if s in jewels])

# Tests
print(jewels_and_stones(jewels="abc", stones="ac"))
print(jewels_and_stones(jewels="Af", stones="AaaddfFf"))
print(jewels_and_stones(jewels="AYOPD", stones="ayopd"))