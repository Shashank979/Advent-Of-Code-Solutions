def main():
    input_file = open('input_problem1.txt').read().splitlines() 
    list_fuels = [calculate_total_fuel(int(x)) for x in input_file]
    total_fuel = sum(list_fuels)
    print(total_fuel)

def calculate_total_fuel(num):
    total_fuel = 0
    while num > 0:
        num = int(num / 3) - 2
        if num > 0:
            total_fuel += num
    return total_fuel


main()