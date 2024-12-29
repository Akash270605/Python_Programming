#Sum of Odd and Even Values sperately in List Using Function

def s(x):
    s_odd=0
    s_even=0
    for j in x:
        if j%2==0:
            s_even+=j

        else:
            s_odd+=j
            
    print("Sum of Even Values: ",s_even)
    print("Sum of Odd Values: ",s_odd)


l=[]
r=int(input("Enter the Range: "))
for i in range(r):
    n=int(input())
    l.append(n)
print(l)
s(l)
