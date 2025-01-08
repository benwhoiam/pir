# Solver Project

This project contains a set of Python scripts designed to solve and simplify mathematical equations using the Z3 theorem prover. The project includes various utilities for equation conversion, simplification, and visualization.

## Table of Contents

- [Introduction](#introduction)
- [Scripts Overview](#scripts-overview)
  - [inf2Pre.py](#inf2prepy)
  - [simplify.py](#simplifypy)
  - [generalSimplify.py](#generalsimplifypy)
  - [solver.py](#solverpy)
- [Equations](#equations)
  - [Original Equations](#original-equations)
  - [Pre-transformed Equations](#pre-transformed-equations)
- [Usage](#usage)
  - [Dependencies](#dependencies)
  - [Running the Scripts](#running-the-scripts)
- [Files](#files)
- [License](#license)

## Introduction

This project aims to provide tools for solving and simplifying mathematical equations using the Z3 theorem prover. The project includes scripts for converting equations to prefix notation, simplifying equations, and visualizing solutions.

## Scripts Overview

### inf2Pre.py

This script converts infix equations to prefix notation. This conversion is necessary for the Z3 solver to process the equations correctly.

#### Key Functions:
- `convert_to_prefix(node)`: Converts an AST node into a prefix notation string.
- `preprocess_expression(expression)`: Preprocesses the input expression to replace certain symbols and terms for compatibility.
- `check_input()`: Checks the input for validity.
- `read_file()`: Reads the input file containing the equation.
- `write_file(prefix_expression)`: Writes the prefix notation to an output file.

### simplify.py

This script simplifies equations using the Z3 theorem prover.

#### Key Functions:
- `get_equation()`: Reads the equation from the input file and processes command line arguments.
- `onlyTheseEquations(result)`: Simplifies the result by removing specific patterns and replacing them with more readable forms.
- `betterNextline(long)`: Formats the long string by adding new lines for better readability.

### generalSimplify.py

This script provides a general simplification of equations to a more readable form.

#### Key Functions:
- `get_equation()`: Reads the equation from the input file and processes command line arguments.
- `onlyTheseEquations(result)`: Simplifies the result by removing specific patterns and replacing them with more readable forms.
- `betterNextline(long)`: Formats the long string by adding new lines for better readability.

### solver.py

This script solves equations using the Z3 theorem prover and visualizes the solutions.

#### Key Functions:
- `sin(x)`: Custom sine function using Taylor series expansion.
- `cos(x)`: Custom cosine function using Taylor series expansion.
- `get_equation()`: Reads the equation from the input file and processes command line arguments.
- `get_solutions(s)`: Generator function to obtain multiple solutions from the Z3 solver.
- `apply_step_constraints(s)`: Applies step constraints to the solver for Range and bearing.
- `Floats(s)`: Converts Z3 decimal to float.
- `show_graph(solutions)`: Displays a graph of the solutions.

## Equations

### Original Equations

The `original_equations` folder contains the equations that were provided at the start of the project. These equations are in their original form and have not been modified.

### Pre-transformed Equations

The `equations` folder contains the pre-transformed equations that have been processed using the `inf2Pre.py` script. This allows users to directly use these equations without having to convert them again.

### Manual Changes

The file [e4m.txt](#file:e4m.txt-context) have had manual change made to an original equation. The original equation in [e4.txt](#file:e4.txt-context) did not follow the form `sqrt(A) < B`, so it was manually modified to create [e4m.txt](#file:e4m.txt-1-context).
The file [e1.txt](#file:e1.txt-context) was negated to give example of unsat negation.
## Usage
All Python scripts support the `-h` and `--help` options to display usage information and available command-line arguments.
### Dependencies

The project requires the following Python packages:
- z3-solver
- termcolor
- matplotlib

You can install these dependencies using pip:
```sh
pip install -r requirements.txt
```

### Running the Scripts

#### Equation Conversion

To convert an equation from infix to prefix notation, use the following command:

```sh
python inf2Pre.py <input_file> <output_file>
```

Example:

```sh
python inf2Pre.py original_equations/e8.txt equations/e8t
```
#### Solving the Equation

To solve an equation and visualize the solutions, use the following command:

```sh
python solver.py <input_file> [<current_range> <level>]
```

Example:

```sh
python solver.py equations/e8t 6 4
```

#### Equation Simplification

To simplify an equation, use the following command:

```sh
python simplify.py <input_file> [<current_range> <level>]
```

Example:

```sh
python simplify.py equations/e8t 6 4
```

#### General Equation Simplification

For general simplification of an equation, use the following command:

```sh
python generalSimplify.py <input_file>
```

Example:

```sh
python generalSimplify.py equations/e8t
```

### Additional Information

For more details on the usage and functionality of each script, refer to the inline documentation within the scripts themselves. Each script includes comments and docstrings that explain the purpose and usage of functions and variables.


