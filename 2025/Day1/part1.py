with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    directions = file.read()
    directions = directions.split("\n")

loc = 50
total = 0
for direction in directions:
    if direction[0] == 'R':
        loc += int(direction[1:])
        while loc > 99:
            loc-=100
    else:
        loc -= int(direction[1:])
        while loc < 0:
            loc+=100

    if loc == 0:
        total+=1
print(total)