def main():
    valids = 0
    file1 = "input_problem4.txt"
    input_file = open(file1).read().split('\n\n')
    for passport in input_file:
        passport = passport.replace('\n', ' ')
        valid = True 
        if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
            elements = passport.split(" ")
            for element in elements:
                field = element.split(":")[0]
                data = element.split(":")[1]
                if field == "byr":
                    if int(data) >= 1920 and int(data) <= 2002:
                        pass
                    else:
                        print(field)
                        valid = False 
                elif field == "iyr":
                    if int(data) >= 2010 and int(data) <= 2020:
                        pass
                    else:
                        print(field)
                        valid = False
                elif field == "eyr":
                    if int(data) >= 2020 and int(data) <= 2030:
                        pass
                    else:
                        print(field)
                        valid = False
                elif field == "hgt":
                    unit = data[len(data) - 2: len(data)]
                    number1 = data[0:len(data) - 2]  
                    if unit == "cm":
                        if int(number1) >= 150 and int(number1) <= 193:
                            pass
                        else:
                            print(field)
                            valid = False
                    elif unit == "in":
                        if int(number1) >= 59 and int(number1) <= 76:
                            pass
                        else:
                            print(field)
                            valid = False
                    else:
                        print(field)
                        valid = False 
                elif field == "hcl":
                    if data[0] == "#" and len(data) == 7:
                        for digit in data[1:7]:
                            if digit in [str(x) for x in range(0,10)] or digit in ["a", "b", "c", "d", "e", "f"]:
                                pass
                            else:
                                print(field)
                                valid = False    
                    else:
                        print(field)
                        valid = False
                elif field == "ecl":
                    if data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        pass
                    else:
                        print(field)
                        valid = False
                elif field == "pid":
                    if len(data) == 9:
                        pass
                    else:
                        print(field)
                        valid = False
            if valid:
                valids += 1
    print("num of valids: ", valids)

main()