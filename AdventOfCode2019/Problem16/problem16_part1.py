# works but is slow, full answer took like 1 minute 

def main():
    list_digits = [int(x) for x in open('test_input_problem16.txt').read().strip()]
    phases = 100
    #print(list_digits)
    for num in range(phases):
        print(num)
        new_list_digits = []
        for index, digit in enumerate(list_digits):
            repeated_pattern = create_pattern(index, len(list_digits))
            del repeated_pattern[0]
            new_digit = int(str(abs(sum([digit2 * repeated_pattern[x] for x, digit2 in enumerate(list_digits)])))[-1])
            new_list_digits.append(new_digit)
        list_digits = new_list_digits
    #print(list_digits)
    print("".join(str(x) for x in list_digits[0:8]))

def create_pattern(position, length_list):
    length_list += 1
    pattern = []
    counter = 0
    while counter < length_list:
        for num in range(position + 1):
            pattern.append(0)
            counter += 1
        for num in range(position + 1):
            pattern.append(1)
            counter += 1
        for num in range(position + 1):
            pattern.append(0)
            counter += 1
        for num in range(position + 1):
            pattern.append(-1)
            counter += 1
    #print(pattern)

    return pattern[0:length_list]

main()

#print(create_pattern(5, 8))