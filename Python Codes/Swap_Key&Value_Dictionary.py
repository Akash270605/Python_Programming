#WAP to Swap Key and Value in Dictionary

d={}
n=int(input("Enter the Range Value: "))

for i in range(n):
    x=int(input("Enter the Value: "))
    d["key"+ str(i)]=x
    
print("\nDictionary: ",d)

d2={}    
for key,val in d.items():
    d2[val]=key
print("Swapped Dictionary: ",d2)
