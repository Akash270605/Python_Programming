n= int(input("Enter the No.: "))

rev=0
while(n>0):
    a=n%10
    rev=rev+a
    n=n//10

print(f"Reverse No. is: ",rev)
