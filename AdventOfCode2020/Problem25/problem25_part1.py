def main():
    #file1 = 'test_input_problem25.txt'
    #input_file = open(file1).read().splitlines()
    #print(input_file)
    card = 15733400
    door = 6408062

    #15733400
    #6408062
    card_loop = 0
    door_loop = 0

    card_value = 1
    door_value = 1
    while card_value != card:
        card_value *= 7
        card_value = card_value % 20201227
        card_loop += 1
    while door_value != door:
        door_value *= 7
        door_value = door_value % 20201227
        door_loop += 1

    value = 1
    for num in range(card_loop):
        value *= door
        value %= 20201227 

    print(card_loop)
    print(door_loop)
    print(value)

main()