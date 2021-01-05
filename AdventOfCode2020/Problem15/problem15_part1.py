

def main():
    # test_input_problem14.txt
    file1 = 'input_problem15.txt'
    input_file = open(file1).read().split(",")
    list_nums = [int(x) for x in input_file]
    print(list_nums)

    turns = 2020
    turns_to_skip = 7
    for turn in range(1, turns + 1):
        print("turn: ", turn)
        if turn > turns_to_skip:
            partial_list = list_nums[:len(list_nums) - 1].copy()
            if list_nums[-1] in partial_list:
                reverse_list = partial_list
                reverse_list.reverse()
                previous = len(list_nums) - reverse_list.index(list_nums[-1])
                #print(reverse_list.index(list_nums[-1]))
                #print(previous)
                list_nums.append(turn - previous)
                '''
                #print(list_nums, list_nums[-1])
                a = list_nums.copy()
                a.reverse()
                #print(a.index(list_nums[-1]))
                previous_turn = list_nums.index(list_nums[-1]) + 1
                print(previous_turn)
                list_nums.append(turn - previous_turn - 1)
                '''
            else:
                list_nums.append(0)
    print("final: ", list_nums[-1])
            
main()