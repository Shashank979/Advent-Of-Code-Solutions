def main():
    start = 246515
    end = 739105
    passwords_counter = 0 
    for num in range(start + 1, end):
        print(num)
        passwords_counter += password_check(num)
    return passwords_counter

def password_check(num):
    #doubles_list = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]
    digits = [int(x) for x in str(num)]

    has_special_adjacent = False
    for num in range(0, 10):
        indices_num = [i for i, x in enumerate(digits) if x == num]


    not_decreasing = True 
    for index, digit in enumerate(digits):
        if index != len(digits) - 1 and digits[index + 1] < digit:
            not_decreasing = False

        if index == 0 and digit == digits[index + 1] and digit != digits[index + 2]:
            has_special_adjacent = True 
        elif index == len(digits) - 2 and digit == digits[index + 1] and digit != digits[index - 1]:
            has_special_adjacent = True 
        elif index != len(digits) - 1 and digit == digits[index + 1] and digit != digits[index - 1] and digit != digits[index + 2]:
            has_special_adjacent = True 


    # returning
    if not_decreasing and has_special_adjacent:
        return 1
    else:
        return 0

print(main())
