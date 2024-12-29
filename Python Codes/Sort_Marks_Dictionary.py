#WAP to take 5 Student's name and their Marks and print the Dictionary contents in Ascending Order

d={}
for i in range(5):
    name=input("Enter the Name: ")
    marks=int(input("Enter the Marks: "))

    d[name]=marks
print("\nDictionary is: ",d)

a=sorted(d.values())
print("Sorted By Values: ",a)
