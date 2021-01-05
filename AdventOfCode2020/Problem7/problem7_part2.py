def main():
    global dict_bag_vals
    dict_bag_vals = {}
    global final 
    final = 0
    global test
    test = []
    file1 = 'input_problem7.txt'
    input_file = open(file1).read().splitlines()
    for line in input_file:
        line = line.split("contain")
        second_part = line[1].split(",")
        second_part = [x.lstrip().strip().replace(".", "").replace("bags", "bag") for x in second_part]
        second_part = [(x.split(" ")[0], x[x.find(" ") + 1: len(x)]) for x in second_part]
        dict_bag_vals[line[0].replace("bags", "bag").rstrip()] = second_part
    tier1 = []
    for key, value in dict_bag_vals.items():
        if key == "shiny gold bag":
            for bag in value:
                #print(bag)
                final += int(bag[0])

                recursive_finds(bag[1], int(bag[0]))
    print(sum(test) + final)
    

def recursive_finds(bag_name, num_bags):
    bags = dict_bag_vals[bag_name]
    if bags[0][0] == "no":
        return 

    bags_sum = 0
    for bag in bags:
        bags_sum += int(bag[0])

    for bag in bags:
        test.append(num_bags * int(bag[0]))
        recursive_finds(bag[1], num_bags * int(bag[0]))




#main()


def using_trees():
    file1 = 'test_input_problem7.txt'
    input_file = open(file1).read().splitlines()
    dict_bag_vals = {}
    for line in input_file:
        line = line.split("contain")
        second_part = line[1].split(",")
        second_part = [x.strip().replace(".", "").replace("bags", "bag") for x in second_part]
        second_part = [(x.split(" ")[0], x[x.find(" ") + 1: len(x)]) for x in second_part]
        dict_bag_vals[line[0].replace("bags", "bag").strip()] = second_part
    
    print(dict_bag_vals)

using_trees()




