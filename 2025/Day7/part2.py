class Emitter:
    def __init__(self, i, j):
        self.row = i
        self.column = j
        self.loc = [self.row, self.column]
    
    def emit(self, grid):
        grid[self.row+1][self.column] = '1'

def ray_spread(grid, row, col, value):
    if grid[row+1][col].isnumeric():
        grid[row+1][col] = str(int(grid[row+1][col])+value)
    elif grid[row+1][col] == '^':
        grid[row+1][col-1] = str(int(grid[row+1][col-1])+value)
        grid[row+1][col+1] = str(int(grid[row+1][col+1])+value)
    else:
        print("AHHHHHHHHH!!")
    return 0


with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    grid = file.read()
grid = grid.replace('.', '0')
grid = grid.split("\n")
grid = [list(row) for row in grid]


#get loc of emitter
my_emitter = Emitter(0, grid[0].index('S'))
my_emitter.emit(grid)

#idea here is to count the amount of "timelines" at each point
for row in range(1, len(grid)-1):
    for col in range(len(grid[0])):
        if grid[row][col] == '^':
            continue
        value = int(grid[row][col])
        if value > 0:
            ray_spread(grid, row, col, value)

#sum the final row
total = 0
for i in grid[-1]:
    total += int(i)
print(total)