def digitOne(battery):
    for i in range(9,0,-1):
        for j in range(len(battery[:-1])):
            if i == int(battery[j]):
                return (i,j)
    return (0,0)

def digitTwo(battery, digit_1_index):
    for i in range(9,0,-1):
        for j in range(digit_1_index+1, len(battery)):
            if i == int(battery[j]):
                return i
    return 0

with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    batt_list = file.read()
batt_list = batt_list.split("\n")

total = 0
for battery in batt_list:
    digit_1, digit_1_index = digitOne(battery)
    digit_2 = digitTwo(battery, digit_1_index)
    print(f"{battery}:\t{digit_1}{digit_2}")
    total += digit_1 * 10 + digit_2
print(total)
    
            

