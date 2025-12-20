import re

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

#clean up input
for i in range(len(input)): #I need to review list comprehension
    input[i] = re.findall("(\S+)", input[i])

total = 0
for i in range(len(input[0])): #for this many columns
    problem_list = []
    for j in range(len(input)):
        problem_list.append(input[j][i])
    if problem_list[-1] == '+':
        total += addFunc(problem_list[:-1:])
    else:
        total += multiplyFunc(problem_list[:-1:])
print(total)