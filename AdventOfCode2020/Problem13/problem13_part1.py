def main():
    file1 = 'input_problem13.txt'
    input_file = open(file1).read().splitlines()
    earliest = int(input_file[0])
    closest_time = None 
    closest_id = None 
    buses = input_file[1].split(",") 
    print(input_file)
    print(buses)
    for bus in buses:
        if bus != "x":
            bus = int(bus)
            dtime = earliest - (earliest % bus) + bus
            if closest_id == None or dtime < closest_time:
                closest_id = bus
                closest_time = dtime
    print(closest_id * (closest_time - earliest))

main()