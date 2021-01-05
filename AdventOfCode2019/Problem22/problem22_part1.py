def main():
    raw = open('input_problem22.txt').read().splitlines()
    factory_orders = []
    num_cards = 10007
    deck = [x for x in range(0, num_cards)]

    for order in raw:
        if order[0:3].lower() == "cut":
            factory_orders.append(["c", int(order.split(" ")[1])])
        elif order.lower() == "deal into new stack":
            factory_orders.append(["d"])
        else:
            factory_orders.append(["i", int(order.split(" ")[3])])
    print(factory_orders)

    for order in factory_orders:
        # cut
        if order[0] == "c":
            deck = cut(deck, order[1])

        # deal into new stack 
        elif order[0] == "d":
            deck = deal_new_stack(deck)

        # deal with increment
        else:
            deck = deal_increment(deck, order[1], num_cards)
    print(deck)
    # print(deck.index(2019))

def cut(deck, n):
    return deck[n:] + deck[0:n]

def deal_new_stack(deck):
    deck.reverse()
    return deck

def deal_increment(deck, n, num_cards):
    i = 0
    new_deck = [x for x in range(0, num_cards)]
    for num in range(num_cards):
        if i + n < num_cards:
            new_deck[i] = deck[num]
        else:  
            new_deck[i % num_cards] = deck[num]
        i += n 
    return new_deck 


main()

