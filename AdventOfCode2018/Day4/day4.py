import time
import operator
from collections import Counter

#guard with most minutes is 1901
def part1():
    with open('day4.txt') as f:
        advent_list = [line.strip() for line in f.readlines()]
    advent_list.sort()
    dict_of_guards = {}
    guard_num = 0
    start_time = 0
    end_time = 0
    for timestamp in advent_list:
        if timestamp[19] == "G":
            guard_num = timestamp.split(" ")[3]
        elif timestamp[19] == "f":
            start_time = timestamp[12:14] + timestamp[15:17]
        elif timestamp[19] == "w":
            end_time = timestamp[12:14] + timestamp[15:17]
            difference_hours = int(end_time[0:2]) - int(start_time[0:2])
            difference_hours_conv = difference_hours * 60
            difference_minutes = int(end_time[2:4]) - int(start_time[2:4])
            if guard_num in dict_of_guards:
                dict_of_guards[guard_num] += difference_minutes + difference_hours_conv
            else:
                dict_of_guards[guard_num] = difference_minutes + difference_hours_conv
    
    print(max(dict_of_guards.items(), key = operator.itemgetter(1))[0])

def part1cont():
    with open('day4.txt') as f:
        advent_list = [line.strip() for line in f.readlines()]
    advent_list.sort()
    dict_of_guards = {}
    guard_num = 0
    start_time = 0
    end_time = 0
    minutes_dict = {}
    for num in range(0, 60):
        minutes_dict[num] = 0
    wrong_guard = True
    for timestamp in advent_list:
        if timestamp[26:30] == "1901":
            wrong_guard = False
                
        elif timestamp[19] == "G" and timestamp[26:30] != "1901":
            wrong_guard = True
            
        if wrong_guard == False:
            if timestamp[19] == "f":
                start_time = timestamp[12:14] + timestamp[15:17]
            elif timestamp[19] == "w":
                end_time = timestamp[12:14] + timestamp[15:17]
                for minute in range(int(start_time[2:4]), int(end_time[2:4])):
                    minutes_dict[minute] += 1
    print(minutes_dict)
    print(max(minutes_dict.items(), key = operator.itemgetter(1))[0])

def part2():
    with open('day4.txt') as f:
        advent_list = [line.strip() for line in f.readlines()]
    advent_list.sort()
    dict_of_guards = {}
    guard_ID = 0
    start_time = 0
    end_time = 0
    
    for timestamp in advent_list:
        if timestamp[19] == "G":
            ID = timestamp.split(" ")[3]
            minutes_dict = {}
            for num in range(0, 60):
                minutes_dict[num] = 0
            dict_of_guards[ID] = minutes_dict
        
    for timestamp in advent_list:
        if timestamp[19] == "G":
            guard_ID = timestamp.split(" ")[3]
        if timestamp[19] == "f":
            start_time = timestamp[12:14] + timestamp[15:17]
        elif timestamp[19] == "w":
            end_time = timestamp[12:14] + timestamp[15:17]
            new_dict = Counter({})
            for num in range(0, 60):
                new_dict[num] = 0
            for minute in range(int(start_time[2:4]), int(end_time[2:4])):
                new_dict[minute] += 1
            values_to_change = Counter(dict_of_guards[guard_ID])
            values_put_back = values_to_change + new_dict
            dict_of_guards[guard_ID] = values_put_back
    
    for guard in dict_of_guards:
        value_of_guard = dict_of_guards[guard]
        max_value = max(value_of_guard.items(), key = operator.itemgetter(1))[0]
        number_of_max = value_of_guard.get(max_value)
        dict_of_guards[guard] = {max_value : number_of_max}
    print(dict_of_guards)
    
        
                
                
            
        
part2()
