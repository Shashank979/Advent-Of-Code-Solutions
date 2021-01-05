import numpy as np
import numpy
import collections

def part1():
    instruction_list = open("day7test.txt").read().splitlines()
    
    items_at_end = []
    alphabet = "ABCDEF"
    before_dict_unordered = {}
    before_dict_ordered = {}
    final_order = []
    
    #making before_dict_unordered
    for instruction in instruction_list:
        first_char = instruction.split()[1]
        second_char = instruction.split()[7]
        if first_char not in before_dict_unordered:
            before_dict_unordered[first_char] = set([second_char])
        else:
            first_char_set = before_dict_unordered[first_char]
            first_char_set.add(second_char)

    #getting the items that need to be at end
    for character in alphabet:
        if character not in before_dict_unordered:
            items_at_end.append(character)
    items_at_end = sorted(items_at_end)

    #sorting the values in before_dict
    for key, value in before_dict_unordered.items():
        value = sorted(value)
        before_dict_ordered[key] = value

    for key, value in before_dict_ordered.items():
        items_to_put = False
        for list_val in before_dict_ordered.values():
            if key in list_val and len(list_val) > 1:
                for index, character in enumerate(list_val):
                    
                items_to_put.append(list_val)
        if items_to_put != False:
            
        if key in final_order:
            
        else:
            final_order.append(key)
            for letter in value:
                final_order.append(letter)

    
    #printing
    print(before_dict_ordered)


part1()
