a=int(input("Enter the 1st No.: "))
b=int(input("Enter the 2nd No.: "))
c=int(input("Enter the 3rd No.: "))

if a>=b and a>=c:
    high=a

elif b>=a and b>=c:
    high=b

else:
    high=c

    print("Largest No. is: ",high)
