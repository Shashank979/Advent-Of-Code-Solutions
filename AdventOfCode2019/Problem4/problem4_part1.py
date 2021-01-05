def main():
    start = 246515
    end = 739105
    passwords_counter = 0 
    for num in range(start + 1, end):
        print(num)
        passwords_counter += password_check(num)
    return passwords_counter

def password_check(num):
    doubles_list = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]
    has_adjacent = False
    for double_nums in doubles_list:
        if double_nums in str(num):
            has_adjacent = True
            break 

    digits = [int(x) for x in str(num)]
    not_decreasing = True 
    for index, digit in enumerate(digits):
        if index != len(digits) - 1 and digits[index + 1] < digit:
            not_decreasing = False
    if not_decreasing and has_adjacent:
        return 1
    else:
        return 0

print(main())