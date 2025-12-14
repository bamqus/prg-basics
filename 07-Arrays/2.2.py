# The data below represents monthly expenses divided into categories and weeks. 
# Write a program that calculates and prints:

# total expenses for each category
# total expenses for each week
# total expenses for a month
# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
suma = 0
food = 0
transport = 0
utilities = 0
for i in (monthly_expenses): 
    food += i[0]
    transport += i[1]
    utilities += i[2]
sum(monthly_expenses[0])
    
suma = sum(monthly_expenses[0]) + sum(monthly_expenses[1]) + sum(monthly_expenses[2]) + sum(monthly_expenses[3])
 







# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',sum(monthly_expenses[0]))
print('Week 2:',sum(monthly_expenses[1]))
print('Week 3:',sum(monthly_expenses[2]))
print('Week 4:',sum(monthly_expenses[3]))
print('---------------')
print('TOTAL:',suma)