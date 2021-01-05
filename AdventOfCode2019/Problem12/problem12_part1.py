def main():
    input_file = open('input_problem12.txt').read().split('\n')
    moons = []
    timestep = 1000
    total = 0

    for moon in input_file:
        moon = moon.replace('<', '').replace('>', '').replace('x', '').replace('y', '').replace('z', '').replace('=', '').replace(',', '')
        moons.append([[int(x) for x in moon.split(" ")], [0, 0, 0]])

    

    # simulating moons motions 
    for num in range(timestep):
        # updating velocities 
        for index, moon in enumerate(moons): 
            moons[index] = update_velocity(moons, moon, index)
        # updating positions 
        for index, moon in enumerate(moons): 
            moons[index] = update_position(moon)

        for moon in moons:
            print(moon)
        print()
    # getting total energy 
    for moon in moons:
        pe = sum([abs(x) for x in moon[0]])
        ke = sum([abs(x) for x in moon[1]])
        # need parenthesis ? 
        total += pe * ke
    return total 

def update_velocity(moons, current_moon, current_moon_index):
    # for each velocity value in the moon 
    for velocity_index in range(3):
        
        current_position = current_moon[0][velocity_index]
        change_counter = 0 
        for moon_index in range(4):
            if moon_index != current_moon_index:
                if current_position > moons[moon_index][0][velocity_index]:
                    change_counter -= 1
                elif current_position < moons[moon_index][0][velocity_index]:
                    change_counter += 1
        current_moon[1][velocity_index] += change_counter
        
    return current_moon

# done 
def update_position(current_moon):
    for num in range(3):
        current_moon[0][num] += current_moon[1][num]
    return current_moon

print(main())