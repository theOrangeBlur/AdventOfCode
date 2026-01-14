#this method is flawed, it will take much too long. Part 2 not complete :(

import numpy as np

def get_area(x1, x2, y1, y2):
    return( (abs(x1-x2)+1) * (abs(y1-y2)+1) )

def fillGridRow(grid, col1, col2, row):
    for i in range(col2+1, col1):
        grid[row][i] = 2

def fillGridCol(grid, row1, row2, col):
    for i in range(row2+1, row1):
        grid[i][col] = 2

def valid_check(grid, tile1, tile2):
    start_row = min(tile1[1], tile2[1])
    end_row = max(tile1[1], tile2[1])
    start_col = min(tile1[0], tile2[0])
    end_col = max(tile1[0], tile2[0])
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):
            if grid[row][col] == 0:
                #print(f"{tile1} to {tile2} is invalid.")
                return False
    #print(f"{tile1} to {tile2} is valid.")
    return True


def search_for_biggest_square(tile_list):
    biggest_area_list = [0, 0, 0] #value, xpos, ypos
    for i in range(len(tile_list)):
        print(f"{i}")
        for j in range(i+1, len(tile_list)):
            valid_bool = valid_check(grid, tile_list[i], tile_list[j])
            my_area = 0
            if valid_bool:
                my_area = get_area(tile_list[i][0], tile_list[j][0], tile_list[i][1], tile_list[j][1])
                #print(f"It has an area of {my_area}.")
            if my_area > biggest_area_list[0]:
                biggest_area_list = [my_area, i, j]
    return(biggest_area_list)

with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    tile_list = file.read()
tile_list = tile_list.split("\n")
tile_list = [row.split(",") for row in tile_list]
tile_list = [[int(row[0]), int(row[1])]for row in tile_list]
tile_array = np.array(tile_list)
grid = np.full(shape=(tile_array[:, 1].max()+1, tile_array[:, 0].max()+1), fill_value=0, dtype=np.uint8)

for tile_loc in tile_array:
    grid[tile_loc[1]][tile_loc[0]] = 1

#make borders
for i in range(-1, len(tile_array)-1):
    row1 = tile_array[i][0]
    row2 = tile_array[i+1][0]
    col1 = tile_array[i][1]
    col2 = tile_array[i+1][1]
    if row1 == row2:
        fillGridCol(grid, max(col1,col2), min(col1,col2), row1)
    elif col1 == col2:
        fillGridRow(grid, max(row1,row2), min(row1,row2), col1)
    else:
        print("AHHHH")

#fill in shape
for row in range(len(grid)):
    for col in range(1, len(grid[0])):
        if grid[row][col] != 0:
            continue
        if grid[row][col-1] == 0:
            continue
        else: grid[row][col] = 3

print("Red + Green generated.")


biggest_area_list = search_for_biggest_square(tile_list)
print(f"biggest square is made by squares at indeces {biggest_area_list[1]} and {biggest_area_list[2]}. It is {biggest_area_list[0]} large.")

