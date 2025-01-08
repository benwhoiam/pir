from z3 import *
from termcolor import colored
import matplotlib.pyplot as plt
import sys
import math
import os
import time

# Start timer
start_time = time.time()

# Initialize Z3 solver
s = Solver()

# Constants -------------------------------------
RANGE_MIN = 0
RANGE_MAX = 10
RANGE_STEP = 0.4
BEARING_MIN = -180
BEARING_MAX = 180
BEARING_STEP = 8
PRECISION = 5
current_Range = 0
level = 0

# Variables -------------------------------------
Range = Real('Range')
bearing = Real('bearing')

# Taylor Approx ---------------------------------
def sin(x):
    """
    Custom sine function to avoid confusion with math.sin.
    Uses Taylor series expansion for sine calculation.
    """
    global PRECISION
    x = (bearing * 3.14159) / 180.0
    term = 0
    sign = -1
    for i in range(1, PRECISION * 2, 2):
        sign *= -1
        term += sign * ((x) ** i) / math.factorial(i)
    return term

def cos(x):
    """
    Custom cosine function to avoid confusion with math.cos.
    Uses Taylor series expansion for cosine calculation.
    """
    global PRECISION
    x = (bearing * 3.14159) / 180.0
    term = 1
    sign = 1
    for i in range(2, PRECISION * 2, 2):
        sign *= -1
        term += sign * ((x) ** i) / math.factorial(i)
    return term

def get_equation():
    """
    Reads the equation from the input file and processes command line arguments.
    Returns the evaluated equation.
    """
    if len(sys.argv) < 2 or len(sys.argv) > 4 or sys.argv[1] in ("-h", "--help"):
        print("\nUsage:")
        print("\tpython solver.py <input_file> [<current_range> <level>]")
        print("\nArguments:")
        print("\t<input_file>:  Path to the input file containing a single-line equation.")
        print("\t<current_range> (optional):  Initial value for the range (e.g., 0).")
        print("\t<level> (optional):  Level value (e.g., 1).")
        print("\nExample:")
        print("\tpython solver.py equation.txt 5 2")
        print("\tpython solver.py equation.txt")
        sys.exit(1)

    expression = ""
    with open(sys.argv[1]) as f:
        expression = f.read().strip()
        if '\n' in expression:
            print(colored("\n\tError: The input file must contain a single-line equation.\n", 'red'))
            sys.exit(1)

    global current_Range, level
    if len(sys.argv) == 3:
        current_Range = float(sys.argv[2])
        level = float(input(colored("Level \t\t: ", 'cyan')))
    elif len(sys.argv) == 4:
        current_Range = float(sys.argv[2])
        level = float(sys.argv[3])
    else:
        current_Range = float(input(colored("Current Range\t: ", 'cyan')))
        level = float(input(colored("Level \t\t: ", 'cyan')))

    print(colored("Equation \t: ", 'cyan'), expression, end=2 * '\n')
    return eval(expression)

def get_solutions(s: z3.z3.Solver):
    """
    Generator function to obtain multiple solutions from the Z3 solver.
    Yields each solution found.
    """
    result = s.check()
    color = "green" if str(result) == 'sat' else "red"
    print(colored(f"> Check: {result}", color))
    # While we still get solutions
    while result == z3.sat:
        m = s.model()
        yield m
        # Add new solution as a constraint
        block = []
        for var in m:
            block.append(var() != m[var])
        s.add(z3.Or(block))
        # Look for new solution
        result = s.check()

def apply_step_constraints(s):
    """
    Applies step constraints to the solver for Range and bearing.
    """
    steps_range = [RANGE_MIN + i * RANGE_STEP for i in range(int((RANGE_MAX - RANGE_MIN) / RANGE_STEP) + 1)]
    steps_bearing = [BEARING_MIN + i * BEARING_STEP for i in range(int((BEARING_MAX - BEARING_MIN) / BEARING_STEP) + 1)]
    s.add(Or([Range == r for r in steps_range]))
    s.add(Or([bearing == b for b in steps_bearing]))

def Floats(s):
    """
    Converts Z3 decimal to float.
    """
    a = s.as_decimal(4)
    try:
        return float(a)
    except:
        return float(a.replace("?", ""))

def show_graph(solutions):
    """
    Displays a graph of the solutions.
    """
    plt.figure(figsize=(8, 5))
    plt.ylim(RANGE_MIN, RANGE_MAX)
    plt.xlim(BEARING_MIN, BEARING_MAX)
    plt.gca().set_facecolor('#dd3628')
    plt.title('Solutions Visualization')
    plt.ylabel('Range')
    plt.xlabel('Bearing')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')

    for indx, s in enumerate(solutions):
        plt.plot(Floats(s[bearing]), Floats(s[Range]), marker='o', color='#85fa50', markersize=14)
        if indx == 0:
            print(colored("\n> Plotting ", 'yellow'), end="", flush=True)
        if indx % 100 == 0:
            print(colored(".", 'yellow'), flush=True, end="")

    plt.show()

# Main function ---------------------------------
def main():
    """
    Main function to execute the solver and display results.
    """
    EQUATION = get_equation()
    s.add(EQUATION,
          bearing <= BEARING_MAX,
          bearing >= BEARING_MIN,
          Range <= RANGE_MAX,
          Range >= RANGE_MIN,
          )

    apply_step_constraints(s)
    solutions = get_solutions(s)

    show_graph(solutions)
    print("\n--- %s seconds ---" % (time.time() - start_time))

# Entry point -----------------------------------
if __name__ == '__main__':
    os.system('cls')
    main()