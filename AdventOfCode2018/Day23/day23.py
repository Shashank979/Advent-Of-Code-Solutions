import numpy as np
import operator

#largest nanobot = pos=<66874149,45054384,46952893>, r=99487886
def part1():
    f = open('day23.txt', 'r+')
    nanobot_string = f.read()
    f.close()
    nanobot_list = nanobot_string.split('\n')
    radius_dict = {}
    nanobots_in_range = 0
    
    del nanobot_list[-1]
    for nanobot in nanobot_list:
        radius = nanobot.split("=")[2]
        radius_dict[nanobot] = radius
    largest_nanobot = max(radius_dict.items(), key=operator.itemgetter(1))[0]
    position_2 = largest_nanobot.split("<")[1].split(">")[0]
    x_2 = int(position_2.split(",")[0])
    y_2 = int(position_2.split(",")[1])
    z_2 = int(position_2.split(",")[2])
    radius_2 = int(radius_dict[max(radius_dict.items(), key = operator.itemgetter(1))[0]])
    print(largest_nanobot)
    print(x_2, y_2, z_2, radius_2)
    
    for nanobot2 in nanobot_list:
        position_1 = nanobot2.split("<")[1].split(">")[0]
        x_1 = int(position_1.split(",")[0])
        y_1 = int(position_1.split(",")[1])
        z_1 = int(position_1.split(",")[2])
        if (abs(x_2 - x_1) + abs(y_2 - y_1) + abs(z_2 - z_1)) <= radius_2:
            nanobots_in_range += 1
    print(nanobots_in_range)

def part2():
    

