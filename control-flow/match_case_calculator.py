#Asking user to input number.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Asking which operation user will like to use.
operation = input("Choose the operation (+, -, *, /): ")

#Using match case for the operation
match operation:
    case "+":
        result = num1 + num2
        
    case "-":
        result = num1 - num2
        
    case " /":
        result = num1 / num2
       
    case "*":
        result = num1 * num2
        
    case _:
        print("Cannot divide by zero.")
print(f"The result is {result}.")