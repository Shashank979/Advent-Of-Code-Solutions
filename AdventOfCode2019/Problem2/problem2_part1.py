def main():
    input_file = [int(x) for x in open('input_problem2.txt').read().split(",")]
    for num in range(0, len(input_file), 4):
        first_input = input_file[num + 1] 
        second_input = input_file[num + 2] 
        position = input_file[num + 3] 
        if input_file[num] == 1:
            input_file[position] = input_file[first_input] + input_file[second_input]

        elif input_file[num] == 2:
            input_file[position] = input_file[first_input] * input_file[second_input]

        elif input_file[num] == 99:
            return input_file

print(main())