# lexer.py
import re
from .constants import INCLUDE_PATTERN

def tokenize_line(line):
    """
    Lexical analyzer for a single line of C code.

    Args:
        line (str): A line from a C source or header file.

    Returns:
        str | None: The included filename if matched, otherwise None.
    """
    match = INCLUDE_PATTERN.search(line)  # Search for pattern like #include "..." or <...>
    if match:
        return match.group(1)  # Extract just the filename (e.g., utils/math.h)
    return None  # No valid include directive in this line
