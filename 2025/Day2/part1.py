def patternCheck(my_int):
    total = 0
    int_str = str(my_int)
    if len(int_str)%2:
        return 0
    pattern = int_str[:int(len(int_str)/2)]
    times_repeated = int_str.count(pattern)
    if times_repeated*len(pattern) == len(int_str):
        print(f"{my_int} is a repeat of {pattern}")
        total += my_int
    return total


with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    ID_list = file.read()
    ID_list = ID_list.split(",")

total = 0
for ID_range in ID_list:
    start_point,end_point = ID_range.split("-")
    for i in range(int(start_point),int(end_point)+1):
        total += patternCheck(i)
print(total)