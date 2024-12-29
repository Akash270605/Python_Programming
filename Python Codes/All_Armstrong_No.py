n=int(input("Range from 1 to "))

for i in range(1,n+1):
    l=len(str(i))
    s=0
    temp=i
    while(temp>0):
        a=temp%10
        s=s+a**l
        temp=temp//10

    if i==s:
        print(i)
        
