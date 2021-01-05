#test_input_problem3.txt

'''
Step Process of How To solve : 
1. Have Conversion for the wire paths and make list of coordinate tuples for both wires  
2. Check all the points of 1st wire if they are in the list of coordinates of the second wire 
3. If a point is in the list of coordinates of the other wire then add the manhatten distance of the point
    into list of intersection distances 
4. Return the smallest manatten distance in the list of intersection distances
'''


def main():
    input_file = open('input_problem3.txt').read().split('\n')
    wire1 = input_file[0].split(",")
    wire2 = input_file[2].split(",")
    wire1_coordinates = make_list_coordinates(wire1)
    wire2_coordinates = make_list_coordinates(wire2)
    intersections_distances = []

    print(wire1_coordinates)
    print(wire2_coordinates)

    #testing 
    wire_coordinate_len = len(wire1_coordinates)
    num = 0
    for coordinate in wire1_coordinates:
        num += 1
        print(num, ":", wire_coordinate_len)
        if coordinate in wire2_coordinates:
            intersections_distances.append((abs(coordinate[0]) + abs(coordinate[1])))
    print(intersections_distances)
    intersections_distances.remove(0)
    # returns final answer 
    return min(intersections_distances)

def make_list_coordinates(some_wire):
    current_coordinate = (0,0)
    wires_coordinates = [(0,0)]
    for path in some_wire:
        direction = path[0]
        number_movements = int(path[1:])
        if direction.lower() == "r":
            for num in range(1, number_movements + 1):
                wires_coordinates.append((current_coordinate[0] + num, current_coordinate[1]))

        elif direction.lower() == "l":
            for num in range(1, number_movements + 1):
                wires_coordinates.append((current_coordinate[0] - num, current_coordinate[1]))

        elif direction.lower() == "u":
            for num in range(1, number_movements + 1):
                wires_coordinates.append((current_coordinate[0], current_coordinate[1] + num))

        elif direction.lower() == "d":
            for num in range(1, number_movements + 1):
                wires_coordinates.append((current_coordinate[0], current_coordinate[1] - num))

        else:
            print("ERROR : UNIDENTIFIED DIRECTION")
        current_coordinate = wires_coordinates[-1]

    return wires_coordinates

print(main())