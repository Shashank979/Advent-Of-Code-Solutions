from collections import Counter
import re

def main():
    file1 = 'input_problem24.txt'
    input_file = open(file1).read().splitlines()
    tiles_state = {}
    for tile in input_file:
        directions = Counter([x for x in re.split('([ns].|.)', tile) if x != ""])
        # index 0 = e or w, index 1 = n or s
        position = [0, 0]
        for direction, count in directions.items():
            if direction == "w":
                position[0] -= count
            elif direction == "e":
                position[0] += count
            elif direction == "nw":
                position[1] += count
                position[0] -= count / 2
            elif direction == "ne":
                position[1] += count
                position[0] += count / 2
            elif direction == "sw":
                position[1] -= count
                position[0] -= count / 2
            elif direction == "se":
                position[1] -= count
                position[0] += count / 2
            else:
                print("error, unrecognized direction")
        if tuple(position) in tiles_state:
            if tiles_state[tuple(position)] == "b":
                tiles_state[tuple(position)] = "w"
            elif tiles_state[tuple(position)] == "w":
                tiles_state[tuple(position)] = "b"
        else:
            tiles_state[tuple(position)] = "b"
    print(tiles_state)
    print(list(tiles_state.values()).count("b"))

def convert_to_string(directions):
    list_directions = []
    for key in directions:
        for num in range(directions[key]):
            list_directions.append(key)
    list_directions = sorted(list_directions)
    return "".join(list_directions)

main()