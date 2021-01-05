import collections
import time 

def main():
    # test_input_problem14.txt
    file1 = 'input_problem16.txt'
    input_file = open(file1).read().splitlines()
    nearby_tickets = []
    real_tickets = []
    your_ticket = []
    rules = {}
    rules_list = []
    first_empty = input_file.index("")
    error_rate = 0
    for index, line in enumerate(input_file):
        if index < first_empty:
            rules_list.append(line.split(":"))
        if "your ticket" in line:
            your_ticket = [int(x) for x in input_file[index + 1].split(",")]
        elif "nearby tickets" in line:
            nearby_tickets = input_file[index + 1:]

    for index, rule in enumerate(rules_list):
        field = rule[0]
        numbers = rule[1].strip().split(" ")
        bottom = [int(x) for x in numbers[-3].split("-")]
        top = [int(x) for x in numbers[-1].split("-")] 
        rules[field] = [bottom, top]
        rules_list[index] = [bottom, top]
    for index, ticket in enumerate(nearby_tickets):
        ticket = [int(x) for x in ticket.split(",")]
        add = True
        for num in ticket:
            if not valid(num, rules_list):
                error_rate += num
                add = False
        if add:
            real_tickets.append(ticket)
    vf_tickets = {}
    for index in range(0, len(rules)):
        possibilities = []
        for ticket in real_tickets:
            possibilities.append(special_valid(ticket[index], rules))
        vf_tickets[index] = possibilities

    for index, value in vf_tickets.items():
        counter = collections.Counter([x for y in value for x in y])
        vf_tickets[index] = [x for x in counter if counter[x] == len(real_tickets)]

    finals = {}
    while len(vf_tickets) > 0:
        for key in vf_tickets:
            if len(vf_tickets[key]) == 1:
                remove = vf_tickets[key][0]
                key_remove = key
                finals[key] = vf_tickets[key][0]
                
        del vf_tickets[key_remove]
        for key in vf_tickets:
            if len(vf_tickets[key]) != 1:
                value = vf_tickets[key]
                value.remove(remove)
                vf_tickets[key] = value
    
    final_ans = 1
    for x in finals:
        if finals[x].startswith("departure"):
            final_ans *= your_ticket[x]
    print(final_ans)
    
def valid(num, rules):
    state = True 
    for field in rules:
        for ranges in field:
            if num < ranges[0] or num > ranges[1]:
                state = False
            else:
                return True
    return state

def special_valid(num, rules_dict):
    ticket_possibles = []
    for field in rules_dict.keys():
        add = False 
        for ranges in rules_dict[field]:
            if num < ranges[0] or num > ranges[1]:
                pass
            else:
                add = True
        if add:
            ticket_possibles.append(field)
    return ticket_possibles

start = time.time()
main()
end = time.time()
print(end - start)