import networkx as nx
import matplotlib.pyplot as plt
#import networkx as nx.path


def main():
    bag_types = set([])
    bags_sg = set([])
    G = nx.DiGraph()
    file1 = 'test_input_problem7.txt'
    input_file = open(file1).read().splitlines()
    for line in input_file:
        # parsing 
        line = line.split("contain")
        second_part = [x.strip().replace(".", "").replace("bags", "bag") for x in line[1].split(",")]
        second_part = [(x.split(" ")[0], x[x.find(" ") + 1: len(x)]) for x in second_part]
        first_part = line[0].replace("bags", "bag").strip()
        #print(first_part, "", second_part)
        bag_types.add(first_part)
        # making graph 
        for bag in second_part:
            if bag[0] != "no":
                bag_types.add(bag[1])
                G.add_edge(first_part, bag[1], weight = int(bag[0]))
    #print(G.edges)
    #print(nx.bellman_ford_path(G, "light red bag", "shiny gold bag"))

    # -------
    # part1 solution 
    #print(bags_sg)
    #print(len(nx.ancestors(G, "shiny gold bag")))
    # -------


    #print(len(bags_sg))
    #print(list(nx.bfs_edges(G, "shiny gold bag")))
    print(count_inside_bags(G, "shiny gold bag"))
    #print(nx.descendants(G, "shiny gold bag"))

def count_inside_bags(graph, top):

    counter = 0
    for bag, value in graph[top].items():
        #print(bag, value['weight'])
        counter += value['weight'] * count_inside_bags(graph, bag) + value['weight']
    print(top, counter)
    return counter

main()
