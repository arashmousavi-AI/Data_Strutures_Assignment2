def evaluate_prefix(expression):
    """Evaluating a valid prefix expression using two stacks."""

    # The value stack stores operands and intermediate calculation results.
    value_stack = []

    # The operator stack stores the current operators (+ or *).
    operator_stack = []

    # Split the input expression into separate tokens.
    tokens = expression.split()

    # Prefix expressions are evaluated from right to left.
    for token in reversed(tokens):
        if token.isdigit():
            value_stack.append(int(token))
        else:
            operator_stack.append(token)

            # Pop the two operands from the value stack.
            # Because we traverse right to left, the first popped value is the first operand of the operation.
            first_operand = value_stack.pop()
            second_operand = value_stack.pop()

            # Pop the operator that will be applied to the two operands.
            operator = operator_stack.pop()

            if operator == "+":
                result = first_operand + second_operand
            elif operator == "*":
                result = first_operand * second_operand


            # Push the intermediate result back onto the value stack so it can be used in a later calculation.
            value_stack.append(result)

    # After all tokens are processed, the only remaining value is the final result of the prefix expression.
    return value_stack.pop()


prefix_expression = input("Enter a prefix expression: ")
result = evaluate_prefix(prefix_expression)

print("result:", result)