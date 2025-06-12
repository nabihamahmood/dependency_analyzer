# main.py

from .analyzer import build_dependency_graph
from .codegen import generate_graph_image

def main():
    print(" Scanning: ../input")
    
    # Build the dependency graph from the input folder
    graph = build_dependency_graph("../input")

    # Print the number of nodes and edges in the graph
    print(f" Nodes: {graph.number_of_nodes()}, 📡 Edges: {graph.number_of_edges()}")

    # Generate the output graph image and DOT file
    generate_graph_image(graph, output_dir="../output1")

if __name__ == "__main__":
    main()
