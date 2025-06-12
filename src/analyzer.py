# analyzer.py

import os
import networkx as nx
from .constants import VALID_EXTENSIONS
from .parser import parse_includes               # Syntax analysis module
from .semantic import resolve_include_path      # Semantic analysis module

def build_dependency_graph(input_dir):
    """
    Walks through all .c and .h files in the given input directory,
    builds a directed dependency graph based on #include directives.

    Args:
        input_dir (str): Path to the root input directory (e.g., 'input/' or 'input2/').

    Returns:
        networkx.DiGraph: The constructed graph with files as nodes and includes as edges.
    """
    graph = nx.DiGraph()  # Directed graph to represent include dependencies

    # Traverse all directories and files within the input directory
    for root, _, files in os.walk(input_dir):
        for filename in files:
            # Only process valid extensions (e.g., .c, .h)
            if any(filename.endswith(ext) for ext in VALID_EXTENSIONS):
                filepath = os.path.join(root, filename)           # Absolute path to the file
                file_key = os.path.relpath(filepath, input_dir)   # Node key relative to project root

                graph.add_node(file_key)  # Add this file as a node in the graph

                # -------- Phase 1 & 2: Lex + Parse --------
                includes = parse_includes(filepath)  # Extract include directives

                # -------- Phase 3: Semantic Resolution --------
                for include in includes:
                    included_path = resolve_include_path(include, root, input_dir)
                    if included_path:
                        graph.add_edge(file_key, included_path)  # Create edge: file → included file
                        print(f"→ {file_key} includes {included_path}")

    return graph
