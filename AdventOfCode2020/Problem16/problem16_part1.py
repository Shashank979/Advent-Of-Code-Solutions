def main():
    # test_input_problem14.txt
    file1 = 'input_problem16.txt'
    input_file = open(file1).read().splitlines()
    nearby_tickets = []
    your_ticket = 0
    rules = []
    error_rate = 0
    first_empty = input_file.index("")
    for index, line in enumerate(input_file):
        if index < first_empty:
            rules.append(line.split(" "))
        if "your ticket" in line:
            your_ticket = [int(x) for x in input_file[index + 1].split(",")]
        elif "nearby tickets" in line:
            nearby_tickets = input_file[index + 1:]
    for index, ticket in enumerate(nearby_tickets):
        nearby_tickets[index] = [int(x) for x in ticket.split(",")]

    for index, rule in enumerate(rules):
        bottom = [int(x) for x in rule[-3].split("-")]
        top = [int(x) for x in rule[-1].split("-")] 
        rules[index] = [bottom, top]
    for ticket in nearby_tickets:
        for num in ticket:
            if not valid(num, rules):
                error_rate += num
                print(num)
    print(rules)
    print(your_ticket)
    print(nearby_tickets)
    print("error rate: ", error_rate)

def valid(num, rules):
    state = True 
    for field in rules:
        for ranges in field:
            if num < ranges[0] or num > ranges[1]:
                state = False
            else:
                return True
    return state

main()