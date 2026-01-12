# (p5.py) A valid number on the planet Metis consists of the digits 1 through 7 and the lower or upper case letters a
# through d. A plus (+) or minus (-) sign can also appear at the beginning of the number. Create a function
# f(mnumbers) that returns how many numbers in the array mnumbers are valid on the planet Metis. Example:
# f(["A15","-31","7abC","+D1","-g4"]) returns 4
# f(["A05","-3+1","7ab8C","+Bb7","-22c55"]) returns 2

import re

def f(mnumbers):
    suma = 0
    for i in mnumbers:
        if re.search(r"^[+-]?[a-dA-D1-7]+$", i):
            suma += 1

    return suma
    


