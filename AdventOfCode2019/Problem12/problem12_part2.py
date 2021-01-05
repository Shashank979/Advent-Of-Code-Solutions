# just test how long it takes to go 1000000000
import time 

def main():
    input_file = open('input_problem12.txt').read().split('\n')
    moons = []
    timestep = 3

    for moon in input_file:
        moon = moon.replace('<', '').replace('>', '').replace('x', '').replace('y', '').replace('z', '').replace('=', '').replace(',', '')
        moon = [int(x) for x in moon.split(" ")] + [0, 0, 0]
        for num in moon:
            moons.append(num)
    print(moons)

    universe_states = set([])
    # simulating moons motions 
    times = 0
    while True: 
        for num in range(0, len(moons) - 5, 6):
            moons[num : num + 6] = update_velocity(moons, moons[num : num + 6], num)

        for num in range(0, len(moons) - 5, 6):
            moons[num : num + 6] = update_position(moons[num : num + 6]) 
        current_len = len(universe_states)
        universe_states.add(''.join([str(x) for x in moons]))  
        if len(universe_states) == current_len:
            return times
        times += 1

        if times % 1000000 == 0:
            print(times)


def update_velocity(moons, current_moon, current_moon_index):
    # for each velocity value in the moon 
    for velocity_index in range(3, 6):
        current_position = current_moon[velocity_index - 3]
        change_counter = 0
        for moon_index in range(0, len(moons) - 5, 6):
            if moon_index != current_moon_index:
                compare_position = moons[moon_index + velocity_index - 3]
                if current_position > compare_position:
                    change_counter -= 1
                elif current_position < compare_position:
                    change_counter += 1
        current_moon[velocity_index] += change_counter        
    return current_moon

def update_position(current_moon):
    for num in range(3):
        current_moon[num] += current_moon[num + 3]
    return current_moon

def test():
    # use sets 
    # doing this for 1000000000 (which is on same magnitutde of their example) took 162 seconds 
    start = time.time()
    #1000000000
    #4686774924
    list1 = []
    for num in range(1000000000):
        list1.append(num)
    end = time.time()
    print(end - start)

#test()

print(main())