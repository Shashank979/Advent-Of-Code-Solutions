import numpy 

def part1():
    advent_list = open('day25test.txt').read().splitlines()
    cordinate_array = []
    for cordinate in advent_list:
        cordinate_array.append([int(cordinate.split(",")[0]), int(cordinate.split(",")[1]), int(cordinate.split(",")[2]), int(cordinate.split(",")[3])])
    cordinates_after_iter = cordinate_array.copy()
    for cordinate in cordinate_array:
        counter = False
        for compare_cordinate in cordinate_array:
            distance_apart = abs(cordinate[0] - compare_cordinate[0]) + abs(cordinate[1] - compare_cordinate[1]) + abs(cordinate[2] - compare_cordinate[2]) + abs(cordinate[3] - compare_cordinate[3])
            if compare_cordinate != cordinate:
                if distance_apart <= 3:
                    counter = True
                    print(cordinate, compare_cordinate)
        if counter == False:
            cordinates_after_iter.remove(cordinate)
            
    all_constellations = {}
    for cordinate in cordinates_after_iter:
        for compare_cordinate in cordinates_after_iter:
            distance_apart = abs(cordinate[0] - compare_cordinate[0]) + abs(cordinate[1] - compare_cordinate[1]) + abs(cordinate[2] - compare_cordinate[2]) + abs(cordinate[3] - compare_cordinate[3])
            if distance_apart <= 3 and compare_cordinate != cordinate:
                if str(cordinate) in all_constellations.values():
                    try:
                        if all_constellations[str(compare_cordinate)] == str(cordinate):
                            pass
                        else:
                            all_constellations[str(cordinate)] = str(compare_cordinate)
                    except KeyError:
                        pass
                else:
                    all_constellations[str(cordinate)] = str(compare_cordinate)
    print(all_constellations, '\n')
    all_constellations_array = []
    for key in all_constellations:
        all_constellations_array.append([key, all_constellations[key]])
    
            
    print(all_constellations_array)

part1()
