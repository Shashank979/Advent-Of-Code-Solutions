import itertools

def main():
    # test_input_problem14.txt
    file1 = 'input_problem14.txt'
    input_file = open(file1).read().splitlines()
    current_mask = ""
    dict_memory = {}
    for line in input_file:
        line = line.split(" ")
        if line[0] == "mask":
            #print("mask")
            current_mask = line[2]
        else:
            address = int(line[0].replace("mem", "").replace("[", "").replace("]", ""))
            binary_address = list('{0:036b}'.format(address))
            value = int(line[2])
            addresses_to_write = all_addresses(binary_address, current_mask)
            for address in addresses_to_write:
                dict_memory[address] = value
    print(sum(dict_memory.values()))


def all_addresses(address, mask):
    addresses_to_write = []
    indexes = []
    ones = []
    combinations = []
    for index, letter in enumerate(mask):
        if letter == "X":
            indexes.append(index)
        elif letter == "1":
            ones.append(index)
    #print("indexes", indexes)
    for num in range(0, len(indexes) + 1):
        combinations = list(itertools.combinations(indexes, num))
        #print("combinations", combinations)
        for combination in combinations:
            address_copy = address.copy()
            for index in indexes:
                if index in combination:
                    address_copy[index] = "1"
                else:
                    address_copy[index] = "0"
            for one in ones:
                address_copy[one] = "1"
            #print(address_copy)
            addresses_to_write.append(int("".join(address_copy), 2))
    return addresses_to_write


main()