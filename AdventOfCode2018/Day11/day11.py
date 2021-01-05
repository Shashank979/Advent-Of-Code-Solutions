import numpy 
import numpy as np
def part1():
    size = 300
    zero_matrix = numpy.zeros(shape = (size, size))
    matrix_fuel_squares = numpy.zeros(shape = (size, size))
    serial_num = 7672
    #making matrix of power levels
    for index, number in np.ndenumerate(zero_matrix):
            
        rack_id = index[1] + 11
        power_level = rack_id * (index[0] + 1)
        power_level += serial_num
        power_level *= rack_id
        if power_level >= 100:
            power_level = int(str(power_level)[-3])
        else:
            power_level = 0
        power_level -= 5
        zero_matrix[index[0]][index[1]] = power_level
        
    for index, number in np.ndenumerate(zero_matrix):
        if index[1] >= (size - 2) or index[0] >= (size - 2):
            matrix_fuel_squares[index[0]][index[1]] = 0
        else:
            top_row = zero_matrix[index] + zero_matrix[index[0]][index[1] + 1] + zero_matrix[index[0]][index[1] + 2]
            middle_row = zero_matrix[index[0] + 1][index[1]] + zero_matrix[index[0] + 1][index[1] + 1] + zero_matrix[index[0] + 1][index[1] + 2]
            bottem_row = zero_matrix[index[0] + 2][index[1]] + zero_matrix[index[0] + 2][index[1] + 1] + zero_matrix[index[0] + 2][index[1] + 2]
            matrix_fuel_squares[index[0]][index[1]] = top_row + middle_row + bottem_row
        print(index)
    
    print(matrix_fuel_squares)
    print(np.where(matrix_fuel_squares == matrix_fuel_squares.max()))
    #add one to both values and then switch them
    
part1()

'''
Find the fuel cell's rack ID, which is its X coordinate plus 10.
Begin with a power level of the rack ID times the Y coordinate.
Increase the power level by the value of the grid serial number (your puzzle input).
Set the power level to itself multiplied by the rack ID.
Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
Subtract 5 from the power level.
For example, to find the power level of the fuel cell at 3,5 in a grid with serial number 8:

The rack ID is 3 + 10 = 13.
The power level starts at 13 * 5 = 65.
Adding the serial number produces 65 + 8 = 73.
Multiplying by the rack ID produces 73 * 13 = 949.
The hundreds digit of 949 is 9.
Subtracting 5 produces 9 - 5 = 4.
'''
