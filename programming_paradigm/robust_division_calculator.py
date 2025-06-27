def safe_divide(numerator, denominator):     #Defining a function that has the numerator and denominator arguments
    try:
        numerator = float(numerator)

        denominator = float(denominator)

        if denominator == 0:

            return ("Error: Cannot divide by zero.")
    
        else:

            answer = numerator / denominator

            return f"The result of the division is {answer}"

    except ValueError:

        return f"Error: Please enter numeric values only."


    





