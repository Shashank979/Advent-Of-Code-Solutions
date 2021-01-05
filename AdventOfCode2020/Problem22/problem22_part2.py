file1 = 'input_problem22.txt'
input_file = open(file1).read().split("\n\n")
deck1 = [int(x) for x in input_file[0].split("\n")[1:]]
deck2 = [int(x) for x in input_file[1].split("\n")[1:]]


def main(deck1, deck2, subgame = False):
    all_rounds = []
    while len(deck1) != 0 and len(deck2) != 0:
        #print(deck1, deck2)
        if deck1 in all_rounds and deck2 in all_rounds:
            if not subgame:
                return deck1
            else:
                return "1"
        all_rounds.append(deck1.copy())
        all_rounds.append(deck2.copy())
        #print("all", all_rounds)


        top1 = deck1[0]
        top2 = deck2[0]
        del deck1[0]
        del deck2[0]
        
        if top1 <= len(deck1) and top2 <= len(deck2):
            winner = main(deck1[0:top1], deck2[0:top2], True)
            if winner == "1":
                deck1.append(top1)
                deck1.append(top2)
            elif winner == "2":
                deck2.append(top2)
                deck2.append(top1)
        else:
            if top1 > top2:
                deck1.append(top1)
                deck1.append(top2)
            else:
                deck2.append(top2)
                deck2.append(top1)



    if subgame:
        if len(deck2) == 0:
            return "1"
        else:
            return "2"

    if len(deck2) == 0:
        final_deck = deck1
    else:
        final_deck = deck2
    final = 0   
    print(final_deck)
    for index, num in enumerate(reversed(final_deck)):
        final += (index + 1) * num
    print(final)



main(deck1, deck2)

