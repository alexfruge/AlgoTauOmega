import networkx as nx
import sys

def build_graph_from_input(input_file):
    G = nx.DiGraph()
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = [line.strip().split(" ") for line in file]
    nodeCnt = int(lines[0][0])
    for i in range(1, len(lines)):
        for edge in lines[i][1:]:
            if edge:
                G.add_edge(int(lines[i][0]), int(edge))
    return G

def remove_nodes_from_processed_file(G, processed_file):
    with open(processed_file, 'r', encoding='utf-8') as file:
        next(file)  # Skip the first line
        nodes_to_remove = [int(node) for line in file for node in line.strip().split(" ")]
    G.remove_nodes_from(nodes_to_remove)

def main(input_file, processed_file):
    G = build_graph_from_input(input_file)
    remove_nodes_from_processed_file(G, processed_file)
    is_dag = nx.is_directed_acyclic_graph(G)
    print("DAG" if is_dag else "Not DAG")

if __name__ == "__main__":
    input_file = sys.argv[1]
    processed_file = sys.argv[2]
    main(input_file, processed_file)
