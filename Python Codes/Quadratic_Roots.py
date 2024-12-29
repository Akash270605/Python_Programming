import cmath
a= int(input("Enter the 1st No.: "))
b= int(input("Enter the 2nd No.: "))
c= int(input("Enter the 3rd No.: "))

dis=(b**2)-(4*a*c)

x1=(-b+ cmath.sqrt(dis))/(2*a)
x2=(-b- cmath.sqrt(dis))/(2*a)

print(f"Solution of {a},{b} and {c}",x1,x2)
