import math

def main():
    ids = []
    file1 = "input_problem5.txt"
    input_file = open(file1).read().splitlines()

    for bpass in input_file:
        row = [0, 127]
        column = [0, 7]
        for char1 in bpass:
            if char1 == "F":
                row[1] = row[0] + math.floor((row[1] - row[0]) / 2)
            elif char1 == "B":
                row[0] = row[0] + math.ceil((row[1] - row[0]) / 2)
            elif char1 == "R":
                column[0] = column[0] + math.ceil((column[1] - column[0]) / 2)
            elif char1 == "L":
                column[1] = column[0] + math.floor((column[1] - column[0]) / 2)
        id1 = row[0] * 8 + column[0]
        ids.append(id1)
    print(max(ids))

main()