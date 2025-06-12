import re

# Regex pattern to match #include directives in C files (both "file.h" and <file.h>)
INCLUDE_PATTERN = re.compile(r'#include\s+[<"]([^">]+)[">]')

# Valid file extensions to scan for dependencies
VALID_EXTENSIONS = ['.c', '.h']
