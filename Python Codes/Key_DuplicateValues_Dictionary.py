#WAP to find key with Duplicate values in Dictionary

d={}

n=int(input("Enter the Range Value: "))

for i in range(n):
    #k=input("Enter the Key: ")
    v=int(input("Enter the Value: "))
    d["Key" +str(i)]=v

print("\nDictionary: ",d)

d2={}
for k,v in d.items():
    if v in d2:
        d2[v]+=k 
    else:
        d2[v]=k
print(d2)

