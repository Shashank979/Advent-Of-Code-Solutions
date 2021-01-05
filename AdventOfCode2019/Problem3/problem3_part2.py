
# fix up the code 
# final list 
#[0, 112316, 114546, 115926, 118388, 120432, 121284, 123118, 124470, 124470, 122128, 122128, 122128, 124728, 130120, 187700, 188224, 188224, 188224, 154648, 155144, 157248, 159338, 159338, 113202, 113202, 113202, 113202, 161432, 162774, 166654, 161702, 161702, 161264, 160906, 157906, 158814, 159226, 175308, 179540, 177326, 179320, 180236, 179898, 181996]

def main():
    input_file = open('input_problem3.txt').read().split('\n')
    wire1 = input_file[0].split(",")
    wire2 = input_file[2].split(",")
    wire1_coordinates = make_list_coordinates(wire1)
    wire2_coordinates = make_list_coordinates(wire2)
    intersection_steps = []

    wire1_only_coords = [x[:2] for x in wire1_coordinates]
    wire2_only_coords = [x[:2] for x in wire2_coordinates]


    wire_coordinate_len = len(wire1_coordinates)
    num = 0
    for coordinate in wire1_only_coords:
        print(num, ":", wire_coordinate_len)
        if coordinate in wire2_only_coords:
            intersection_steps.append(wire1_coordinates[num][2] + wire2_coordinates[wire2_only_coords.index(coordinate)][2])
        num += 1
    print(intersection_steps)
    intersection_steps.remove(0)
    # returns final answer 
    return min(intersection_steps)


def make_list_coordinates(some_wire):
    current_coordinate = (0,0)
    wires_coordinates = [(0,0,0)]
    steps_gone = 0
    for path in some_wire:
        direction = path[0]
        number_movements = int(path[1:])
        if direction.lower() == "r":
            for num in range(1, number_movements + 1):
                steps_gone += 1
                wires_coordinates.append((current_coordinate[0] + num, current_coordinate[1], steps_gone))

        elif direction.lower() == "l":
            for num in range(1, number_movements + 1):
                steps_gone += 1
                wires_coordinates.append((current_coordinate[0] - num, current_coordinate[1], steps_gone))

        elif direction.lower() == "u":
            for num in range(1, number_movements + 1):
                steps_gone += 1
                wires_coordinates.append((current_coordinate[0], current_coordinate[1] + num, steps_gone))

        elif direction.lower() == "d":
            for num in range(1, number_movements + 1):
                steps_gone += 1
                wires_coordinates.append((current_coordinate[0], current_coordinate[1] - num, steps_gone))

        else:
            print("ERROR : UNIDENTIFIED DIRECTION")
        current_coordinate = wires_coordinates[-1]

    return wires_coordinates

print(main())
