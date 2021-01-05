def main():
    file1 = 'input_problem10.txt'
    input_file = sorted([int(x) for x in open(file1).read().splitlines()])
    high_val = max(input_file) + 3
    input_file.insert(0, 0)
    one = 0
    three = 1
    for index, num in enumerate(input_file):
        if index > 0:
            if num - input_file[index - 1] == 1:
                one += 1
            else:
                three += 1
    print(input_file)
    print("3", three)
    print("1", one)
    print(three * one)


main()