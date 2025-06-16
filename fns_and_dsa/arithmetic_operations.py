#defining a function to perform arthimetic operations.
def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero."
            else:
                return num1 / num2
        case "multiply":
            return num1 * num2
        case _:
            print("Invalid inputs")