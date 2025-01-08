import ast
import sys

# Dictionary mapping AST nodes to their corresponding operator representations.
operators = {
    ast.And: 'And',  # Logical AND operator
    ast.Or: 'Or',   # Logical OR operator
    ast.Invert: 'Not',  # Unary NOT operator
    ast.LtE: '<=',  # Less than or equal to
    ast.Eq: '==',   # Equality
    ast.Lt: '<',    # Less than
    ast.Sub: '-',   # Subtraction
    ast.Add: '+',   # Addition
    ast.Mult: '*',  # Multiplication
    ast.Div: '/',   # Division
    ast.Pow: '**',  # Exponentiation
}

def convert_to_prefix(node):
    """
    Converts an AST node into a prefix notation string.
    
    Args:
        node (ast.AST): The AST node to convert.

    Returns:
        str: The prefix representation of the expression.
    """
    if isinstance(node, ast.BinOp):  # Handle binary operations (e.g., +, -, *)
        op = operators[type(node.op)]
        if type(node.op) in (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow):  # Arithmetic operations
            return f"({convert_to_prefix(node.left)} {op} {convert_to_prefix(node.right)})"
    elif isinstance(node, ast.BoolOp):  # Handle logical operations (e.g., AND, OR)
        op = operators[type(node.op)]
        values = [convert_to_prefix(value) for value in node.values]
        return f"{op}({', '.join(values)})"
    elif isinstance(node, ast.UnaryOp):  # Handle unary operations (e.g., NOT)
        op = operators[type(node.op)]
        return f"{op}({convert_to_prefix(node.operand)})"
    elif isinstance(node, ast.Compare):  # Handle comparisons (e.g., <=, ==)
        left = convert_to_prefix(node.left)
        comparisons = " ".join(
            f"{operators[type(op)]} {convert_to_prefix(comp)}"
            for op, comp in zip(node.ops, node.comparators)
        )
        return f"({left} {comparisons})"
    elif isinstance(node, ast.Constant):  # Handle constant values (e.g., numbers, strings)
        return str(node.value)
    elif isinstance(node, ast.Name):  # Handle variable names
        return node.id
    elif isinstance(node, ast.Call):  # Handle function calls (e.g., abs(x))
        func_name = convert_to_prefix(node.func)
        args = ', '.join(convert_to_prefix(arg) for arg in node.args)
        return f"{func_name}({args})"
    else:
        raise ValueError(f"Unsupported node type: {type(node)}")

def preprocess_expression(expression):
    """
    Preprocess the input expression to replace certain symbols and terms for compatibility, This is a Case-specific replacements, replace the code blow with the replacements depending on your need.

    Args:
        expression (str): The input expression as a string.

    Returns:
        str: The preprocessed expression.
    """
    expression = expression.replace('&', ' and ').replace('|', ' or ').replace('^', '**')
    expression = expression.replace('false', 'False').replace('true', 'True').replace('range', 'Range')
    # This part is only useful for our very niche  usecase.
    expression = expression.replace("300", "90000").replace("285", "81225").replace("sqrt", "")
    return expression

def check_input():
    """
    Validate the input arguments and provide usage instructions if invalid.
    """
    if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
        print("\nUsage:")
        print("\tpython inf2Pre.py <input_file> <output_file>")
        print("\nArguments:")
        print("\t<input_file>:  Path to the input file containing a single-line equation.")
        print("\t<output_file>: Path to the output file to store the result.")
        print("\nExample:")
        print("\tpython script.py input.txt output.txt")
        sys.exit(1)

def read_file():
    """
    Read the input file and validate its content.

    Returns:
        str: The expression from the file.
    """
    with open(sys.argv[1]) as f:
        expression = f.read().strip()
        if '\n' in expression:
            print("\n\tError: The input file must contain a single-line equation.\n")
            sys.exit(1)
        return expression

def write_file(prefix_expression):
    """
    Write the converted prefix expression to the output file.

    Args:
        prefix_expression (str): The prefix expression to write.
    """
    output = sys.argv[2] 
    with open(output, "w") as f:
        f.write(prefix_expression)
        print(f"\n\tOutput written to: {output}\n")

def main():
    """
    Main function to handle the script workflow.
    """
    check_input()  # Validate input arguments
    expression = read_file()  # Read the input expression from the file
    expression = preprocess_expression(expression)  # Preprocess the expression
    parsed_expr = ast.parse(expression, mode='eval')  # Parse the expression into an AST
    prefix_expression = convert_to_prefix(parsed_expr.body).replace('abs', 'Abs')  # Convert to prefix notation
    write_file(prefix_expression)  # Write the output to a file

if __name__ == '__main__':
    main()
