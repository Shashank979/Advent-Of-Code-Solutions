


def main():
    #test_input_problem12.txt
    file1 = 'input_problem12.txt'
    input_file = open(file1).read().splitlines()
    print(input_file)
    coords = [0, 0]
    direction = 90
    for x in input_file:
        print(x)
        action = x[0]
        value = int(x[1:])
        if action == "N":
            coords[1] = coords[1] + value
        elif action == "S":
            coords[1] = coords[1] - value
        elif action == "E":
            coords[0] = coords[0] + value
        elif action == "W":
            coords[0] = coords[0] - value
        elif action == "L":
            direction -= value 
        elif action == "R":
            direction += value 
        elif action == "F":
            if direction % 360 > 0 and abs(direction % 360) != 0:
                if direction % 360 == 90:
                    coords[0] += value
                elif direction % 360 == 180:
                    coords[1] -= value
                elif direction % 360 == 270:
                    coords[0] -= value
                else:
                    print("DIRECTION BROKEN")
            elif abs(direction) % 360 == 0:
                coords[1] = coords[1] + value
            else:
                if direction % 360 == -90:
                    coords[0] -= value
                elif direction % 360 == -180:
                    coords[1] -= value
                elif direction % 360 == -270:
                    coords[0] += value
                else:
                    print("DIRECTION BROKEN")
        print(coords)
    
    print(abs(coords[0]) + abs(coords[1]))

    #for x in input_file:
        
    #vals = {'F' : 0}



main()