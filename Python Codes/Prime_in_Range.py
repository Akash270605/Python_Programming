
n= int(input("Range from 2 to "))
for i in range(2,n+1):
     p=0
     for j in range(2,i):
         if i%j==0:
             p=p+1
     if p==0:
         print(i)
     
