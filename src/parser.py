# parser.py
from .lexer import tokenize_line

def parse_includes(file_path):
    """
    Parses a C file and returns a list of all included filenames.

    Args:
        file_path (str): Path to the C source/header file to be parsed.

    Returns:
        List[str]: A list of all includes found (e.g., "utils/logger.h").
    """
    includes = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                token = tokenize_line(line)  # Apply lexical analysis to each line
                if token:
                    includes.append(token)  # Add matched token to list
    except Exception as e:
        print(f"[!] Error reading {file_path}: {e}")

    return includes
