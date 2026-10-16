"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    vehicle_type = "Vehicle"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    vehicle_category = "Car"

    def __init__(self, brand, model, year, features):
        super().__init__(brand, model)
        self.year = year
        self.features = features

    def display_info(self):
        return f"{super().display_info()}, Year: {self.year}"

    def show_features(self):
        return f"Features: {', '.join(self.features)}"

    # TODO 6: Student-created extension.
    # This extra method lets a car start its engine.
    def start_engine(self):
        return f"The {self.brand} {self.model} engine has started."


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    car1 = ChildClass("Toyota", "Camry", 2022, ["Bluetooth", "Camera"])
    car2 = ChildClass("Honda", "Civic", 2023, ["Navigation"])

    print("Class variable through class:", ChildClass.vehicle_category)
    print("Class variable through object:", car1.vehicle_category)

    car1.owner = "Jonathan"

    print("First car namespace:", car1.__dict__)
    print("Second car namespace:", car2.__dict__)
    print("Class namespace keys:", list(ChildClass.__dict__.keys()))


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Ford", "Focus", 2020, ["Radio", "Air conditioning"]
    )

    shallow = copy(original)
    deep = deepcopy(original)

    # A shallow copy shares the same nested list as the original.
    # A deep copy has its own separate nested list.
    original.features.append("Backup camera")

    print("Original features:", original.features)
    print("Shallow copy features:", shallow.features)
    print("Deep copy features:", deep.features)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    vehicle = ParentClass("Ford", "Truck")
    print(vehicle.display_info())

    print("\n=== Child Object ===")
    car = ChildClass(
        "Toyota", "Corolla", 2024, ["Bluetooth", "Backup camera"]
    )

    print(car.display_info())
    print(car.show_features())
    print(car.start_engine())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
