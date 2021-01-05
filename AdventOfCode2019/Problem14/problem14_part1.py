import math
from anytree import Node, RenderTree

# some error happening on the test case that returns 180697
# even the number of MNCFX is wrong by a magnitude f0r sure (it calculted to be 800000)
# look into MNCFX and see what proper value should be 
# Used base_val, seems bad though not working for second case
# and leads to error in third one, maybe need to do thing where all vals reset after each turn idk. 




# FIGURING OUT NODES, need to figure out how to add nodes. 


class Chemical:
    def __init__(self, name, number):
        self.name = name
        self.number = number



def main():
    reactions = open('test_input_problem14.txt').read().splitlines()
    dict_ores = {}
    dict_reactions = {}


    # creation of dict of ores and dict of the reactions 
    for reaction in reactions:
        reaction = reaction.split(" => ")
        input_chemicals_raw = reaction[0].split(", ")
        input_chemicals = []

        output_chemical = reaction[1].split(" ")
        output_chemical = Chemical(output_chemical[1], int(output_chemical[0]))


        for chemical in input_chemicals_raw:
            input_chemicals.append(Chemical(chemical.split(" ")[1], int(chemical.split(" ")[0])))

        dict_reactions[output_chemical] = input_chemicals
        
        # creation of dict_ores
        if input_chemicals[0].name == "ORE":
            dict_ores[output_chemical.name] = [output_chemical.number, input_chemicals[0].number]


    print(dict_ores)

    
    for key, value in dict_reactions.items():
        if key.name == "FUEL":
            fuel_node = Node(key)
            next(key, dict_reactions, None, fuel_node)
    
    for pre, fill, node in RenderTree(fuel_node):
        print("%s%s%s%s" % (pre, node.name.name, ":", node.name.number))

    for pre, fill, node in RenderTree(fuel_node):
        print(node.name)





def next(parent_chemical, dict_reactions, parent_node, fuel_node):
    if parent_node == None:
        child_node = fuel_node
    else:
        child_node = Node(parent_chemical, parent = parent_node)     


    '''
    for pre, fill, node in RenderTree(fuel_node):
        print("%s%s%s%s" % (pre, node.name.name, ":", node.name.number)) 
    '''

    for key in dict_reactions.keys():
        if key.name == parent_chemical.name:
            children_chemicals = dict_reactions[key]

    for child in children_chemicals:
        if child.name == "ORE":
            ore_node = Node(child, parent = child_node)
            return 
        else:
            next(child, dict_reactions, child_node, fuel_node)

'''
class Chemical:
    def __init__(self, name, number):
        self.name = name
        self.number = number


def main():
    global chemicals_needed 
    chemicals_needed = {}
    reactions = open('test_input_problem14.txt').read().splitlines()
    global dict_ores 
    dict_ores = {}
    global dict_reactions 
    dict_reactions = {}
    ores_needed = 0

    # TBD make dict ores so its normal dict where a : [2, 5], b : [3, 10]

    # creation of dict of ores and dict of the reactions 
    for reaction in reactions:
        reaction = reaction.split(" => ")
        input_chemicals_raw = reaction[0].split(", ")
        input_chemicals = []

        output_chemical = reaction[1].split(" ")
        output_chemical = Chemical(output_chemical[1], int(output_chemical[0]))


        for chemical in input_chemicals_raw:
            input_chemicals.append(Chemical(chemical.split(" ")[1], int(chemical.split(" ")[0])))

        dict_reactions[output_chemical] = input_chemicals
        
        # creation of dict_ores
        if input_chemicals[0].name == "ORE":
            dict_ores[output_chemical.name] = [output_chemical.number, input_chemicals[0].number]
            chemicals_needed[output_chemical.name] = 0
    for key, value in dict_reactions.items():
        if key.name == "FUEL":
            next(key)

    
    print(dict_ores)
    print(chemicals_needed)

    for key, value in dict_reactions.items():
        print("---------------")
        print(key.name, "  ", key.number, ":    ")
        for chemical in value:
            print('\t', chemical.name, "  ", chemical.number)




    for chemical1, value in chemicals_needed.items():
        parent_key = dict_ores[chemical1][0]
        parent_ores = dict_ores[chemical1][1]
        
        # parent_key = 2
        # value = 23
        #if value % parent_key == 0:
        #    ores_needed += (value / parent_key * parent_ores)
        #else:
        #    ores_needed += (math.ceil(value / parent_key) * parent_ores)
        ores_needed += (math.ceil(value / parent_key) * parent_ores)
    print(ores_needed)


def next(parent_chemical):
    global base_val

    print(parent_chemical.name, ":", parent_chemical.number)
    for key, value in dict_reactions.items():
        print('\t', key.name, "  ", key.number, ":    ")
        for chemical in value:
            print('\t' * 2, chemical.name, "  ", chemical.number)


    if parent_chemical.name in dict_ores:

        parent_key = dict_ores[parent_chemical.name][0]
        parent_ores = dict_ores[parent_chemical.name][1]

        print("------")

        if parent_chemical.number > parent_key:
            chemicals_needed[parent_chemical.name] += parent_chemical.number 
        else:
            chemicals_needed[parent_chemical.name] += parent_chemical.number 

        # TRYING
        parent_chemical.number = base_val

        
        
        return



    for key in dict_reactions.keys():
        if key.name == parent_chemical.name:
            parent_key = key 
            #print("PARENT KEY}", parent_key.name, ": ", parent_key.number)
            children_chemicals = dict_reactions[parent_key]
            #for x in children_chemicals:
            #    print("(", x.name, ",", x.number, ")", end = ' ')
            #print()

    for child in children_chemicals:
        if parent_chemical.number > parent_key.number:
            #rint(child.number)
            #print(parent_chemical.number, " ", parent_key.number)

            # TRYING
            base_val = child.number

            child.number = child.number * math.ceil(parent_chemical.number / parent_key.number)
            next(child)
        else:
            next(child)
'''

main()