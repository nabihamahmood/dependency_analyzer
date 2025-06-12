# semantics.py
import os

def resolve_include_path(include_name, current_dir, root_dir):
    """
    Resolves the relative path of an included file, simulating semantic analysis.

    Args:
        include_name (str): The filename extracted from #include.
        current_dir (str): The directory of the file that includes it.
        root_dir (str): The root directory of the entire input project.

    Returns:
        str | None: A relative path if found, or None if not resolvable (e.g., system headers).
    """
    # Try relative to the current file's directory
    possible_path = os.path.normpath(os.path.join(current_dir, include_name))
    if os.path.isfile(possible_path):
        return os.path.relpath(possible_path, root_dir)

    # Try relative to the root of the input project
    possible_path = os.path.normpath(os.path.join(root_dir, include_name))
    if os.path.isfile(possible_path):
        return os.path.relpath(possible_path, root_dir)

    # If not found, it's likely a system header like <stdio.h>
    return None
