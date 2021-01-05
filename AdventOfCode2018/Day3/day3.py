import numpy as np
import numpy
def part1():
    with open('day3.txt') as f:
        advent_list = [line.strip() for line in f.readlines()]
    num_list = []
    zero_matrix = numpy.zeros(shape = (10000, 10000))
    overlaps = 0
    for fabric in advent_list:
        fabric2 = fabric.split("@")
        append_val = fabric2[1]
        num_list.append(append_val)
        
    for fabric3 in num_list:
        semi_colon_split = fabric3.split(":")
        #position
        position = semi_colon_split[0]
        comma_split = position.split(",")
        x = int(comma_split[0])
        y = int(comma_split[1])
        #size
        size = semi_colon_split[1]
        mult_split = size.split("x")
        width = int(mult_split[0])
        height = int(mult_split[1])
        zero_matrix[y : y + height, x : x + width] += 1
    overlaps = np.count_nonzero(zero_matrix > 1)    
    print(overlaps)

def part2():
    with open('day3.txt') as f:
        advent_list = [line.strip() for line in f.readlines()]
    id_list = []
    zero_matrix = numpy.zeros(shape = (10000, 10000))
    for fabric in advent_list:
        fabric2 = fabric.split("#")
        fabric_id = int(fabric2[1].split("@")[0])
        id_list.append(fabric_id)
    for fabric3 in advent_list:
        id_temp = fabric3.split("#")
        id_current_fab = int(id_temp[1].split("@")[0])
        fabric4 = fabric3.split("@")
        num_val = fabric4[1]
        semi_colon_split = num_val.split(":")
        #position
        position = semi_colon_split[0]
        comma_split = position.split(",")
        x = int(comma_split[0])
        y = int(comma_split[1])
        #size
        size = semi_colon_split[1]
        mult_split = size.split("x")
        width = int(mult_split[0])
        height = int(mult_split[1])
        for list1 in zero_matrix[y : y + height, x : x + width]:
            for place in list1:
                if place != 0:
                    try:
                        id_list.remove(place)
                    except ValueError:
                        pass
                    try:
                        id_list.remove(id_current_fab)
                    except ValueError:
                        pass
                    
        print(id_current_fab)
        zero_matrix[y : y + height, x : x + width] = id_current_fab
    print(id_list)

        
        
part2()
