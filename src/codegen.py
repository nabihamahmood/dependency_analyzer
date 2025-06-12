import os
import subprocess
import networkx as nx
import pydot

# Generates a .dot and .png file from the given dependency graph
def generate_graph_image(graph, output_dir="output"):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    dot_path = os.path.join(output_dir, "dependencies.dot")  # Path to save .dot file
    png_path = os.path.join(output_dir, "dependencies.png")  # Path to save .png file

    try:
        # Convert the NetworkX graph to a pydot graph and save to .dot file
        pydot_graph = nx.nx_pydot.to_pydot(graph)
        pydot_graph.write_raw(dot_path)
        print(f"[✔] DOT file saved: {dot_path}")
    except Exception as e:
        print(f"[✘] Failed to write DOT file: {e}")
        return

    try:
        # Call Graphviz `dot` tool to convert .dot file to .png image
        subprocess.run(['dot', '-Tpng', dot_path, '-o', png_path], check=True)
        print(f"[✔] Dependency graph image generated: {png_path}")
    except Exception as e:
        print(f"[✘] Failed to generate PNG image: {e}")
