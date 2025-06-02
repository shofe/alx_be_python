#Asking user for input on their weather condition
user_input = input("What is the weather like today? (sunny/rainy/cold) ")

#Using user"s input to give advice by implementig IF statements.
if user_input == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_input =="rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_input == "cold": 
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
