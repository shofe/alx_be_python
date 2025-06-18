#creating a variable for the formula.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    if type(fahrenheit) != int:
        print("Invaid input type")
    else:
        return  (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    if type(celsius) != int:
        print("Invaid input type")
    else:
        return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 

msg_1 = int(input("Enter the temperature to convert: "))
temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temp.lower().strip("") == "c":
    print(f"{temp} is {convert_to_fahrenheit(msg_1)} F")
elif temp.lower().strip("") == "f":
    print(f"{temp} is {convert_to_celsius(msg_1)} C")
else:
    print("You have entered an invalid request")
