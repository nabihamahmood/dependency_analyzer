#  Dependency Analyzer – Compiler Construction Project

This project is a **C file dependency analyzer** developed for a Compiler Construction course. It simulates the **front-end phases of a compiler** — Lexical Analysis, Syntax Analysis, Semantic Analysis, and Code Generation — by analyzing `#include` directives in C `.c` and `.h` source files.

It constructs a **directed graph** representing file include relationships and generates both `.dot` and `.png` files using Graphviz.

---

##  Project Structure

```

dependency-analyzer/
├── input/        → Test case 1: simple C program
├── input2/       → Test case 2: nested includes
├── output1/      → Output graph from input/
├── output2/      → Output graph from input2/
├── src/
│   ├── lexer.py
│   ├── parser.py
│   ├── semantics.py
│   ├── analyzer.py
│   ├── codegen.py
│   ├── constants.py
│   └── main.py
├── run.py
├── README.md
├── requirements.txt

````

---

##  Compiler Phases Simulated

| Phase             | Module           | Description |
|------------------|------------------|-------------|
| Lexical Analysis | `lexer.py`       | Extracts `#include` directives using regex |
| Syntax Analysis  | `parser.py`      | Parses tokens into structured include lists |
| Semantic Analysis| `semantics.py`   | Resolves include file paths on disk |
| Code Generation  | `codegen.py`     | Generates `.dot` and `.png` from the graph |
| Integration      | `analyzer.py`    | Combines all phases to build the graph |

---

##  How to Run

### 1. Install dependencies:
```bash
pip install -r requirements.txt
````

### 2. Run analysis:

```bash
python run.py
```

### Output:

* `output1/`: Graph for `input/`
* `output2/`: Graph for `input2/`

---
##  Features

* Handles nested folder includes
* Skips system headers like `<stdio.h>`
* Visualizes dependencies using DOT and PNG
* Follows compiler front-end structure

---

##  Requirements

* Python 3.8 or higher
* Graphviz (must be installed and added to PATH)
* Required packages:

  ```
  networkx
  pydot
  graphviz
  ```

---
