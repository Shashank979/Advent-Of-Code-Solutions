def main():
    input_file = open('input_problem2.txt').read().splitlines()
    valids = 0
    for line1 in input_file:
        list_elements = line1.split(" ")
        min_range = int(list_elements[0].split("-")[0])
        max_range = int(list_elements[0].split("-")[1])
        letter = list_elements[1][0]
        password = list_elements[-1]
        print(list_elements)
        print(min_range)
        print(max_range)
        print(letter)
        print(password)
        if password.count(letter) >= min_range and password.count(letter) <= max_range:
            valids += 1
    print(valids)

main()