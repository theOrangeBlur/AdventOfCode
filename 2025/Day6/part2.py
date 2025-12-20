def addFunc(input):
    sum = 0
    for num in input:
        sum += int(num)
    return sum

def multiplyFunc(input):
    sum = 1
    for num in input:
        sum *= int(num)
    return sum

with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    input = file.read()
input = input.split("\n")

total = 0
operand_list = []
j = len(input[0])-1
while j > -1: #once for each column, right to left
    operand = ''
    func_bool = False
    for i in range(len(input)): #once for each row, counting down
        if input[i][j] == ' ':
            continue
        if input[i][j].isdigit(): #if it's a number, concat it to the operand
            operand += input[i][j]
            continue
        operator = input[i][j]
        func_bool = True
    operand_list.append(operand)
    

    if func_bool:
        if operator == '+':
            total += addFunc(operand_list)
        elif operator == '*':
            total += multiplyFunc(operand_list)
        else:
            print("Bad function")
        operand_list = []
        j -= 1
    j -= 1
print(total)