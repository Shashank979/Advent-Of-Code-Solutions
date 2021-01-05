import numpy 

# L = 6
# # = 1
# . = 0 


def main():
    file1 = 'input_problem11.txt'
    input_file = open(file1).read().splitlines()
    #print(input_file)
    width = len(input_file[0])
    height = len(input_file)
    layout = numpy.zeros((height, width))
    #layout = numpy.empty((height, width), dtype="S1")

    for index, line in enumerate(input_file):
        converted = []
        for x in line:
            if x == "L":
                converted.append(6)
            elif x == "#":
                converted.append(1)
            elif x == ".":
                converted.append(0)
        layout[index] = converted

    changed = True 
    counter = 0
    while changed:
        changed = False 
        new = numpy.zeros((height, width))
        for row_i, row in enumerate(layout):
            for column_i, column in enumerate(layout):
                cur = layout[row_i, column_i]
                indexes = [(row_i - 1, column_i), (row_i + 1, column_i), (row_i, column_i + 1), (row_i, column_i - 1), (row_i + 1, column_i + 1), (row_i - 1, column_i + 1), (row_i + 1, column_i - 1), (row_i - 1, column_i - 1)]
                adjecent_vals = []
                for index in indexes:
                    try:
                        if index[0] >= 0 and index[0] < height and index[1] >= 0 and index[1] < width:
                            item1 = layout[index[0], index[1]]
                            adjecent_vals.append(item1)
                    except:
                        pass
                print(row_i, column_i, adjecent_vals)
                if cur == 6:
                    if adjecent_vals.count(1) == 0:
                        new[row_i, column_i] = 1
                        changed = True 
                    else:
                        new[row_i, column_i] = 6
                elif cur == 1:
                    if adjecent_vals.count(1) >= 4:
                        new[row_i, column_i] = 6
                        changed = True 
                    else:
                        new[row_i, column_i] = 1
        layout = new.copy()
        print(layout)
        print("occupied: ", numpy.count_nonzero(layout == 1))
        #counter += 1
        #if counter == 2:
            #break
    #print(layout)

#indexes = [(row_i - 1, column_i), (row_i + 1, column_i), (row_i, column_i + 1), (row_i, column_i - 1), (row_i + 1, column_i + 1), (row_i - 1, column_i + 1), (row_i + 1, column_i - 1), (row_i - 1, column_i - 1)]

main()