import numpy as np
import numpy

def part1():
    #722
    height = 723
    #11
    width = 12
    #first place is for height, second is for width
    zero_matrix = numpy.zeros(shape = (height, width))
    erosion_matrix = numpy.zeros(shape = (height, width))
    risk_matrix = numpy.zeros(shape = (height, width))
    #depth is 10689
    depth = 10689
    #index[0] is y, and index[1] is x coordinate
    for index, num in np.ndenumerate(zero_matrix):
        if index == (0, 0):
            geological_index = 0
        elif index[0] == 0 and index[1] != 0:
            geological_index = index[1] * 16807
        elif index[1] == 0 and index[0] != 0:
            geological_index = index[0] * 48271
        elif index[0] == (height - 1) and index[1] == (width - 1):
            geological_index = 0
        else:
            geological_index = erosion_matrix[index[0], index[1] - 1] * erosion_matrix[index[0] - 1, index[1]]
        erosion_level = (geological_index + depth) % 20183
        erosion_matrix[index] = erosion_level
        if erosion_level % 3 == 0:
            risk_matrix[index] = 0
        elif erosion_level % 3 == 1:
            risk_matrix[index] = 1
        else:
            risk_matrix[index] = 2
    print(risk_matrix)
    print(risk_matrix.sum())
part1()
