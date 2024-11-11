# Define the MathExpression class using Object-Oriented Programming
class MathExpression:
    def __init__(self, expression):
        # Initialize with the given expression
        self.expression = expression

    def evaluate(self):
        # Evaluate the expression and return the result
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error evaluating expression: {e}"

    def print_result(self):
        # Print the result of the evaluated expression
        result = self.evaluate()
        print(f"The result of the expression '{self.expression}' is: {result}")


# Example usage of the MathExpression class
expression = "3 * (2 + 5) - 4 / 2"  # The expression to solve

# Create a MathExpression object
math_expr = MathExpression(expression)

# Print the result of the expression
math_expr.print_result()
