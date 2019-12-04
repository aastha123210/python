class Rectangle():
     def _init_(self):
         self.width = 10
         self.height = 13

 #creating function to print its dimensions
     def print_dimension(self):
         print("The dimensions of the rectangle are" + str(self.width) + "x" + str(self.height))

  #creating function to return its area 
     def get_area(self):
         area = self.width * self.height
         return area

  #creating funstion to return its perimeter 
     def get_perimeter(self):
         perimeter = (2*self.width) + (2*self.height)
         return perimeter

 R =    Rectangle()
 R.print_dimensions()
 print("The area of the rectangle is " + str(R.get_area()))
 print("The perimeter of the rectangle is " + str(R.get_perimeter()))

