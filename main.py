import networkx as nx
import matplotlib.pyplot as plt
import fileinput
import numpy as np
import sys

from collections import Counter
# ** THIS METHOD IS SLOWER BUT MORE ACCURATE **
# this loop finds the element in the most cycles in the graph, and removes it until there are
# no more cycles
def remove_from_most_cycles(G):
    nodes_removed = []
    while True:
        breakLoop = True
        cycles = nx.simple_cycles(G)
        cycleList = []
        for l in cycles:
            cycleList.append(l)
            breakLoop=False
        if breakLoop:
            break
        flattened_list = [item for sublist in cycleList for item in sublist]
        counter = Counter(flattened_list)
        most_common_element, count = counter.most_common(1)[0]
        nodes_removed.append(most_common_element)
        G.remove_node(most_common_element)
    return nodes_removed

# ** THIS METHOD IS FASTER BUT LESS ACCURATE  **
def remove_high_degree_node(G):
    nodes_removed = []
    while True:
        # Check if the graph has cycles
        if nx.is_directed_acyclic_graph(G):
            break
        # Compute degrees
        degree_dict = G.degree()
        # Find node with the highest degree
        max_degree_node = max(degree_dict, key=lambda x: x[1])[0]
        # Remove the node with the highest degree
        nodes_removed.append(max_degree_node)
        G.remove_node(max_degree_node)
    return nodes_removed

# finds and returns the node with the highest "closeness centrality"
def get_most_close_node(G):
    nodes = G.nodes
    max_centrality = -1*np.inf
    most_central_node = None
    for n in nodes:
        clos_centr = nx.closeness_centrality(G, n)
        if clos_centr > max_centrality:
            max_centrality = clos_centr
            most_central_node = n
    return most_central_node

# finds and returns the node with the highest "betweenness centrality"
def get_most_between_node(G):
    centralities = nx.betweenness_centrality(G)
    max_value = max(centralities, key=centralities.get)
    return max_value

def generate_output(nodes_removed, output_filename):
    with open(output_filename, "w") as f:
        f.write(f"{len(nodes_removed)}\n")
        nodes_rem = [str(x) for x in nodes_removed]
        f.write(" ".join(nodes_rem))

def remove_to_acyclic_by_betweenness(G):
    nodes_removed = []
    while True:
        try:
            # Detect a cycle
            cycle = nx.find_cycle(G, orientation='original')
        except nx.NetworkXNoCycle:
            break  # Exit if the graph is acyclic
        
        # Calculate betweenness centrality of nodes in the detected cycle
        cycle_nodes = set(node for edge in cycle for node in edge[:2])
        centrality = nx.betweenness_centrality_subset(G, sources=cycle_nodes, targets=cycle_nodes)
        
        # Find the node with the highest centrality in the cycle
        node_to_remove = max(centrality, key=centrality.get)
        
        # Remove the node with the highest centrality
        G.remove_node(node_to_remove)
        nodes_removed.append(node_to_remove)
    
    return nodes_removed


if __name__ == "__main__":
    lines = []
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]  # New line to accept output filename as argument
    G = nx.DiGraph()
    with open(inputFileName, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip().split(" "))
    nodeCnt = int(lines[0][0])
    for i in range(nodeCnt):
        G.add_node(i+1)
    for i in range(1, nodeCnt+1):
        for start in lines[i][1:]:
            if start != '':
                G.add_edge(int(start), i)

    nodes_removed = remove_to_acyclic_by_betweenness(G) # CHANGE THIS LINE TO GO FROM SLOW TO FAST HEURISTIC AND VICE VERSA
    generate_output(nodes_removed, outputFileName)