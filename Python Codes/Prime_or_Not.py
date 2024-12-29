n= int(input("Enter the No.: "))
p=0


if n<2:
      print("Invalid No.")
   
else:
    for i in range(2,n):
        if n%i==0:
           p=p+1 

    if p==0:
        print("Prime No.")

    else:
        print("Not Prime No.")


