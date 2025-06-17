from datetime import datetime, timedelta

def  display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date


def  calculate_future_date(future_date) -> datetime:
    return datetime.now() +  timedelta(days=int(future_date))


print(f"Current date and time: {display_current_datetime()}")
num_of_days = input("Enter the number of days to add to the current date: ")
print(f"Future date: {calculate_future_date(num_of_days).strftime("%Y-%m-%d %H:%M:%S")}")