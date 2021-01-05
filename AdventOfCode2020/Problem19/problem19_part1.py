import re


file1 = 'input_problem19.txt'
input_file = open(file1).read().split('\n\n')
rules = input_file[0].split("\n")
messages = input_file[1].split("\n")
global dict_rules
dict_rules = {}
for rule in rules:
    if "|" in rule:
        halves = rule.split(":")[1].split("|")
        dict_rules[rule.split(":")[0]] = [[x for x in halves[0].split(" ") if x != ""], "|", [x for x in halves[1].split(" ") if x != ""]]
    elif "a" in rule or "b" in rule:
        dict_rules[rule.split(":")[0]] = rule.split(":")[1].replace('"', "").replace(" ", "")
    else:
        dict_rules[rule.split(":")[0]] = [x for x in rule.split(":")[1].split(" ") if x != ""]


global glob_pos
glob_pos = 0


def main(messages):
    valids = 0
    #print(dict_rules["0"])
    path = re.compile(check(dict_rules["0"], 0, messages[0]))
    for index, message in enumerate(messages):
        print(index)
        x = re.fullmatch(path, message)
        if x != None:
            valids += 1
    print(valids)

def check(rule, pos, message):
    #print("rule: ", rule)
    #print("pos: ", pos, '\n')
    if type(rule) != list and "|" in dict_rules[rule]:
        first_half = dict_rules[rule][0]
        second_half = dict_rules[rule][2]
        return "(" + check(first_half, pos, message) + "|" + check(second_half, pos, message) + ")"
    elif type(rule) != list and dict_rules[rule] == "a":
        return "a"
    elif type(rule) != list and dict_rules[rule] == "b":
        return "b"
    else:
        if type(rule) == list:
            half = rule
        else:
            half = dict_rules[rule]

        if len(half) == 2:
            return check(half[0], pos, message) + check(half[1], pos + 1, message)
        elif len(half) == 3:
            return check(half[0], pos, message) + check(half[1], pos + 1, message) + check(half[2], pos + 2, message)
        #need to add option for len(half) == 1
        elif len(half) == 1:
            return check(half[0], pos, message)
        else:
            print("error")


main(messages)

