l1=[]

for i in range(5):
    n=int(input())
    l1.append(n)

print("Given List is: ",l1)

l2=[]

for j in l1:
    if l2.count(j)==0:
        l2.append(j)
        
print(l2)





















