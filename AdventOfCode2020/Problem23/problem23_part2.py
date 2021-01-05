from itertools import cycle, islice
import time 

def main():
    # 614752839
    # 389125467
    file1 = "614752839"
    cups = [int(x) for x in list(file1)]
    cups += [x for x in range(10, 1000001)]
    current = cups[0]
    max_five = [x for x in range(len(cups), len(cups) - 5, -1)]
    moves = 10000000
    # creating dict
    dict1 = {}
    for index, cup in enumerate(cups):
        if index == len(cups) - 1:
            dict1[cup] = cups[0]
        else:
            dict1[cup] = cups[index + 1]

    # going through moves 
    for round1 in range(moves - 1):
        first_cup = dict1[current]
        second_cup = dict1[first_cup]
        third_cup = dict1[second_cup]
        three_cups = [first_cup, second_cup, third_cup]

        new_current = dict1[third_cup]
        # getting destination cup 
        destination = current - 1
        while True:
            if destination < 1:
                destination = max([x for x in max_five if x not in three_cups])
                break
            elif destination not in three_cups:
                break
            destination -= 1
        # setting new values 
        dict1[third_cup] = dict1[destination]
        dict1[destination] = first_cup
        dict1[current] = new_current
        current = new_current
    print("move:", round1 + 2)
    print(dict1[1], dict1[dict1[1]])
    print(dict1[1] * dict1[dict1[1]])
main()


