from itertools import cycle, islice

def main():
    # 614752839
    # 389125467
    file1 = "614752839"
    cups = [int(x) for x in list(file1)]
    current = cups[0]
    moves = 100
    #print(cups)
    for round1 in range(moves):
        #print("--------------", round1)
        circle_cups = list(islice(cycle(cups), len(file1) * 2))
        #print(circle_cups)
        three_cups = circle_cups[cups.index(current) + 1: cups.index(current) + 4].copy()
        #print(three_cups)
        for cup in three_cups:
            cups.remove(cup)
        destination = current - 1
        while True:
            if destination not in three_cups and destination in cups:
                break
            elif destination < min(cups):
                destination = max(cups)
                break
            destination -= 1
        destination_index = cups.index(destination)
        for index in range(destination_index + 1, destination_index + 4):
            cups.insert(index, three_cups[index - destination_index - 1])
        current = cups[(cups.index(current) + 1) % len(file1)]
        #print(three_cups)
        #print("destination: ", destination)
        #print("new current: ", current)
        #print(cups)
    print(moves, cups)
        
main()