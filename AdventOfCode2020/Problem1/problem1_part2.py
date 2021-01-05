def main():
    input_file = [int(x) for x in open('input_problem1.txt').read().splitlines()]
    print(input_file)
    list1 = []
    for num1 in input_file:
        for num2 in input_file:
            for num3 in input_file:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3

print(main())