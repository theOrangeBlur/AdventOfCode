def get_area(x1, x2, y1, y2):
    return( (abs(x1-x2)+1) * (abs(y1-y2)+1) )

with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    tile_list = file.read()
tile_list = tile_list.split("\n")

tile_list = [row.split(",") for row in tile_list]
tile_list = [[int(row[0]), int(row[1])]for row in tile_list]
biggest_area_list = [0, 0, 0] #value, xpos, ypos
for i in range(len(tile_list)):
    for j in range(i+1, len(tile_list)):
        my_area = get_area(tile_list[i][0], tile_list[j][0], tile_list[i][1], tile_list[j][1])
        if my_area > biggest_area_list[0]:
            biggest_area_list = [my_area, i, j]
print(f"biggest square is made by squares at indeces {biggest_area_list[1]} and {biggest_area_list[2]}. It is {biggest_area_list[0]} large.")

