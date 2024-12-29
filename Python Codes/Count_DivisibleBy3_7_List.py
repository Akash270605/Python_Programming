#Count the No. Divisible by 3 and 7 in List using Function

def count(x):
    c=0
    for j in x:
        if j%3==0 or j%7==0:
            c+=1

    print("Count No. Divisible by 3 or 7: ",c)

l=[]
r=int(input("Enter the Range: "))
for i in range(r):
    n=int(input())
    l.append(n)

print("Given List: ",l)
count(l)

