import numpy as np

def main():
    num_trees = 0
    input_file = open('input_problem3.txt').read().replace('\n', '')
    number_grabber = open('input_problem3.txt').read().splitlines()
    width, height = len(number_grabber[0]), len(number_grabber)
    print(width, height)
    array1 = [x for x in input_file]
    array1 = np.array(array1)
    array1 = array1.reshape(height, width)
    print(array1)
    list_position = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    list_trees = []
    for position in list_position:
        current_pos = [0, 0]
        num_trees = 0
        while current_pos[0] < height:
            if array1[current_pos[0] % height, current_pos[1] % width] == "#":
                num_trees += 1
            current_pos[0] += position[0]
            current_pos[1] += position[1]
        list_trees.append(num_trees)
    print(list_trees)
    final = 1
    for tree in list_trees:
        final *= tree
    print(final)



main()