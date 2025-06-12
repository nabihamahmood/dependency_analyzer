import os
import re

INCLUDE_REGEX = r'#include\s*["<](.*?)[">]'

def extract_includes(file_path):
    """
    Extracts all #include filenames from a C source/header file.
    """
    includes = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(INCLUDE_REGEX, line)
                if match:
                    includes.append(match.group(1))
    except Exception as e:
        print(f"[!] Error reading {file_path}: {e}")
    return includes

def resolve_include_path(include_name, current_dir, root_dir):
    """
    Attempts to resolve the include file path relative to current_dir and root_dir.
    Returns the relative path if found, else None.
    """
    # Check relative to current directory
    possible_path = os.path.normpath(os.path.join(current_dir, include_name))
    if os.path.isfile(possible_path):
        return os.path.relpath(possible_path, root_dir)

    # Check relative to root input directory
    possible_path = os.path.normpath(os.path.join(root_dir, include_name))
    if os.path.isfile(possible_path):
        return os.path.relpath(possible_path, root_dir)

    # Could not resolve locally (likely system header)
    return None
