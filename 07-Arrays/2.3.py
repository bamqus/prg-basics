# The data below contains weekly meal plan. 
# Write a program that prints the weekly meal plan along with the day name as in the example below.

# WEEKLY MEAL PLAN
# (Breakfast, Lunch, Dinner)
# ==========================
# Monday: Oatmeal, Grilled Checken Salad, Spaghetti
# Tuesday: ...
# Wednesday: ...
...
...
...
...
# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plans = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   return f"{weekday(day_number)}: { ', '.join(meal_plans[meal_plan])}" 


for i in range(1,7):
   print(day_meal_plan(i-1, i))
   