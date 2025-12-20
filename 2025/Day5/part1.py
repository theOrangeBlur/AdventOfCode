def rangeCheck(range_list, ID):
    for my_range in range_list:
        my_range = my_range.split('-')
        if int(my_range[0]) <= int(ID) <= int(my_range[1]):
            print(f"{my_range[0]} <= {ID} <= {my_range[1]}")
            return True
    return False

with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    input = file.read()
input = input.split("\n")
range_list = [input[0]]
for i in range(1,len(input[1:])):
    if input[i].find('-') == -1:
        end_index = i
        break
    range_list.append(input[i])
ID_list = [input[end_index+1]]
for i in range(end_index+2, len(input)):
    ID_list.append(input[i])
print("done")
total = 0
for ID in ID_list:
    fresh_bool = rangeCheck(range_list, ID)
    if fresh_bool:
        total += 1
print(total)
    