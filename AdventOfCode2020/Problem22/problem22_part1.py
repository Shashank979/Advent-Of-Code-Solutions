def main():
    file1 = 'input_problem22.txt'
    input_file = open(file1).read().split("\n\n")
    deck1 = [int(x) for x in input_file[0].split("\n")[1:]]
    deck2 = [int(x) for x in input_file[1].split("\n")[1:]]
    counter = 0
    while len(deck1) != 0 and len(deck2) != 0:
        top1 = deck1[0]
        top2 = deck2[0]
        del deck1[0]
        del deck2[0]
        if top1 > top2:
            deck1.append(top1)
            deck1.append(top2)
        else:
            deck2.append(top2)
            deck2.append(top1)

    if len(deck2) == 0:
        final_deck = deck1
    else:
        final_deck = deck2
    final = 0   
    for index, num in enumerate(reversed(final_deck)):
        final += (index + 1) * num
    print(final)

main()