# This question is asked by Google. Given an array of integers, return whether
# or not two numbers sum to a given target, k.
# Note: you may not sum a number with itself.

# Ex: Given the following...

# [1, 3, 8, 2], k = 10, return true (8 + 2)
# [3, 9, 13, 7], k = 8, return false
# [4, 2, 6, 5, 2], k = 4, return true (2 + 2)

def twoSum(arr:list, target:int) -> list:
    res = {}

    for i, num in enumerate(arr):
        complement = target - num

        if complement in res:
            return True
        res[num] = i
    return False

# Tests
print(twoSum(arr=[1, 3, 8, 2], target=10))
print(twoSum(arr=[3, 9, 13, 7], target=8))
print(twoSum(arr=[4, 2, 6, 5, 2], target=4))

