#Titas Sarker
#Other Lab Class Task!!!
#Task_01
"""

                                                                    Do the following code:

                                                                    _______________________
                                                                    |                     |
                                                                    |    << Vehicle >>    |
                                                                    |_____________________|
                                                                    |                     |
                                                                    |                     |
                                                                    |_____________________|
                                                                    |                     |
                                                                    |+ start()            |
                                                                    |+ stop()             |
                                                                    |_____________________|
                                                                        ^             ^
                                                                        |             |
                                                                        |             |
                                                                        |             |
                                                                        |             | 
                                                    ___________________|___        __|____________________
                                                    |                     |        |                     |
                                                    |         car         |        |      MotorCycle     |
                                                    |_____________________|        |_____________________|
                                                    |                     |        |                     |
                                                    |                     |        |                     |
                                                    |_____________________|        |_____________________| 
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")


class MotorCycle(Vehicle):
    def start(self):
        print("Motorcycle started.")

    def stop(self):
        print("Motorcycle stopped.")


car = Car()
motorcycle = MotorCycle()

car.start()
car.stop()

motorcycle.start()
motorcycle.stop()

try:
    vehicle = Vehicle()
except TypeError as e:
    print(e)

#Task_02

"""
                                            Do the following code:

                                            _______________________
                                            |                     |
                                            |    << Vehicle >>    |
                                            |_____________________|
                                            |                     |
                                            |+ brand              |
                                            |_____________________|
                                            |                     |
                                            |+ startEngine()      | -> abstract method
                                            |+ description()      | -> non-abstryct method
                                            |_____________________|
                                                    ^
                                                    |
                                                    |
                                                    |
                                                    | 
                                            ___________|___________
                                            |                     |
                                            |         car         |
                                            |_____________________|
                                            |                     |
                                            |+model               |
                                            |_____________________|
                                            
Create an object of car. What will happen if we try to create an object of Vehicles class?

"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def startEngine(self):
        pass

    def description(self):
        print(f"This is a vehicle of brand: {self.brand}")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def startEngine(self):
        print(f"{self.brand} {self.model} engine started.")

    def description(self):
        super().description()
        print(f"The model is: {self.model}")


car = Car("Toyota", "Corolla")
car.startEngine()
car.description()

try:
    vehicle = Vehicle("Generic Brand")
except TypeError as e:
    print(e)