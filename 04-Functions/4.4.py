###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
a = int(input("First side of the triangle: "))
b = int(input("Second side of the triangle: "))
c = int(input("Third side of the triangle: "))
def triangle_area(a,b,c):
    s = 1/2*(a+b+c)
    result = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return result
print(f'The area of ​​a triangle with sides {a},{b},{c} is {triangle_area(a,b,c)}')
