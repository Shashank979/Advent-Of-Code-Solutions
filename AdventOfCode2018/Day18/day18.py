import numpy as np
import numpy

def part1():
    temp_advent_list = open("day18.txt").read().splitlines()
    string_counter = 0
    original_matrix = np.empty([50, 50], dtype = str)
    new_matrix = np.empty([50, 50], dtype = str)
    #empty_matrix = np.empty([10, 10], dtype = str)
    #creation of the original matrix
    for string1 in temp_advent_list:
        char_counter = 0
        for char in string1:
            original_matrix[string_counter][char_counter] = char
            char_counter += 1
        string_counter += 1
    
    for num in range(1000):
        if num != 0:
            original_matrix = new_matrix.copy()
        for index, object1 in np.ndenumerate(original_matrix):
            list_of_objects = []
            #right
            if index[1] <= 48:
                list_of_objects.append(original_matrix[index[0]][index[1] + 1])
            #left
            if index[1] >= 1:
                list_of_objects.append(original_matrix[index[0], index[1] - 1])
            #forward
            if index[0] <= 48:
                list_of_objects.append(original_matrix[index[0] + 1, index[1]])
            #back
            if index[0] >= 1:
                list_of_objects.append(original_matrix[index[0] - 1, index[1]])
                
            #right forward
            if index[0] <= 48 and index[1] <= 48:
                list_of_objects.append(original_matrix[index[0] + 1, index[1] + 1])
            #right back
            if index[0] >= 1 and index[1] <= 48:
                list_of_objects.append(original_matrix[index[0] - 1, index[1] + 1])
            #left forward
            if index[0] <= 48 and index[1] >= 1:
                list_of_objects.append(original_matrix[index[0] + 1, index[1] - 1])
            #left back
            if index[0] >= 1 and index[1] >= 1:
                list_of_objects.append(original_matrix[index[0] - 1, index[1] - 1])

            #counting
            if object1 == ".":
                if list_of_objects.count("|") >= 3:
                    new_matrix[index[0]][index[1]] = "|"
                else:
                    new_matrix[index[0]][index[1]] = "."
            elif object1 == "|":
                if list_of_objects.count("#") >= 3:
                    new_matrix[index[0]][index[1]] = "#"
                else:
                    new_matrix[index[0]][index[1]] = "|"
            else:
                if list_of_objects.count("#") == 0 or list_of_objects.count("|") == 0:
                    new_matrix[index[0]][index[1]] = "."
                else:
                    new_matrix[index[0]][index[1]] = "#"
        print(num)
    #getting final val
    unique, counts = numpy.unique(new_matrix, return_counts=True)
    dict_of_objects = dict(zip(unique, counts))
    print(dict_of_objects["#"] * dict_of_objects["|"])
    
part1()
