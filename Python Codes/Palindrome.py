n =int(input("Enter the No.: "))
pal=n

rev=0
while(n>0):
    a=n%10
    rev=rev*10+a
    n=n//10

print("Reverse No. is: ",rev)

if pal==rev:
    print("\nPalindrome No.")

else:
    print("\nNot Palindrome No.")
