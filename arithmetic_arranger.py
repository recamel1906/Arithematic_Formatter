def arithmetic_arranger(problems, showResults=False):
    # check to see if list of problems doesn't exceed 5 elements
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        pass

    arranged_problems = None
    for problem in problems:
        # split each item in problems by lists of operands and operations
        firstOperand = problem.split()[0]
        operation = problem.split()[1]
        secondOperand = problem.split()[2]

        # check to see if operations only contains "+" or "-"
        if operation == '*' or operation == '/':
            return "Error: Operator must be '+' or '-'."
        else:
            pass

        # check to see if each element in firstOperand and secondOperand is an integer
        isNumericBoolean = any(c.isnumeric() for c in firstOperand) or \
                           any(c.isnumeric() for c in secondOperand)
        if not isNumericBoolean:
            return "Error: Numbers must only contain digits."
        else:
            pass

        # check to see if length of each element in firstOperand and secondOperand <= 4
        if len(firstOperand) > 4 or len(secondOperand) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            pass

        # Set up lines to print
        separationWidth = max(len(firstOperand), len(secondOperand)) + 2
        first_line = str(firstOperand.rjust(separationWidth - 1))
        second_line = str(operation + secondOperand.rjust(separationWidth))
        third_line = str("-" * separationWidth)
        fourth_line = str(eval(problem))

        first_line += "    " + '\n'
        second_line += "    " + '\n'
        third_line += "    " + '\n'
        fourth_line += "    " + '\n'
        arranged_problems = first_line + second_line + third_line + fourth_line
    return arranged_problems
