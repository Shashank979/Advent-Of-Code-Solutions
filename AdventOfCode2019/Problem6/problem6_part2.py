import copy

# look for first object that both SAN and You meet if u went from SAN to COM and YOU to COM
# can make two lists of all objects SAN and Com meet (and have attribute which stores data of 
# how far from COM and attribute that stores how far from respective parter ) with and then find the one with smallest distance from COM 
# then just add distance from that object to San and that object to you 

# make inverse dict of all the objects
# then find san in dict and go recursively keep finding its parents and adding them to list
# do same for You 
# then create set of these objects based on there 

class Space_object:
    def __init__(self, object_id, distance_object = 0):
        self.object_id = object_id
        self.distance_object = distance_object


orbits = open('input_problem6.txt').read().splitlines()
inverse_dict = {}
counter = 0
san_list = []
you_list = []
for index, orbit in enumerate(orbits):
    parent = Space_object(orbit.split(")")[0])
    child = Space_object(orbit.split(")")[1])
    inverse_dict[child] = parent
    if child.object_id == "SAN":
        san = child
    elif child.object_id == "YOU":
        you = child


def main():
    get_parent(san, False)
    counter = 0
    clear_distances(inverse_dict)
    get_parent(you, True)

    for object1 in san_list:
        print(object1.object_id, ": ", object1.distance_object)

    print("------------------")
    for object1 in you_list:
        print(object1.object_id, ": ", object1.distance_object)
    
    overlapping_objects = []
    for object1 in san_list:
        for object2 in you_list:
            if object1.object_id == object2.object_id:
                overlapping_objects.append(object1.distance_object + object2.distance_object - 2)

    print(min(overlapping_objects))
    #for key, value in inverse_dict.items():
    #    print(key.distance_object)


def get_parent(child, you):

    global counter
    child_distance_object = child.distance_object

    for key in inverse_dict:
        if key.object_id == child.object_id:

            parent = inverse_dict[key]
            parent.distance_object = child_distance_object + 1
            
            if you:
                you_list.append(copy.deepcopy(parent))
            elif not you:
                san_list.append(copy.deepcopy(parent))
            get_parent(parent, you)

    return 


def clear_distances(my_dict):
    for key, value in my_dict.items():
        key.distance_object = 0
        value.distance_object = 0

def get_child(parent):
    global counter
    parent_distance_COM = parent.distance_COM
    children_list = []
    counter += parent_distance_COM

    for key in orbits_dict:
        if key.object_id == parent.object_id:
            child = orbits_dict[key]
            child.distance_COM = parent_distance_COM + 1
            children_list.append(child)

    if len(children_list) == 0:
        return 

    for child in children_list:
        get_child(child)


main()
