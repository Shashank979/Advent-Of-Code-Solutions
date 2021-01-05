def main():
    # test_input_problem14.txt
    file1 = 'input_problem14.txt'
    input_file = open(file1).read().splitlines()
    current_mask = ""
    dict_memory = {}
    print(input_file)
    for line in input_file:
        line = line.split(" ")
        if line[0] == "mask":
            print("mask")
            current_mask = line[2]
        else:
            print("mem")
            address = int(line[0].replace("mem", "").replace("[", "").replace("]", ""))
            value = int(line[2])
            binary_value = list('{0:036b}'.format(value))
            for index, x in enumerate(current_mask):
                if x != "X":
                    binary_value[index] = x
            dict_memory[address] = int("".join(binary_value), 2)
    print(dict_memory)
    print(sum(dict_memory.values()))
main()