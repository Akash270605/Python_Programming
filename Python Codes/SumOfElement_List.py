#Sum of the Elements in List:

l1=[]
for i in range(5):
    n=int(input())
    l1.append(n)

print("Given List: ",l1)

s=0
for j in l1:
    s=s+j

print("Sum of the Elements: ",s)
