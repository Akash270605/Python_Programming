n=int(input("Enter the No.: "))
sum=0
for i in range(1,n):
    if n%i==0:
        print(i)
        sum=sum+i
        i=i+1
print(f"Sum of Factors are: ",sum)

if sum==n:
    print(f"{n} is Perfect No.")

else:
    print(f"{n} is Not Perfect No.")
