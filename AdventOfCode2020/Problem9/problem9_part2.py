import sys

def main():
    file1 = 'input_problem9.txt'
    part1 = 556543474
    input_file = open(file1).read().splitlines()
    input_file = [int(x) for x in input_file]
    for index1, num1 in enumerate(input_file):
        for index2 in range(index1):
            slice1 = input_file[index2:index1 + 1]
            #print(slice1)
            if sum(slice1) == part1:
                print(index1, index2)
                print("small", min(slice1))
                print("large", max(slice1))
                print(min(slice1) + max(slice1))


main()