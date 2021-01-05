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
    position = [1, 3]
    while position[0] < height:
        if array1[position[0] % height, position[1] % width] == "#":
            num_trees += 1
        position[0] += 1
        position[1] += 3
        print(position)
    print(num_trees)


main()