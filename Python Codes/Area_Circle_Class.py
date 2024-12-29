#TO Find the Area & Perimeter of Circle using Class:

class c:
    def area(self,r):
        self.area=3.14*r**2
        print("Area is: ",self.area)

    def peri(self,r):
        self.p=2*3.14*r
        print("Perimeter is: ",self.p)

radius=float(input("Enter the Radius: "))

circle=c()
circle.area(radius)
circle.peri(radius)
