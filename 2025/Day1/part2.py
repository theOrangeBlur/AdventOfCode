with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    directions = file.read()
    directions = directions.split("\n")

loc = 50
total = 0
for direction in directions:
    if direction[0] == "R":
        iterator = 1
    else:
        iterator = -1
    spaces_list = [loc]
    for i in range(int(direction[1:])):
        new_loc = loc + iterator
        if new_loc == 100:
            new_loc = 0
        if new_loc == -1:
            new_loc = 99
        spaces_list.append(new_loc)
        loc = new_loc
    total += spaces_list[1:].count(0)
print(total)