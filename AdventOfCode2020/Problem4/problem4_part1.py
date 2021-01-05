def main():
    valids = 0
    file1 = "input_problem4.txt"
    input_file = open(file1).read().split('\n\n')
    for passport in input_file:
        passport = passport.replace('\n', '')
        if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
            valids += 1

    print(valids)
"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

main()