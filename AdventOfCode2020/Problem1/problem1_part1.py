def main():
    input_file = [int(x) for x in open('input_problem1.txt').read().splitlines()]
    print(input_file)
    list1 = []
    for num1 in input_file:
        for num2 in input_file:
            if num1 + num2 == 2020:
                print(num1, ", ", num2)
                return num1 * num2
print(main())