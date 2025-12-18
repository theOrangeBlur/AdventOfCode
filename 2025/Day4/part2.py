TOO_MUCH_PAPER = 4

def check_Up_Left(diagram, row, col):
    if row == 0:
        return 0
    if col == 0:
        return 0
    if diagram[row-1][col-1] == '@':
        return 1
    return 0

def check_Up_Center(diagram, row, col):
    if row == 0:
        return 0
    if diagram[row-1][col] == '@':
        return 1
    return 0

def check_Up_Right(diagram, row, col):
    if row == 0:
        return 0
    if col == len(diagram[row])-1:
        return 0
    if diagram[row-1][col+1] == '@':
        return 1
    return 0

def check_Down_Left(diagram, row, col):
    if row == len(diagram)-1:
        return 0
    if col == 0:
        return 0
    if diagram[row+1][col-1] == '@':
        return 1
    return 0

def check_Down_Center(diagram, row, col):
    if row == len(diagram)-1:
        return 0
    if diagram[row+1][col] == '@':
        return 1
    return 0

def check_Down_Right(diagram, row, col):
    if row == len(diagram)-1:
        return 0
    if col == len(diagram[row])-1:
        return 0
    if diagram[row+1][col+1] == '@':
        return 1
    return 0

def check_Left(diagram, row, col):
    if col == 0:
        return 0
    if diagram[row][col-1] == '@':
        return 1
    return 0

def check_Right(diagram, row, col):
    if col == len(diagram[row])-1:
        return 0
    if diagram[row][col+1] == '@':
        return 1
    return 0

def check_Grid(diagram):
    change_bool = False
    total = 0
    for row in range(len(diagram)):
        for col in range(len(diagram[row])):
            if diagram[row][col] != '@':
                continue
            paper_count = 0
            paper_count += check_Up_Left(diagram, row, col)
            paper_count += check_Up_Center(diagram, row, col)
            paper_count += check_Up_Right(diagram, row, col)
            paper_count += check_Down_Left(diagram, row, col)
            paper_count += check_Down_Center(diagram, row, col)
            paper_count += check_Down_Right(diagram, row, col)
            paper_count += check_Left(diagram, row, col)
            paper_count += check_Right(diagram, row, col)
            if paper_count < TOO_MUCH_PAPER:
                total += 1
                newRow = list(diagram[row])
                newRow[col] = '.'
                diagram[row] = ''.join(newRow)
                change_bool = True
    return change_bool, total


with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    diagram = file.read()
#print(diagram)
diagram = diagram.split("\n")

total = 0
success = True
while success:
    success, sum = check_Grid(diagram)
    total += sum
print(total)
#for row in diagram:
#    print(row)