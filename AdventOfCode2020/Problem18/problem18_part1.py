import re

def main():
    file1 = 'test_input_problem18.txt'
    input_file = open(file1).read().splitlines()
    total = 0
    skip = False
    sum1 = 0
    for index, x in enumerate(input_file):
        problem = x.replace(" ", "")
        input_file[index] = problem
    finals = []
    for problem in input_file:
        while "(" in problem:
            problem = re.sub(r"\(([^()]+)\)", eval1, problem,flags=re.I)
        
        finals.append(problem)
    for almost_solved in finals:
        sum1 += int(eval1(almost_solved, True))
    print(finals)
    print(sum1)

def eval1(match, without_para = False):
    if not without_para:
        group = re.split(r"([\+\*])", match.group(1))
    else:
        group = re.split(r"([\+\*])", match)


    print(group)
    final = None 
    for index, element in enumerate(group):
        if final == None:
            final = int(element)
        else:
            if element == "*":
                final = final * int(group[index + 1])
            elif element == "+":
                final = final + int(group[index + 1])
    return str(final)

main()

