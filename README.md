# Solver Project

This project contains a set of Python scripts designed to solve and simplify mathematical equations using the Z3 theorem prover. The project includes various utilities for equation conversion, simplification, and visualization.

## Table of Contents

- [Introduction](#introduction)
- [Scripts Overview](#scripts-overview)
  - [inf2Pre.py](#inf2prepy)
  - [simplify.py](#simplifypy)
  - [generalSimplify.py](#generalsimplifypy)
  - [solver.py](#solverpy)
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

## Usage

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

