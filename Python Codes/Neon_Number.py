#WAP to Check Neon No.:

n=int(input("Enter the No.: "))

sq=n**2
print(f"Square of {n} is: ",sq)
s=0

while(sq>0):
    a=sq%10
    s=s+a
    sq//=10
print("Sum is: ",s)

if s==n:
    print(f"\n{n} is Neon No.")

else:
    print(f"\n{n} is Not Neon No.")

