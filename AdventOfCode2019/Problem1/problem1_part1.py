def main():
    input_file = open('input_problem1.txt').read().splitlines()
    list_nums = [int(int(x) / 3) - 2 for x in input_file]
    print(sum(list_nums))
    
main()