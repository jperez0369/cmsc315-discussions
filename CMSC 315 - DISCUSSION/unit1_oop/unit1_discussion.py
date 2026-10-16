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
        # Check that the vehicle has a valid brand and model.
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Brand must be a non-empty name.")

        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty name.")

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
        # Use the parent constructor for brand and model.
        super().__init__(brand, model)

        # Check the year and features before saving them.
        if not isinstance(year, int) or isinstance(year, bool) or year < 1886:
            raise ValueError("Year must be a valid whole number (1886 or later).")

        if not isinstance(features, list):
            raise TypeError("Features must be a list.")

        self.year = year
        self.features = features.copy()

    # Override the parent method to include the year.
    def display_info(self):
        return f"{super().display_info()}, Year: {self.year}"

    def show_features(self):
        # Handle a car that has no features listed.
        if not self.features:
            return "Features: None listed"

        return f"Features: {', '.join(self.features)}"

    # TODO 6: Student-created extension.
    # This method simulates starting the car engine.
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

    car1 = ChildClass(
        "Toyota", "Camry", 2022, ["Bluetooth", "Camera"]
    )

    car2 = ChildClass(
        "Honda", "Civic", 2023, ["Navigation"]
    )

    print("Class variable through class:", ChildClass.vehicle_category)
    print("Same class variable through object:", car1.vehicle_category)

    # Only the first car receives an owner attribute.
    car1.owner = "Jonathan"

    print("First car namespace:", car1.__dict__)
    print("Second car namespace:", car2.__dict__)

    print("Child class namespace keys:", list(ChildClass.__dict__.keys()))

    # Check that the owner attribute belongs only to car1.
    owner_test = "owner" in car1.__dict__ and "owner" not in car2.__dict__
    print("Owner is only on first car:", owner_test)


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

    # A shallow copy shares the original object's features list.
    # A deep copy creates a separate copy of the features list.
    original.features.append("Backup camera")

    print("Original features:", original.features)
    print("Shallow copy features:", shallow.features)
    print("Deep copy features:", deep.features)

    print(
        "Explanation: Shallow copy shares the features list; "
        "deep copy keeps its own list."
    )

    # Check that both copying methods worked as expected.
    assert shallow.features == original.features
    assert deep.features != original.features


# EXTRA TESTS AND EDGE CASES:
# These tests check empty lists and invalid information.
# They also demonstrate how errors are handled safely.

def demonstrate_edge_cases():
    print("\n=== Extra Tests and Edge Cases ===")

    # Test 1: Create a car with an empty features list.
    empty_car = ChildClass("Honda", "Fit", 2018, [])

    print("Empty features test:", empty_car.show_features())

    assert empty_car.show_features() == "Features: None listed"

    # Test 2: Try creating a car with an empty brand.
    try:
        ChildClass("", "Civic", 2023, [])
    except ValueError as error:
        print("Invalid brand handled:", error)
    else:
        raise AssertionError("Empty brand should be rejected.")

    # Test 3: Try using text instead of a list for features.
    try:
        ChildClass("Toyota", "Camry", 2022, "Bluetooth")
    except TypeError as error:
        print("Invalid features handled:", error)
    else:
        raise AssertionError("Non-list features should be rejected.")

    # Test 4: Try creating a car with an invalid year.
    try:
        ChildClass("Ford", "Focus", 1800, [])
    except ValueError as error:
        print("Invalid year handled:", error)
    else:
        raise AssertionError("Invalid year should be rejected.")

    # Test 5: Create another valid car object.
    another_car = ChildClass(
        "Mazda", "3", 2021, ["Radio"]
    )

    print("Extra object test:", another_car.display_info())
    print("All extra tests passed.")


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

    # Run the additional tests and edge cases.
    demonstrate_edge_cases()


if __name__ == "__main__":
    main()
