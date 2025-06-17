def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}' to the shopping list. \n")
            
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            shopping_list.remove(item)
            print(f"Removed '{item}' from the shopping list. \n")
            if item not in shopping_list:
                print(f"Item '{item}' not found in the shopping list. \n")
        
        elif choice == '3':
            # Display the shopping list
            if len(shopping_list) == 0:
                print("Shopping list is empty. \n")
            else:
                print(shopping_list)
        
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()