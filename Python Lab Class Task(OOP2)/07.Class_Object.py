#Titas Sarker
#a_Product

"""

         Given UML                          _____________________
                                            |                   |
                                            |      Product      |
                                            |___________________|
                                            |                   |
                                            |name               |
                                            |price              |
                                            |___________________|
                                            |                   |
                                            |display_detail()   | ->(Print name and price)
                                            |___________________|
                                                    ^
                                                    |     
                                            _____________________
                                            |                   |
                                            |Electronic_Product |
                                            |___________________|
                                            |                   |
                                            |warranty           |
                                            |___________________|
                                            |                   |
                                            |display_detail()   |
                                            |___________________|
               
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print(f"Product Name: {self.name}, Price: {self.price}")


class Electronic_Product(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail()
        print(f"Warranty: {self.warranty} years")


# Example usage
product = Product("Generic Item", 100)
product.display_detail()

electronic_product = Electronic_Product("Laptop", 1000, 2)
electronic_product.display_detail()

#b_Shape
"""
     Given UML                          _____________________
                                        |                   |
                                        |      Shape        |
                                        |___________________|
                                        |                   |
                                        |- name             |
                                        |___________________|
                                        |                   |
                                        |+ getName          |
                                        |___________________|
                                        |                   |
                                        |+ display()        |
                                        |display_Info()     |
                                        |___________________|
                                                ^
                                                |     
                                        _____________________
                                        |                   |
                                        |      Rectangle    |
                                        |___________________|
                                        |                   |
                                        |-- length          |
                                        |-- width           |
                                        |___________________|
                                        |                   |
                                        |+ area()           |
                                        |+ perimeter()      |
                                        |___________________|
                                                
"""

class Shape:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def display(self):
        print(f"Shape Name: {self.name}")


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_Info(self):
        print(f"Rectangle Name: {self.getName()}")
        print(f"Length: {self.length}, Width: {self.width}")
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")


# Example usage
rect = Rectangle("MyRectangle", 10, 5)
rect.display_Info()