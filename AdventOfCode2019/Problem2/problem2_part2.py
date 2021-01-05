
# main function 
def main():
    input_file = [int(x) for x in open('input_problem2.txt').read().split(",")]
    for num1 in range(100):
        for num2 in range(100):
            print(num1, num2)
            print("--------------------------------")
            #print("inputfile in main: ", input_file)
            output = produce_output(input_file.copy(), num1, num2)
            print(output)
            if output:
                return

# produces_output 
def produce_output(list1, pos1, pos2):
    # changing first two positions 
    list1[1] = pos1
    list1[2] = pos2
    # iterating through the list
    for num in range(0, len(list1) - 4, 4):
        first_input = list1[num + 1] 
        second_input = list1[num + 2] 
        position = list1[num + 3] 
        if list1[num] == 1:
            list1[position] = list1[first_input] + list1[second_input]

        elif list1[num] == 2:
            list1[position] = list1[first_input] * list1[second_input]

        elif list1[num] == 99:
            if list1[0] == 19690720:
                return True 
            else:
                return False 

main()