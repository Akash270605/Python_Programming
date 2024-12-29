n=int(input("Enter the Range No."))

a=0
b=1
sum=0

while(sum<=n):
    sum=a+b
    a=b
    b=sum
    print(sum,end=" ")

    sum=a+b
