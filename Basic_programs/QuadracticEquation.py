#importing module
import cmath
a = float(input('Enter a :'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))

#Calculating d
d = (b**2) - (4*a*c)

sol1 = (-b + cmath.sqrt(d))/(2*a)
sol2 = (-b - cmath.sqrt(d))/(2*a)

print('The root of the equation is : {0} and {1}'.format(sol1,sol2))