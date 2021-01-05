import numpy as np

def main():
    size = 10
    file1 = 'input_problem20.txt'
    input_file = [x.replace('\n', '') for x in open(file1).read().split("\n\n")]
    dict_tiles = {}
    all_edges = []
    corners = []
    for x in input_file:
        dict_tiles[x.split(":")[0]] = x.split(":")[1]
    for key, value in dict_tiles.items():
        new_val = np.reshape(list(value), (size, size))
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

    #print(all_edges)
    for key, value in dict_tiles.items():
        print(key)
        touched = 0
        for edge in value:
            #print(edge)
            if all_edges.count(edge) > 1 or all_edges.count(edge[::-1]) > 1:
                touched += 1
        #print(touched)
        if touched == 2:
            corners.append(key)
    final = 1
    for x in corners:
        final *= int(x.split(" ")[1])
    print(corners)
    print(final)
main()