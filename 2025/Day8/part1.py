import math

CONNECTION_NUM = 1000
BIG_NUMBER = 10000.

class JunctionBox:
    def __init__(self, x, y, z):
        self.x_pos = int(x)
        self.y_pos = int(y)
        self.z_pos = int(z)
        self.connected = False

    def distance(self, box2):
        return math.sqrt( (self.x_pos - box2.x_pos)**2 + (self.y_pos - box2.y_pos)**2 + (self.z_pos - box2.z_pos)**2)

    def distance_list_gen(self, junction_box_list):
        self.distance_list = []
        for other_box in junction_box_list:
            self.distance_list.append(self.distance(other_box))


with open("C:/Users/eckma/OneDrive/Documents/AdventOfCodeOuter/input.txt", "r") as file:
    grid = file.read()
grid = grid.split("\n")
grid = [row.split(",") for row in grid]

junction_box_list = []
for jbox in grid:
    my_box = JunctionBox(jbox[0], jbox[1], jbox[2])
    junction_box_list.append(my_box)

#connect CONNECTION_NUM boxes
distance_grid = []
for box in junction_box_list:
    box.distance_list_gen(junction_box_list)
    distance_grid.append(box.distance_list)

connection_list = []
while len(connection_list) < CONNECTION_NUM:
    next_closest_distance = [BIG_NUMBER, 0, 0]
    for i in range(len(distance_grid)):
        for j in range(len(distance_grid[i])):
            if distance_grid[i][j] < next_closest_distance[0] and distance_grid[i][j] > 0 and [distance_grid[i][j], i, j] not in connection_list and [distance_grid[i][j], j, i] not in connection_list:
                next_closest_distance = [distance_grid[i][j], i, j]
    connection_list.append(next_closest_distance)
    if next_closest_distance[0] == BIG_NUMBER:
        print("AHHHHHHHHHHHHH! BIG NUMBER ISN'T BIG ENOUGH")
    print(f"{len(connection_list)}/{CONNECTION_NUM}")

#investigate the circuits
circuit_list = [[connection_list[0][1],connection_list[0][2]]]
num_circuits = 1
for connection in connection_list:
    box1_match = [False, 0, 0]
    box2_match = [False, 0, 0]
    for i in range(len(circuit_list)):
        for j in range(len(circuit_list[i])):
            if connection[1] == circuit_list[i][j]:
                box1_match = [True, i, j]
            if connection[2] == circuit_list[i][j]:
                box2_match = [True, i, j]
    if box1_match[0] and box2_match[0]:
        if box1_match[1] == box2_match[1]:
            continue
        else:
            circuit_list[box1_match[1]] += circuit_list[box2_match[1]]
            circuit_list[box2_match[1]] = ''
            continue
    if box1_match[0]:
        circuit_list[box1_match[1]].append(connection[2])
        continue
    if box2_match[0]:
        circuit_list[box2_match[1]].append(connection[1])
        continue
    circuit_list.append([connection[1], connection[2]])

#get the three largest
biggest_list = []
for row in circuit_list:
    biggest_list.append(len(row))
biggest_list.sort(reverse=True)
total = 1
for i in range(3):
    total *= biggest_list[i]
print(total)