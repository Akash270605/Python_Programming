d=int(input("Enter the No. of Digits: "))
n=int(input("Enter the No.: "))

temp=n

s=0
while(n>0):
    a=n%10
    s=s+a**d
    n=n//10
print("Solution is: ",s)

if temp==s:
    print(f"\n{temp} is an Armstrong No.")
else:
    print(f"\n{temp} is Not Armstrong No.")
