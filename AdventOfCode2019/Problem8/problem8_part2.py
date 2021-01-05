def main():
    input_file = open('input_problem8.txt').read()
    list_nums = [int(num) for num in input_file]
    width = 25
    height = 6
    layers = []
    for num in range(0, len(list_nums), width * height):
        if num != len(list_nums) - 1:
            layers.append(list_nums[num : num + width * height])

    #print(layers)    
    message = []
    for index in range(width * height):
        for layer in layers:
            if layer[index] == 0 or layer[index] == 1:
                message.append(layer[index])
                break 
    print(message, '\n')
    final_message = []

    for index in range(0, len(message) - 24, 25):
        print(index)
        row_to_append = [0 if x == 0 else x for x in message[index : index + 25]]
        row_to_append = [1 if x == 1 else x for x in message[index : index + 25]]
        final_message.append(row_to_append)

    # printing message 3
    for x in final_message:
        for num in x:
            if num == 1:
                print('#', end ='')
            else:
                print(' ', end = '')
        print()


main()


# 0 is black 
# 1 is white
# 2 is transparent 
# looking for the first layer with a 0 or 1 
# make list of the visible ones and then print it out in 25 by 6 format 