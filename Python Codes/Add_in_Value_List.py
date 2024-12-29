#Add 5 in list if List Value is Even, else add 10(if Odd)

l1=[]
l=int(input("Enter the Length of List: "))
for i in range(l):
    n=int(input())
    l1.append(n)

print("Given List is: ",l1)

l2=[]
for j in l1:
    if j%2==0:
        b=j+5
        l2.append(b)

    else:
        b=j+10
        l2.append(b)

print("Resulted List is: ",l2)
