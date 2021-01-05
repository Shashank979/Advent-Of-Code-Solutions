import numpy as np

def main():
    size = 10
    file1 = 'test_input_problem20.txt'
    input_file = [x.replace('\n', '') for x in open(file1).read().split("\n\n")]
    dict_tiles = {}
    for x in input_file:
        dict_tiles[x.split(":")[0]] = x.split(":")[1]
    for key, value in dict_tiles.items():
        new_val = np.reshape(list(value), (size, size))
        dict_tiles[key] = new_val
        rotations_dict = {}
        '''
        edges = []
        # regular 
        edges.append("".join(new_val[0, :]))
        edges.append("".join(new_val[:, 0]))
        edges.append("".join(new_val[:, size - 1]))
        edges.append("".join(new_val[size - 1, :]))
        # switched 
        #edges.append("".join(new_val[0, :])[::-1])
        #edges.append("".join(new_val[:, 0])[::-1])
        #edges.append("".join(new_val[:, size - 1])[::-1])
        #edges.append("".join(new_val[size - 1, :])[::-1])
        for x in edges:
            all_edges.append(x)
            all_edges.append(x[::-1])
        dict_tiles[key] = edges
        '''


    val = str(2311)
    first_tile = dict_tiles[val]
    for title + rotation in dict_tiles:
        
    '''
    positions = {}
    for edge in first_tile:
        matches = all_edges[edge[0]]
        for match in matches:
            if match not in positions.keys():
                positions[match] = positions[first_tile][0]
                recusrive()
    '''
    print(dict_tiles)

main()