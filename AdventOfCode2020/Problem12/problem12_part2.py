


def main():
    #test_input_problem12.txt
    file1 = 'input_problem12.txt'
    input_file = open(file1).read().splitlines()
    print(input_file)
    ship_direction = 90
    wp_direction = 0
    wp_coords = [10, 1]
    ship_coords = [0, 0]
    for x in input_file:
        print(x)
        action = x[0]
        value = int(x[1:])
        if action == "N":
            wp_coords[1] = wp_coords[1] + value
        elif action == "S":
            wp_coords[1] = wp_coords[1] - value
        elif action == "E":
            wp_coords[0] = wp_coords[0] + value
        elif action == "W":
            wp_coords[0] = wp_coords[0] - value
        elif action == "L":
            if value == 90:
                temp = wp_coords[0]
                wp_coords[0] = -wp_coords[1]
                wp_coords[1] = temp
            elif value == 180:
                wp_coords[0] = -wp_coords[0]
                wp_coords[1] = -wp_coords[1]
            elif value == 270:
                temp = -wp_coords[0]
                wp_coords[0] = wp_coords[1]
                wp_coords[1] = temp
        elif action == "R":
            if value == 90:
                temp = -wp_coords[0]
                wp_coords[0] = wp_coords[1]
                wp_coords[1] = temp
            elif value == 180:
                wp_coords[0] = -wp_coords[0]
                wp_coords[1] = -wp_coords[1]
            elif value == 270:
                temp = wp_coords[0]
                wp_coords[0] = -wp_coords[1]
                wp_coords[1] = temp
        elif action == "F":
            #x_dist = (wp_coords[0] - ship_coords[0]) * value 
            #y_dist = (wp_coords[1] - ship_coords[1]) * value 
            ship_coords[0] += wp_coords[0] * value
            ship_coords[1] += wp_coords[1] * value 

    
    print(abs(ship_coords[0]) + abs(ship_coords[1]))



main()