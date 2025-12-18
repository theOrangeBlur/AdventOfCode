TOTAL_LENGTH = 12

def getDigitOne(battery):
    for i in range(9,0,-1):
        for j in range(len(battery[:-1*TOTAL_LENGTH])+1):
            if i == int(battery[j]):
                return (i,j)
    return (0,0)

def getNextDigit(battery, previous_index, digit):
    for i in range(9,0,-1):
        for j in range(previous_index+1, len(battery[:-1*(TOTAL_LENGTH - digit)])+1):
            if i == int(battery[j]):
                return (i,j)
    return (0,0)

with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    batt_list = file.read()
batt_list = batt_list.split("\n")

total = 0
for battery in batt_list:
    digit_1, digit_1_index = getDigitOne(battery)
    batt_jolt = str(digit_1)
    for i in range(1,12):
        digit_2, digit_2_index= getNextDigit(battery, digit_1_index, i)
        batt_jolt += str(digit_2)
        digit_1_index = digit_2_index
    print(f"{battery}:\t{batt_jolt}")
    total += int(batt_jolt)
print(total)
    
            

