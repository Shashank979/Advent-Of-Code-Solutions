import numpy as np


def array_to_string(array2d):   
    string_form = ""

    for row in array2d:
        string_form += "".join(list(row))

    return string_form



states_set = set([])

# creation of the initial state 
raw = [list(x) for x in open('input_problem24.txt').read().splitlines()]

state = np.array([".", ".", ".", ".", "."] * 5)
state = state.reshape(5, 5)

for row_index, row in enumerate(raw):
    for column_index, column in enumerate(row):
        state[row_index, column_index] = raw[row_index][column_index]
states_set.add(array_to_string(state))

print(state, '\n')

# getting the final state 
while True:
    new_state = np.array([".", ".", ".", ".", "."] * 5).reshape(5, 5)
    for row_index in range(5):
        for column_index in range(5):

            #print(row_index, ",", column_index)
            current_element = state[row_index, column_index]
            if (row_index == 2 and column_index == 2):
                print(current_element)
            bug_counter = 0
            if row_index + 1 <= 4 and row_index + 1 >= 0:
                adjacent = state[row_index + 1, column_index]
                if adjacent == "#":
                    bug_counter += 1

            if row_index - 1 <= 4 and row_index - 1 >= 0:
                adjacent = state[row_index - 1, column_index]
                if adjacent == "#":
                    bug_counter += 1
            

            if column_index + 1 <= 4 and column_index + 1 >= 0:
                adjacent = state[row_index, column_index + 1]
                if adjacent == "#":
                    bug_counter += 1
            

            if column_index - 1 <= 4 and column_index - 1 >= 0:
                adjacent = state[row_index, column_index - 1]
                if adjacent == "#":
                    bug_counter += 1
            

            #print("(", row_index, ",", column_index, ")", ":", bug_counter)

            # changing current element 
            # empty 
            if current_element == ".":
                if bug_counter == 1 or bug_counter == 2:
                    new_state[row_index, column_index] = "#"

            # bug 
            else:
                if bug_counter != 1:
                    new_state[row_index, column_index] = "."
                else:
                    new_state[row_index, column_index] = "#"
    old_len = len(states_set)
    states_set.add(array_to_string(new_state))
    if len(states_set) == old_len:
        final_state = new_state
        final_string = array_to_string(new_state)
        break 

    state = new_state.copy()

print(final_state)
print(final_string)

# calcualting biodiversity rating
biodiversity = 0
for index, element in enumerate(final_string):
    if element == "#":
        biodiversity += (2 ** index)

print(biodiversity)

