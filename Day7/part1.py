class Emitter:
    def __init__(self, i, j):
        self.row = i
        self.column = j
        self.loc = [self.row, self.column]
    
    def emit(self, grid):
        if grid[self.row+1][self.column] == '.':
            grid[self.row+1][self.column] = '|'
        elif grid[self.row+1][self.column] == '^':
            grid[self.row+1][self.column-1] = '|'
            grid[self.row+1][self.column+1] = '|'

def ray_spread(grid, row, col):
    if grid[row+1][col] == '.':
        grid[row+1][col] = '|'
    elif grid[row+1][col] == '^':
        grid[row+1][col-1] = '|'
        grid[row+1][col+1] = '|'
        return 1
    return 0


with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    grid = file.read()
grid = grid.split("\n")
grid = [list(row) for row in grid]

#get loc of emitter
my_emitter = Emitter(0, grid[0].index('S'))
my_emitter.emit(grid)

total = 0
for row in range(len(grid)-1):
    for col in range(len(grid[0])):
        if grid[row][col] == '|':
            total += ray_spread(grid, row, col)

print(total)