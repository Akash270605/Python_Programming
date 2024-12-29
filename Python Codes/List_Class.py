#WAP to append,delete and display elements of a list using Class:

class L:
    def append(self,l):
        self.a=int(input("\nEnter the Value to append: "))
        l.append(self.a)
       
    def rem(self,l):
         self.r=int(input("\nEnter the Value to Remove: "))
         if(self.r in l):
             l.remove(self.r)

         else:
             print("\nElement Not Found!!!")

    def display(self,l):
        self.l=l
        print("New List is: ",self.l)

#Code to Get List
n=int(input("Enter the Range of List: "))
l=[]
for i in range(n):
    v=int(input("Enter the Value "+ str(i+1)+" :"))
    l.append(v)
print("List is: ",l)

#Creating Object
List=L()

while(1):
    ch=int(input("\nEnter the Choice: \n1.Append \n2.Remove \n3.Display \n4.Exit: "))
    
    if(ch==1):
        List.append(l)

    elif(ch==2):
        List.rem(l)

    elif(ch==3):
        List.display(l)

    elif(ch==4):
        exit(0)

    else:
        print("Invalid Choice, pls Select Correct!!!!")


