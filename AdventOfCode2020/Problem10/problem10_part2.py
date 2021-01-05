import itertools
import timeit
import time 

def main():
    file1 = 'input_problem10.txt'
    input_file = sorted([int(x) for x in open(file1).read().splitlines()])
    high_val = max(input_file) + 3
    input_file.insert(0, 0)
    input_file.append(high_val)
    changes = []
    dict_trib = {}
    # creating one_stretches 
    for index, num in enumerate(input_file):
        if index > 0:
            if num - input_file[index - 1] == 1:
                changes.append(1)
            elif num - input_file[index - 1] == 3:
                changes.append(3)
            elif num - input_file[index - 1] == 2:
                print(2)
    string_changes = ''.join([str(element) for element in changes]) 
    one_stretches = string_changes.split("3")
    # making tribonnaci sequence up to highest possiblity 
    previous_three = [0,1,1]
    for num in range(2, len(input_file) + 1):
        dict_trib[num] = sum(previous_three)
        del previous_three[0]
        previous_three.append(dict_trib[num])
    dict_trib[0] = 1
    dict_trib[1] = 1
    final = 1
    # getting total arrangements
    for x in one_stretches:
        final *= dict_trib[len(x)] 
    print(final)

def manual_combs():
    for num in range(1, 6):
        print("num:", num, "---------------------------")
        final_combs = []
        for r in range(1, num + 1):
            #print('\t', "r:", r, "------------------------")
            combs = itertools.combinations([y for y in range(1, num + 1)], r)
            combs = [sorted(list(x)) for x in combs]
            #print('\t', combs)
            #combs = [sorted([x[0]]) for x in combs]
            for comb in combs:
                send = comb.copy()
                send.insert(0, 0)
                send.append(num + 3)
                if valid(send):
                    final_combs.append(send)
                #print('\t', send)
        print(final_combs)
        print(len(final_combs))

def valid(list1):
    for index, num in enumerate(list1):
        if index > 0:
            if num - list1[index - 1] > 3:
                return False 
    return True 
a = time.time()
main()
b = time.time()

# timing 
#print(b - a)
#timeit.timeit('main()', number=5)

