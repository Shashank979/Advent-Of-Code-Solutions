# final answer for part 1 was 269 
# and the coordinates of the astr were (13, 17)

def main():
    # variabes 
    asteroids = []
    max_astr_seen = 0 
    max_astr = ()  # y value is flipped negative so it works with real x y graph 

    map = open('input_problem10.txt').read().splitlines()

    # creation of list of asteroid coordinates (in tuple form)
    for row_index, row in enumerate(map):
        for column_index, column in enumerate(row):
            if map[row_index][column_index] == "#":
                asteroids.append(Asteroid(column_index, -row_index))

    # iterates through asteroids 
    for asteroid in asteroids:
        slopes = set()
        # iterates throuhg every astr except variable asteroid 
        for comparison_astr in asteroids:
            if asteroid.x != comparison_astr.x or asteroid.y != comparison_astr.y:
                # adds slope data to set of slopes data 
                slopes.add(calc_slope(asteroid, comparison_astr))
        # if number of asteroids detected is greater than previous max
        if len(slopes) > max_astr_seen:
            max_astr_seen = len(slopes)
            max_astr = asteroid


    print('\n', "(" + str(max_astr.x) +  "," + str(max_astr.y) + ")")  # asteroids coordinates 
    print(max_astr_seen)  # number of asteroids seen 


# returns the slope data between two different asteroids 
def calc_slope(astr1, astr2):
    """
    Calculates slope + (ast2 location relative to ast1) which is returned as one value 
    """

    # calculates slope data 
    try:
        calc_slope = (astr1.y - astr2.y) / (astr1.x - astr2.x)  # slope calculated 
        # accounting for slope 0
        # slope == 0 and astr2 is left of astr1
        if astr2.y - astr1.y == 0 and astr1.x > astr2.x:
            calc_slope = "left_0"
            return calc_slope
        # slope == 0 and astr2 is right of astr1
        elif astr2.y - astr1.y == 0 and astr1.x < astr2.x:
            calc_slope = "right_0"
            return calc_slope

        # above 
        if astr1.y < astr2.y:
            return "above_" + str(calc_slope) 
        # below 
        elif astr1.y > astr2.y:
            return "below_" + str(calc_slope) 

    # accounting for if x2 - x1 == 0
    except ZeroDivisionError: 
        # below 
        if astr1.y - astr2.y > 0:
            calc_slope = "below_infinity"
        # above 
        elif astr1.y - astr2.y < 0:
            calc_slope = "above_infinity"

    return calc_slope


# asteroid class to store x y data for the asteroids 
class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


main()