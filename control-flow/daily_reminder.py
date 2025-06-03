# Task Reminder System

# Step 1: Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process the task based on priority using Match Case
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
        
        # Check if time-bound for high priority
        if time_bound == "yes":
            print(f"Reminder: {base_message} that requires immediate attention today!")
        else:
            print(f"Reminder: {base_message}. Please prioritize this task.")
    
    case "medium":
        base_message = f"'{task}' is a medium priority task"
        
        # Check if time-bound for medium priority
        if time_bound == "yes":
            print(f"Reminder: {base_message} that requires immediate attention today!")
        else:
            print(f"Note: {base_message}. Complete when possible.")
    
    case "low":
        base_message = f"'{task}' is a low priority task"
        
        # Check if time-bound for low priority
        if time_bound == "yes":
            print(f"Reminder: {base_message} that requires immediate attention today!")
        else:
            print(f"Note: {base_message}. Consider completing it when you have free time.")
    
    case _:
        print("Invalid priority level. Please use high, medium, or low.")