#WAP to remove keys with Values Greater than K using Dictionary

d={}
n=int(input("Enter the Range: "))
K= int(input("Enter the Greatest Limit: "))

for i in range(n):
    v=int(input("Enter the Value: "))
    d["Key"+ str(i)]=v
print("Dictionary: ",d)

d2={}
for k,v in d.items():
    if v<=K:
         d2[k]=v

    else:
        continue
print("Removed Dictionary: ",d2)
