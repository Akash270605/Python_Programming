#Swap the first half Elements in List with 2nd half Elements using Function

def swap(x):
    a=len(x)-1
    b=a//2
    c=b+1
    for j in range(c):
      if (a+1)%2==0:
        temp=x[j]
        x[j]=x[c]
        x[c]=temp
        
        c=c+1

      else:
        temp=x[j]
        x[j]=x[c-1]
        x[c-1]=temp
        
        c=c+1
    print("Swapped List: ",x)

l=[]
r=int(input("Enter the Length of List: "))
for i in range(r):
    n=int(input())
    l.append(n)

print("Given List: ",l)
swap(l)

