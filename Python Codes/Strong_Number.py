#WAP to Check Strong No.:

n=int(input("Enter the No.: "))
t=n

s=0
while(n>0):
    a=n%10

    #Finding Factorial of Digits
    fact=1
    for i in range(1,a+1):
        fact=fact*i
        

    #sum of factorials
    s=s+fact

    n=n//10
print("Sum of Factorials: ",s)

if(t==s):
    print(f"{t} is Strong No.")

else:
    print(f"{t} is not Strong No.")




    
