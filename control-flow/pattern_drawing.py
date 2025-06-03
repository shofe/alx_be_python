#Creating a count for the user.
row = 0

#Asking user for pattern size.
user_size = int(input("Enter the size of the pattern: "))

#Using thw while loop to print the pattern.
while row < user_size:
    for column in range(user_size):
        print("*" , end = "")
    print()  #Moves to the next line after printing.
    row +=1 #increases the row size

