# run.py 

from src.analyzer import build_dependency_graph
from src.codegen import generate_graph_image

def run_analysis(input_dir, output_dir):
    print(f"\n Analyzing: {input_dir}")
    graph = build_dependency_graph(input_dir)
    print(f" Nodes: {graph.number_of_nodes()}, Edges: {graph.number_of_edges()}")
    generate_graph_image(graph, output_dir=output_dir)

if __name__ == "__main__":
    run_analysis("input", "output1")
    run_analysis("input2", "output2")
