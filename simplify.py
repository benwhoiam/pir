from z3 import *
import sys
from termcolor import colored
import os
import re

# Constants -------------------------------------
current_Range = 6
level = 4
sin = Function('sin', RealSort(), RealSort())
cos = Function('cos', RealSort(), RealSort())

# Variables -------------------------------------
Range = Real('Range')
bearing = Real('bearing')

def get_equation():
    """
    Reads the equation from the input file and processes command line arguments.
    Returns the evaluated equation.
    """
    if len(sys.argv) < 2 or len(sys.argv) > 4 or sys.argv[1] in ("-h", "--help"):
        print("\nUsage:")
        print("\tpython simplify.py <input_file> [<current_range> <level>]")
        print("\nArguments:")
        print("\t<input_file>:  Path to the input file containing a single-line equation.")
        print("\t<current_range> (optional):  Initial value for the range (e.g., 0).")
        print("\t<level> (optional):  Level value (e.g., 1).")
        print("\nExample:")
        print("\tpython simplify.py equation.txt 6 4")
        print("\tpython simplify.py equation.txt")
        sys.exit(1)

    expression = ""
    # Read the equation from the input file
    with open(sys.argv[1]) as f:
        expression = f.read().strip()
        if '\n' in expression:
            print(colored("\n\tError: The input file must contain a single-line equation.\n", 'red'))
            sys.exit(1)

    global current_Range, level
    # Process command line arguments
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

def onlyTheseEquations(result):
    """
    Simplifies the result by removing specific patterns and replacing them with more readable forms.
    """
    result = result.replace("314159/18000000*", "")
    result = re.sub(r'If\(bearing <= 0,\s*bearing >= -90,\s*bearing <= 90\)', '|bearing|<=90', result)
    if "145/2" in result:
        result = result.replace("145/2", "β") + '\n\nAvec β = 145/2'
    return '\n' + result

def betterNextline(long):
    """
    Formats the long string by adding new lines for better readability.
    """
    long = long.split('\n')
    result = ''
    for i in range(len(long)):
        if not long[i-1][-1] == ',':
            long[i] = long[i].strip()
        else:
            long[i] = '\n' + long[i]
        result += long[i]
    return result

# Main function ---------------------------------
def main():
    """
    Main function to execute the simplification process and display results.
    """
    EQUATION = get_equation()
    s = str(simplify(EQUATION))
    print(colored("Simplified correct\t: ", 'cyan'), colored(s, 'light_magenta'))
    s = betterNextline(s)
    s = onlyTheseEquations(s)
    print(colored("\n\nSimplified readable\t: ", 'cyan'), colored(s, 'green'))

# Entry point -----------------------------------
if __name__ == '__main__':
    os.system('cls')
    print(colored("\n-> START\n", 'dark_grey'))
    main()
    print(colored("\n\n-> END\n", 'dark_grey'))