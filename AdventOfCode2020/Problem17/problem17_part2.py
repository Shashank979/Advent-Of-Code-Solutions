import numpy 
import collections 

def main():
    file1 = 'input_problem17.txt'
    input_file = open(file1).read().splitlines()
    a = 1
    z = 1
    y = len(input_file)
    x = len(input_file[0])
    input_file = [list(x) for x in input_file]

    cycles = 6
    cycles += 8
    grid = numpy.full((a + cycles * 2, z + cycles * 2, y + cycles * 2, x + cycles * 2), ".")

    # transcribing input to grid
    grid[cycles, cycles, cycles : cycles + y, cycles : cycles + x] = input_file

    cycles = 6
    for cycle in range(cycles):
        print(cycle, "--------------------------------")
        new_grid = grid.copy()
        for ia, a in enumerate(grid):
            print(ia)
            for iz, z in enumerate(grid):
                for iy, y in enumerate(grid):
                    for ix, x in enumerate(grid):
                        new_state = calc_state(grid, ia, iz, iy, ix)
                        new_grid[ia, iz, iy, ix] = new_state

        grid = new_grid.copy()
        finals = collections.Counter(grid.flatten())
        print(finals)

def calc_state(grid, ia, iz, iy, ix):
    active_neighbors = collections.Counter(grid[ia - 1:ia + 2, iz-1:iz+2, iy-1:iy+2, ix-1:ix+2].flatten())["#"]
    is_active = False
    if grid[ia, iz, iy, ix] == "#":
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