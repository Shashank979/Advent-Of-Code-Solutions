def part1():
    advent_list = []
    with open('day5.txt') as f:
        advent_string = f.read()
    for char in advent_string:
        advent_list.append(char)
    del advent_list[-1]
    places_to_remove = []
    final_list = advent_list.copy()
    counter = 0
    skip = False
    exit = False
    print(advent_list)
    while exit == False:
        for index, character in enumerate(advent_list):
            if index < (len(advent_list) - 1):
                next_character = advent_list[index + 1]
                if character.lower() == next_character.lower():
                    if (next_character.islower() and character.isupper()) or (next_character.isupper() and character.islower()):
                        if skip == False:
                            places_to_remove.append(index)
                            places_to_remove.append(index + 1)
                            skip = True
                        else:
                            skip = False
                else:
                    skip = False
        #print(places_to_remove)
        if len(places_to_remove) > 0:
            places_to_remove = sorted(set(places_to_remove))
            for num in places_to_remove:
                del advent_list[num - counter]
                counter += 1
            #print("IF: ", advent_list)
            places_to_remove = []
            counter = 0
        else:
            exit = True
            #print("Else: ", advent_list)
        #print("NEW")
            
    print(len(advent_list))

    
def part2():
    advent_list = []
    with open('day5.txt') as f:
        advent_string = f.read()
    for char in advent_string:
        advent_list.append(char)
    del advent_list[-1]

    #creating of letter dictionary
    letter_dict = {}
    for char in "abcdefghijklmnopqrstuvwxyz":
        letter_dict[char] = 0

    #iterating and getting values
    for char in "abcdefghijklmnopqrstuvwxyz":
        new_list = advent_list.copy()
        new_list = [x for x in new_list if x != char and x != char.upper()]
        
        places_to_remove = []
        counter = 0
        skip = False
        exit = False
        while exit == False:
            for index, character in enumerate(new_list):
                if index < (len(new_list) - 1):
                    next_character = new_list[index + 1]
                    if character.lower() == next_character.lower():
                        if (next_character.islower() and character.isupper()) or (next_character.isupper() and character.islower()):
                            if skip == False:
                                places_to_remove.append(index)
                                places_to_remove.append(index + 1)
                                skip = True
                            else:
                                skip = False
                    else:
                        skip = False
            if len(places_to_remove) > 0:
                places_to_remove = sorted(set(places_to_remove))
                for num in places_to_remove:
                    del new_list[num - counter]
                    counter += 1
                    places_to_remove = []
                counter = 0
                
            else:
                exit = True
                
        letter_dict[char] = len(new_list)
    
    print(letter_dict)

#This was dictionary I got:
#{'a': 11486, 'b': 11478, 'c': 11480, 'd': 11432, 'e': 11480, 'f': 11500, 'g': 11404, 'h': 11422, 'i': 4240, 'j': 11498, 'k': 11460, 'l': 11470, 'm': 11430, 'n': 11458, 'o': 11440, 'p': 11480, 'q': 11468, 'r': 11514, 's': 11448, 't': 11508, 'u': 11432, 'v': 11470, 'w': 11426, 'x': 11486, 'y': 11478, 'z': 11530}
#the smallest onew as "i" with 4240
    
    
part2()




