def part1():
    list_all = [3, 7]
    #value, index
    index1 = 0 
    value1 = 3
    index2 = 1 
    value2 = 7
    #puzzle input + 10
    #147071
    while len(list_all) < 10:
        new_num = str(value1 + value2)
        for num in new_num:
            list_all.append(int(num))
        #1
        if len(list_all) > (value1 + 1 + index1):
            index1 = value1 + index1
        else:
            index1 = ((value1 + 1) % len(list_all)) + index1 + 1
        value1 = list_all[index1]
        #2
        if len(list_all) > (value2 + 1 + index2):
            index2 = value2 + index2
        else:
            index2 = ((value2 + 1) % len(list_all)) + index2 + 1
        value2 = list_all[index2]
        
        print("INDEX: ", index1)
        print("Value: ", value1)
        print("INDEX: ", index2)
        print("Value: ", value2)
        print(list_all)
        
        
part1()
