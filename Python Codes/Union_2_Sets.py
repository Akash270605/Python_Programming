#Union Operation b/w 2 Sets

s1=set()
l1=int(input("Enter the Length of Set 1: "))
for i in range(l1):
    n1=int(input())
    s1.add(n1)

s2=set()
l2=int(input("Enter the Length of Set 2: "))
for j in range(l2):
    n2=int(input())
    s2.add(n2)

print("Given Set 1: ",s1)
print("Given Set 2: ",s2)

s=s1|s2
#s=s1.union(s2)
print("Combined Set: ",s)


