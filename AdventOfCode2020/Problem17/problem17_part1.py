import numpy 
import collections 

def main():
    file1 = 'input_problem17.txt'
    input_file = open(file1).read().splitlines()
    z = 1
    y = len(input_file)
    x = len(input_file[0])
    #print(x, y, z)
    input_file = [list(x) for x in input_file]

    #print(input_file)

    cycles = 6
    cycles += 8
    # np.full(z, y, x)
    grid = numpy.full((z + cycles * 2, y + cycles * 2, x + cycles * 2), ".")
    #print(grid.shape)

    # transcribing input to grid
    grid[cycles, cycles : cycles + y, cycles : cycles + x] = input_file

    '''
    for index, x in enumerate(grid):
        if collections.Counter(x.flatten())["#"] > 0:
            print(index)
            print(x)
    '''
    cycles = 6
    for cycle in range(cycles):
        print(cycle, "--------------------------------")
        new_grid = grid.copy()
        for iz, z in enumerate(grid):
            for iy, y in enumerate(grid):
                for ix, x in enumerate(grid):
                    new_state = calc_state(grid, iz, iy, ix)
                    new_grid[iz, iy, ix] = new_state

        grid = new_grid.copy()
        '''
        for index, x in enumerate(grid):
            if collections.Counter(x.flatten())["#"] > 0:
                print(index)
                print(x)
        '''
        finals = collections.Counter(grid.flatten())
        print(finals)

def calc_state(grid, iz, iy, ix):
    active_neighbors = collections.Counter(grid[iz-1:iz+2, iy-1:iy+2, ix-1:ix+2].flatten())["#"]
    is_active = False
    if grid[iz, iy, ix] == "#":
        active_neighbors -= 1
        is_active = True
    if is_active:
        if active_neighbors == 2 or active_neighbors == 3:
            return "#"
        else:
            return "."
    else:
        if active_neighbors == 3:
            return "#"
        else:
            return "."

main()