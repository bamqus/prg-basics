# An array contains a list of Polish names:

# Genowefa, Onufry, Celestyna, Alojzy, Pankracy
# Create a program that prints the longest name 
# (consisting of the largest number of characters). Sample result:

# Names: Genowefa Onufry Cele

arr = ["Genowefa","Onufry","Celestyna","Alojzy","Pankracy"]

imie = ""
for x in arr:
    if len(x) > len(imie):
        imie = x
print(imie)