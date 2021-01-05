

def part1():
    f = open('day12.txt', 'r+')
    pot_key_string = f.read()
    f.close()
    pot_key_list = pot_key_string.split('\n')
    
    #creation of initial (25 extra "." on each side) and new
    #initial is 100 characters long
    initial = list(pot_key_list[0])
    total_plants = 0
    for num in range(25):
        initial.append(".")
        initial.insert(0, ".")
    
    #deleting
    del pot_key_list[0]
    del pot_key_list[0]
    del pot_key_list[-1]

    #dictionary creation
    dict_plant = {}
    dict_pot = {}
    for string1 in pot_key_list:
        list_of_key = list(string1.split()[0])
        right_and_left_vals_list = [list_of_key[0], list_of_key[1], list_of_key[3], list_of_key[4]]
        right_and_left_vals_string = ''.join(right_and_left_vals_list)
        if list_of_key[2] == ".":
            dict_pot[right_and_left_vals_string] = string1.split()[2]
        else:
            dict_plant[right_and_left_vals_string] = string1.split()[2]
    
    #iterations
    for num in range(5000000000):
        if num%100000000 == 0:
            print(num)
        if num != 0:
            initial = new.copy()
        new = []
        for index, char in enumerate(initial):
            #not doing actions on things at first, second, last, or second last vals
            if index not in (0, 1, 148, 149):
                list_of_chars_nearby = [initial[index - 2], initial[index - 1], initial[index + 1], initial[index + 2]]
                string_of_chars_nearby = ''.join(list_of_chars_nearby)
                if char == ".":
                    if string_of_chars_nearby in dict_pot:
                        new.append(dict_pot[string_of_chars_nearby])
                    else:
                        new.append(".")
                else:
                    if string_of_chars_nearby in dict_plant:
                        new.append(dict_plant[string_of_chars_nearby])
                    else:
                        new.append(".")
                    if num == 20:
                        total_plants += (index - 25)
            else:
                new.append(char)
        print(total_plants)
    print(total_plants)
part1()
