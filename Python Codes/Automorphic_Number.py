#WAP to Check Automorphic No.:

n=int(input("Enter the No.: "))
sq=n**2
print(f"Square of {n} is: ",sq)

#Checking the No. of digits:
d=len(str(n))
print("No. of Digits: ",d)

l=sq%10**d
print("\nEnding Digits: ",l)

if l==n:
    print(f"\n{n} is Automorphic No.")

else:
    print(f"\n{n} is Not Automorphic No.")
    
