#Asking a user for input
num = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate from 1 to 10
for i in range(1, 11):
    product = num * i
    print(f"{num} * {i} = {product}")

