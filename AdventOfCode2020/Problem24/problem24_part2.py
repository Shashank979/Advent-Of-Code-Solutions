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
    #print(tiles_state)
    #print(list(tiles_state.values()).count("b"))
    black_tiles = []
    for key in tiles_state:
        if tiles_state[key] == "b":
            black_tiles.append(key)
    black_tiles = sorted(black_tiles)
    #print(black_tiles)
    print("black tiles: ", black_tiles)
    for num in range(100):
        new_black_tiles = set([])
        for tile in black_tiles:
            #print(tile, adjacents(tile, black_tiles))
            for adjecent in adjacents(tile, black_tiles):
                new_black_tiles.add(adjecent)
        black_tiles = sorted(list(new_black_tiles))
    #print("new black tiles: ", new_black_tiles)
        print(num, len(black_tiles))

def adjacents(tile, black_tiles):
    list_adj = []
    list_adj.append((tile[0] + 1, tile[1]))
    list_adj.append((tile[0] - 1, tile[1]))
    list_adj.append((tile[0] - 0.5, tile[1] + 1))
    list_adj.append((tile[0] - 0.5, tile[1] - 1))
    list_adj.append((tile[0] + 0.5, tile[1] + 1))
    list_adj.append((tile[0] + 0.5, tile[1] - 1))
    list_adj.append((tile[0], tile[1]))
    #print(tile, list_adj)
    new_blacks = set([])
    for adj in list_adj:
        blackes_nearby = 0
        for (x, y) in [(1, 0), (-1, 0), (-0.5, 1), (-0.5, -1), (0.5, 1), (0.5, -1)]:
            if (adj[0] + x, adj[1] + y) in black_tiles:
                blackes_nearby += 1
        if adj in black_tiles:
            if blackes_nearby == 1 or blackes_nearby == 2:
                new_blacks.add(adj)
        else:
            if blackes_nearby == 2:
                new_blacks.add(adj)
    return new_blacks

main()





