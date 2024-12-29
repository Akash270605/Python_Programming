temp= input("Choose temperature in Degree- C or F: ")
n=int(input("Enter Temp Value: "))
if temp=='C':
    F=n*9/5+32
    print("Temperature is: ",F," in Farehneit")

elif temp=='F':
    C=(n-32)*5/9
    print("Temperature is: ",C," in Celcius")

else:
    print("Choose Correct Choice:")
