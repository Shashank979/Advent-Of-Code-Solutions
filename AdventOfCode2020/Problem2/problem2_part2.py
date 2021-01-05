def main():
    input_file = open('input_problem2.txt').read().splitlines()
    corrects = 0
    valid_pws = 0
    for line1 in input_file:
        list_elements = line1.split(" ")
        min_range = int(list_elements[0].split("-")[0])
        max_range = int(list_elements[0].split("-")[1])
        letter = list_elements[1][0]
        password = list_elements[-1]
        if password[min_range - 1] == letter:
            corrects += 1
        if password[max_range - 1] == letter:
            corrects += 1
        if corrects == 1:
            valid_pws += 1
        corrects = 0
    print(valid_pws)
    #print(input_file)

main()