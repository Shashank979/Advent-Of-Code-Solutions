# -----GCD library 
#from sympy.ntheory import factorint
#factorint(10**20+1)   -> gives prime factorization 
# -----GCD library 

def using_chinese_remainder_theorem():
    file1 = 'input_problem13.txt'
    input_file = open(file1).read().splitlines()
    buses = input_file[1].split(",")
    buses.reverse()
    nums = [int(x) for x in buses if x.isdigit()]
    n = 1
    for num in nums:
        n *= num
    total = 0
    for index, bus in enumerate(buses):
        if bus.isdigit() and index != 0:
            bus = int(bus)
            bi = index
            ni = int(n / bus)
            xi = 1
            while (ni * xi) % bus != 1:
                xi += 1
            binixi = bi * ni * xi
            total += binixi
    print((total - len(buses) + 1) % (n))

using_chinese_remainder_theorem()


