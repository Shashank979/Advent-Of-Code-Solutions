
"""
station = Station(13, -17)
num_asteroids = 200

station = Station(11, -13)
num_asteroids = 20

station = Station(3, -2)
num_asteroids = 20
"""




import math 

def main():
    # variables 
    asteroids = []
    station = Station(13, -17)
    num_asteroids = 200

    map = open('input_problem10.txt').read().splitlines()

 
    for row_index, row in enumerate(map):
        for column_index, column in enumerate(row):
            if map[row_index][column_index] == "#" and (column_index != station.x or -row_index != station.y):
                astr_to_add = Asteroid(column_index, -row_index)
                astr_to_add.station_distance = math.sqrt((station.x - astr_to_add.x) ** 2 + (station.y - astr_to_add.y) ** 2)
                astr_to_add.angle = calc_angle(station, astr_to_add)
                asteroids.append(astr_to_add)

    # asteroids sorted by angle 
    asteroids = sorted(asteroids, key=lambda asteroid: asteroid.angle) 

    

    d2_asteroids = []
    sub_list = []
    max_list_size = 0
    for index, asteroid in enumerate(asteroids):
        if index == len(asteroids) - 1:
            if asteroid.angle == asteroids[index - 1].angle:
                sub_list.append(asteroid)
            else:
                sub_list = []
                sub_list.append(asteroid)
            d2_asteroids.append(sorted(sub_list, key=lambda asteroid: asteroid.station_distance))  
            if len(sub_list) > max_list_size:
                max_list_size = len(sub_list)
        elif asteroid.angle == asteroids[index + 1].angle:
            sub_list.append(asteroid)
        else :
            sub_list.append(asteroid)
            d2_asteroids.append(sorted(sub_list, key=lambda asteroid: asteroid.station_distance))
            if len(sub_list) > max_list_size:
                max_list_size = len(sub_list)
            sub_list = []

    final_list = []
    for order in range(max_list_size):
        for same_angle_asteroids in d2_asteroids:
            try: 
                final_list.append(same_angle_asteroids[order])
            except IndexError:
                pass 

    #print(final_list[num_asteroids - 1].x, final_list[num_asteroids - 1].y)

    for index, asteroid in enumerate(final_list):
        print(str(index + 1), ":  ", "(", str(asteroid.x), ",", str(asteroid.y), ",", str(asteroid.angle), ",", str(asteroid.station_distance), ")")


    

def calc_angle(station, astr):

    # x equal and asteroid above 
    if station.x == astr.x and station.y < astr.y:
        return 0

    # x equal and asteroid below 
    elif station.x == astr.x and station.y > astr.y:
        return 180

    # y equal and asteroid to right
    elif station.y == astr.y and station.x < astr.x:
        return 90

    # y equal and asteroid to left
    elif station.y == astr.y and station.x > astr.x:
        return 270

    # need to make sure this math is right 
    y_diff = abs(station.y - astr.y)
    x_diff = abs(station.x - astr.x)
    inverse_tan = math.degrees(math.atan((x_diff / y_diff)))

    # NEED TO FIX THESE 
    # astr in 1 quadrant
    if station.x < astr.x and station.y < astr.y:
        return inverse_tan

    # astr in 2 quadrant
    elif station.x > astr.x and station.y < astr.y:
        return 360 - inverse_tan

    # astr in 3 quadrant
    elif station.x > astr.x and station.y > astr.y:
        return 180 + inverse_tan

    # astr in 4 quadrant
    elif station.x < astr.x and station.y > astr.y:
        return 180 - inverse_tan

    else:
        return "ERROR"

# station class 
class Station:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# asteroid class 
class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # preset values 
        self.angle = 0
        self.station_distance = 0 
        self.rotation_num = 0

main()
