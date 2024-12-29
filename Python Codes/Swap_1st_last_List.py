#Swap the 1st and Last Elements of the List

l1=[]
for i in range(6):
    n=int(input())
    l1.append(n)

print("Given List: ",l1)
"""
l1[0],l1[-1]=l1[-1],l1[0]
print(l1)
"""

temp=l1[0]
l1[0]=l1[-1]
l1[-1]=temp
print("List After Swapping: ",l1)











































