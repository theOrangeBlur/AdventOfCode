with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    input = file.read()
input = input.split("\n")
range_list = [input[0]]
for i in range(1,len(input[1:])):
    if input[i].find('-') == -1:
        break
    range_list.append(input[i])


range_list.sort(key=lambda str: int(str.split('-')[0])) #sort the list by first number in range

new_range_list = [[0 for i in range(2)] for j in range(len(range_list))]
for i in range(len(range_list)):
    new_range_list[i][0] = int(range_list[i].split('-')[0])
    new_range_list[i][1] = int(range_list[i].split('-')[1])

for i in range(1, len(new_range_list)): #go through each item in the range_list. We only need to check the previous range.
    if new_range_list[i][0] > new_range_list[i-1][1]:
        continue
    new_range_list[i][0] = new_range_list[i-1][1] + 1
    if new_range_list[i][1] <= new_range_list[i-1][1]: #if the range is fully contained, get it to not count
        new_range_list[i][1] = new_range_list[i][0] - 1

total = 0
for i in range(len(new_range_list)):
    total += new_range_list[i][1] - new_range_list[i][0] + 1
print(total)