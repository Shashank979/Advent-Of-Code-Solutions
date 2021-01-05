

class Space_object:
    def __init__(self, object_id, distance_COM = 0):
        self.distance_COM = distance_COM
        self.object_id = object_id

orbits = open('test_input_problem6.txt').read().splitlines()
orbits_dict = {}
counter = 0
for index, orbit in enumerate(orbits):
    parent = Space_object(orbit.split(")")[0])
    child = Space_object(orbit.split(")")[1])
    orbits_dict[parent] = child
    if parent.object_id == "COM":
        com_child = orbits_dict[parent]
        com_child.distance_COM = 1 



def main():
    get_child(com_child)
    print(counter)

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