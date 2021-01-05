
set_bags = set([])
def main():
    global dict_bag_vals
    dict_bag_vals = {}
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
        for bag in value:
            if bag[1] == "shiny gold bag":
                tier1.append(key)
                set_bags.add(key) 

    for bag in tier1:
        recursive_finds(bag)
    print(len(set_bags))


def recursive_finds(bag_name):
    bags_it_appears_in = []
    for key, value in dict_bag_vals.items():
        for bag in value:
            if bag_name == bag[1]:
                bags_it_appears_in.append(key)
    if len(bags_it_appears_in) == 0:
        return
    for bag in bags_it_appears_in:
        set_bags.add(bag)
        recursive_finds(bag)

main()



