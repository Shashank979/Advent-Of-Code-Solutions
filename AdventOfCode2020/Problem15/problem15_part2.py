import time

def main():
    # test_input_problem14.txt
    file1 = 'input_problem15.txt'
    input_file = open(file1).read().split(",")
    list_nums = [int(x) for x in input_file]

    turns = 30000000
    turns_to_skip = len(list_nums)
    spoken = list_nums[-1]
    dict_nums = {}
    for x in range(len(list_nums) - 1):
        dict_nums[list_nums[x]] = x + 1

    for turn in range(1 + turns_to_skip, turns + 1):
        if turn % 1000000 == 0:
            print("turn: ", turn)
        if spoken in dict_nums.keys():
            before = dict_nums[spoken]
            dict_nums[spoken] = turn - 1
            spoken = turn - before - 1
        else:
            dict_nums[spoken] = turn - 1
            spoken = 0
    print(spoken)

start = time.time()          
main()
print("time taken: ", time.time() - start)
