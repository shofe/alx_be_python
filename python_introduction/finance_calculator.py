#Asking user for their monthly incone
monthly_income = int(input("Enter your monthly income: "))

#Asking user for their total monthly expenses
total_monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculating the monthly savings by subtracting monthly expenses from monthly income
monthly_savings = monthly_income - total_monthly_expenses

# Projected savings for one year
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Displaying the results
print(f"Your monthly savings are ${monthly_savings}")
print(f"projected savings after one year, with interest, is: ${int(projected_savings)}")
