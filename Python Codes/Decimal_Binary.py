#Decimal to Binary Conversion

n=int(input("Enter the Decimal: "))
b=[]
while(n>0):
    r=n%2
    b.append(r)
    n=n//2
#print(b)

l=len(b)-1
print("\nBinary Value: ",end="")

i=l
while(i>=0):
    print(b[i],end="")
    i-=1
