#WAP to Check SPY Number:

n=int(input("Enter the No.: "))
t=n

s=0
p=1
while(n>0):
    a=n%10
    s=s+a
    p=p*a

    n=n//10

print("Sum of Digits: ",s)
print("Product of Digits: ",p)

if(s==p):
    print(f"\n{t} is Spy No.")

else:
    print(f"\n{t} is Not Spy No.")
