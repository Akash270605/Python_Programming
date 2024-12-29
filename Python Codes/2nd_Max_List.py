#Finding 2nd Max using List

l1=[]
for i in range(5):
    n=int(input("Enter the Values: "))
    l1.append(n)

print("List is: ",l1)

#Largest
m=l1[0]
for j in l1:
    if j>m:
        m=j
print("Largest is: ",m)

#Removing Largest from List
l2=[]
for k in l1:
    if k!=m:
       l2.append(k)

#2nd Largest
m2=l2[0]
for x in l2:
    if x>m2:
        m2=x

print("2nd Largest is: ",m2)
