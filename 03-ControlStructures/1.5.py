
basic_salary = 5000
total_salary = 0
bonus = 0.15 
is_bonus = input('Does the employee receive a bonus? (Y/N): ') 

if is_bonus == "Y":
    print(f"The employee got a {bonus * 100}% bonus!")
else:
    print(f"The employee didn't get a bonus")

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')

if is_bonus == "Y":
    print(f'Total salary: {basic_salary*bonus + basic_salary}')
else:
    print(f'Total salary: {basic_salary}')


