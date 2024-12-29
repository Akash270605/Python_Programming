n=int(input("Enter the No.: "))
fact=1

if n<0:
    print(f"Factorial of {n} is Not Possible")

elif n==0:
    print(f"Factorial of {n} is: 1")

else: 
 for i in range(1,n):
    fact=fact*i

 print(f"Factorial of {n} is: ",fact)
