#Add Elements in Tuples Dynamically

t=()
l=int(input("Enter the Length of Tuple: "))
for i in range(l):
    n=int(input())
    t=t+(n,)

print("Given Tuple: ",t)
