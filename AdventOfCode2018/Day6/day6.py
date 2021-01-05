import numpy as np
import numpy
import collections
import operator

def turning_test_into_int():
    turn_matrix = []
    str1 = "aaaaa.ccccaAaaa.ccccaaaddeccccaadddeccCc..dDdeecccbb.deEeeccbBb.eeee..bbb.eeefffbbb.eeffffbbb.ffffFf"
    for char in str1:
        if char.lower() == "a":
            num = 1
        elif char.lower() == "b":
            num = 2
        elif char.lower() == "c":
            num = 3
        elif char.lower() == "d":
            num = 4
        elif char.lower() == "e":
            num = 5
        elif char.lower() == "f":
            num = 6
        else:
            num = 0
        turn_matrix.append(num)
    for index, number in enumerate(turn_matrix):
        if (index + 1) % 10 == 0:
            print(turn_matrix[index - 9: index + 1])
    

def part1():
    #creates list of all the cordinates
    temp_advent_list = open("day6.txt").read().splitlines()
    #matrix of just zeros
    zero_matrix = numpy.zeros(shape = (400, 400))
    #putting in cordiantes form advent_list into zero_matrix
    counter = 1
    advent_list = []
    objects_to_delete = []
    for cordinate in temp_advent_list:
        x = int(cordinate.split(",")[0])
        y = int(cordinate.split(" ")[1])
        advent_list.append((x, y))
g        zero_matrix[y, x] = int(counter)
        counter += 1
    repeat_key_list = []
    dict_count_of_nums = {}
    for num in range(len(advent_list)):
        dict_count_of_nums[num + 1] = 0
        
    for index, number in np.ndenumerate(zero_matrix):
        if number == 0:
            difference_dict = {}
            for second_cord in advent_list:
                a = (abs(int(second_cord[0]) - int(index[1])) + abs(int(second_cord[1]) - int(index[0])))
                if a in difference_dict:
                    repeat_key_list.append(a)
                if a != 0:
                    difference_dict[a] = advent_list.index(second_cord) + 1
            if min(difference_dict) in repeat_key_list:
                zero_matrix[index[0], index[1]] = 0
            else:
                zero_matrix[index[0], index[1]] = difference_dict[min(difference_dict)]
            repeat_key_list = []
            
        #have to change the vals for the real matrix
        if index[0] == 0 or index[1] == 0 or index[0] == 399 or index[1] == 399:
            objects_to_delete.append(zero_matrix[index[0], index[1]])
        print(index)
    
    unique, counts = numpy.unique(zero_matrix, return_counts=True)
    dict_count_of_nums = dict(zip(unique, counts))
    objects_to_delete.append(0)
    objects_to_delete = set(objects_to_delete)
    for object1 in objects_to_delete:
        del dict_count_of_nums[object1]

    #printing
    print(dict_count_of_nums[max(dict_count_of_nums.items(), key = operator.itemgetter(1))[0]])
    print(dict_count_of_nums)


def part2():
    #creates list of all the cordinates
    temp_advent_list = open("day6.txt").read().splitlines()
    #matrix of just zeros
    zero_matrix = numpy.zeros(shape = (400, 400))
    #putting in cordiantes form advent_list into zero_matrix
    counter = 1
    advent_list = []
    for cordinate in temp_advent_list:
        x = int(cordinate.split(",")[0])
        y = int(cordinate.split(" ")[1])
        advent_list.append((x, y))
        zero_matrix[y, x] = int(counter)
        counter += 1
    print(advent_list)
    size = 0
    for index, number in np.ndenumerate(zero_matrix):
        difference_sum = 0
        for second_cord in advent_list:
            difference_sum += (abs(int(second_cord[0]) - int(index[1])) + abs(int(second_cord[1]) - int(index[0])))
        if difference_sum < 10000:
            size += 1
        print(index)
    print(size)
part2()
