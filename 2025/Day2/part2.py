def patternCheck(my_int):
    int_str = str(my_int)
    for i in range(round(len(int_str)/2)):
        pattern = int_str[:i+1]
        times_repeated = int_str.count(pattern)
        if times_repeated*len(pattern) == len(int_str):
            print(f"{my_int} is a repeat of {pattern}")
            return True
    return False


with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    ID_list = file.read()
    ID_list = ID_list.split(",")

total = 0
for ID_range in ID_list:
    start_point,end_point = ID_range.split("-")
    for i in range(int(start_point),int(end_point)+1):
        if patternCheck(i):
            total += i
print(total)