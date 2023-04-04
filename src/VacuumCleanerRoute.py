# This question is asked by Amazon. Given a string representing the sequence of moves a robot 
# vacuum makes, return whether or not it will return to its original position. The string will 
# only contain L, R, U, and D characters, representing left, right, up, and down respectively.

# Ex: Given the following strings...

# "LR", return true
# "URURD", return false
# "RUULLDRD", return true

def vcleaner_route(route:str) -> str:
    # let one step of the direction have a magnitude of 1
    # its opposive direction have the same magnitude but different "direction"

    magnitudes_directions = {"L":1, "R":-1, "U":1, "D":-1}
    string_conversion = [magnitudes_directions[key] for key in magnitudes_directions.keys() if key in route]
    
    return sum(string_conversion) == 0

# Tests

print(vcleaner_route("LR"))
print(vcleaner_route("URURD"))
print(vcleaner_route("RUULLDRD"))