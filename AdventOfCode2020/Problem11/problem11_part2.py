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
                #indexes = [(row_i - 1, column_i), (row_i + 1, column_i), (row_i, column_i + 1), (row_i, column_i - 1), (row_i + 1, column_i + 1), (row_i - 1, column_i + 1), (row_i + 1, column_i - 1), (row_i - 1, column_i - 1)]
                
                adjecent_vals = adjecents(layout, row_i, column_i, width, height)
                #print(row_i, column_i, adjecent_vals)
                if cur == 6:
                    if adjecent_vals.count(1) == 0:
                        new[row_i, column_i] = 1
                        changed = True 
                    else:
                        new[row_i, column_i] = 6
                elif cur == 1:
                    if adjecent_vals.count(1) >= 5:
                        new[row_i, column_i] = 6
                        changed = True 
                    else:
                        new[row_i, column_i] = 1
        layout = new.copy()
        print(layout)
        print("occupied: ", numpy.count_nonzero(layout == 1))
        #counter += 1
        #if counter == 2:
        #    break
    #print(layout)

#indexes = [(row_i - 1, column_i), (row_i + 1, column_i), (row_i, column_i + 1), (row_i, column_i - 1), (row_i + 1, column_i + 1), (row_i - 1, column_i + 1), (row_i + 1, column_i - 1), (row_i - 1, column_i - 1)]


def adjecents(layout, row, column, width, height):
    items = []
    for z in range(row + 1, height):
        x = layout[z, column]
        if x == 1 or x == 6:
            items.append(x)
            break
    for z in range(row, 0, -1):
        x = layout[z - 1, column]
        if x == 1 or x == 6:
            items.append(x)
            break
    for z in range(column + 1, width):
        x = layout[row, z]
        if x == 1 or x == 6:
            items.append(x)
            break
    for z in range(column, 0, -1):
        x = layout[row, z - 1]
        if x == 1 or x == 6:
            items.append(x)
            break

    row_copy = row
    col_copy = column
    while row_copy + 1 >= 0 and col_copy + 1 >= 0 and row_copy + 1 < height and col_copy + 1< width:
        row_copy += 1
        col_copy += 1
        try:
            val = layout[row_copy, col_copy]
            if val == 1 or val == 6:
                #print("++")
                items.append(layout[row_copy, col_copy])
                break 
        except:
            pass
    row_copy = row
    col_copy = column
    while row_copy - 1 >= 0 and col_copy + 1 >= 0 and row_copy - 1 < height and col_copy + 1< width:
        row_copy -= 1
        col_copy += 1
        try:
            val = layout[row_copy, col_copy]
            if val == 1 or val == 6:
                #print("-+")
                items.append(layout[row_copy, col_copy])
                break 
        except:
            pass
    row_copy = row
    col_copy = column
    while row_copy + 1 >= 0 and col_copy - 1 >= 0 and row_copy + 1 < height and col_copy - 1< width:
        row_copy += 1
        col_copy -= 1
        try:
            val = layout[row_copy, col_copy]
            if val == 1 or val == 6:
                #print("+-")
                items.append(layout[row_copy, col_copy])
                break 
        except:
            pass
    row_copy = row
    col_copy = column
    while row_copy - 1 >= 0 and col_copy - 1 >= 0 and row_copy - 1 < height and col_copy - 1< width:
        row_copy -= 1
        col_copy -= 1
        try:
            val = layout[row_copy, col_copy]
            if val == 1 or val == 6:
                #print("--")
                items.append(layout[row_copy, col_copy])
                break 
        except:
            pass

    return items


main()