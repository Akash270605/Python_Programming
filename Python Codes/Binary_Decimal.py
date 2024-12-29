#Binary to Decimal Conversion

n=int(input("Enter the Binary: "))

#Finding Digits in List
d=[]
inv=0
while(n>0):
    a=n%10
    d.append(a)
    n=n//10

#print("Digits are: ",d)

    
l=len(d)
#print("Length: ",l)

#Code for Conversion
sum=0
for i in range(l):
    sum=sum+(d[i]*2**i)
print("\nDecimal Value: ",sum)
    
