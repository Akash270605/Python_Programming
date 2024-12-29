n= int(input("Enter the Year: "))

if n%100!=0:
    if n%4==0:
        print(f"{n} is Leap Year")
    else:
        print(f"{n} is Not Leap Year")

else:
    if n%400==0:
        print(f"{n} is Leap Year")
    else:
        print(f"{n} is Not Leap Year")
