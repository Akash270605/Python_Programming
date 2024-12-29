s=input("Enter the String: ")
a=s.lower().replace(" ","")
b=len(a)
x={}

for i in range(0,b):
           if a[i] in x:
              x[a[i]]+=1

           else:
              x[a[i]]=1
print(x)
           



