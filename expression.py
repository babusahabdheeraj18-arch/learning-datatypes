'''length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
print("The area of the rectangle is:", area)
#area of triangle 
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_triangle = 0.5 * base * height
print("The area of the triangle is:", area_triangle)
#area of circle 
radius = int(input("Enter radius: "))
import math
area_circle = math.pi * radius ** 2
print("The area of the circle is:", area_circle)'''

# calculating displacement
'''initial_position = float(input("Enter initial position (in meters): "))
final_position = float(input("Enter final position (in meters): "))
displacement = final_position - initial_position
print("The displacement is:", displacement, "meters")'''

'''#conversion of km to miles
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers *  0.621371
print("The distance in miles is:", miles) '''
 
#area of cuboid
'''length = float(input("Enter length of the cuboid: "))
width = float(input("Enter width of the cuboid: "))     
height = float(input("Enter height of the cuboid: "))
volume = length * width * height
print("The volume of the cuboid is:", volume)'''

#finding root of quadratic equation
import cmath
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
discriminant = b**2 - 4*a*c
root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
print("The roots of the quadratic equation are:", root1, "and", root2)

#finding the area of a trapezoid
base1 = float(input("Enter the length of the first base: "))    
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height of the trapezoid: "))
area_trapezoid = 0.5 * (base1 + base2) * height
print("The area of the trapezoid is:", area_trapezoid)
