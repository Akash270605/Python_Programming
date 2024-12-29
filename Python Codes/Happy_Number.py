#WAP to check Happy No.:

n=int(input("Enter the No.: "))
t=n

while(n!=1 and n!=4):
    s=0
    while(n>0):
        a=n%10
        s+=a**2
        n//=10

    n=s
    print("Sum of No.: ",n)

if n==1:
    print(f"\n{t} is Happy No.")

else:
    print(f"\n{t} is Not Happy No.")
