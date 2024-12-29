#Pattern 1

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")

#Pattern 2


for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")

#Pattern 3
i=5
while(i>=1):
    j=5
    while(j>=i):
        print(j,end=" ")
        j=j-1
    print("\n")
    i=i-1

#Pattern 4

i=1
while(i<=5):
    j=5
    while(j>=i):
        print("*",end=" ")
        j=j-1
    print("\n")
    i=i+1


    

