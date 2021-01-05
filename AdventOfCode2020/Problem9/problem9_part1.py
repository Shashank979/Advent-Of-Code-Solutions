import sys

def main():
    file1 = 'input_problem9.txt'
    preamble = 25
    input_file = open(file1).read().splitlines()
    input_file = [int(x) for x in input_file]
    for index, num in enumerate(input_file[preamble:]):
        list_look = input_file[index:index + preamble]
        final = check(list_look, num)
        #print(num, preamble)
        if not final:
            print(num)
            sys.exit()


def check(list_nums, num):
    found = False 
    for index_x, x in enumerate(list_nums):
        for index_y, y in enumerate(list_nums):
            if index_x != index_y and x + y == num:
                return True 
    return False

main()