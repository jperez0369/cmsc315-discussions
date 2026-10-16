
# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explored object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying. I used vehicles and cars as examples to demonstrate these concepts.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

The assignment required the following tasks:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## My Implementation

### Parent Class

I created a parent class called `ParentClass`. It stored the brand and model of a vehicle. I added a class variable called `vehicle_type` and a method called `display_info()` to show information about the vehicle.

### Child Class

I created a child class called `ChildClass` that inherited from the parent class. I added the year and features of each car. I also added a class variable called `vehicle_category`.

I used `super()` to call the parent constructor and reused the parent's information method. I added a method to display the car's features.

### Namespaces

I created two car objects to demonstrate class and instance namespaces. I accessed a class variable through both the class and an object.

I added an owner attribute to only one car. I used `__dict__` to display the information stored in each object and the class namespace. This showed that objects could have their own attributes while sharing class variables.

### Shallow and Deep Copying

I created a car object with a list of features. I then made a shallow copy and a deep copy using Python's `copy()` and `deepcopy()` functions.

After adding a new feature to the original car, I showed that the shallow copy shared the same features list. The deep copy kept its own separate list.

### Student-Created Extension

I added a method called `start_engine()`. This method returned a message showing that the car's engine had started.

## Additional Testing and Edge Cases

I added extra tests to check how my program handled different situations.

First, I created a car with an empty features list. The program was designed to display "Features: None listed" instead of causing an error.

I also tested an empty brand name, an invalid year, and an incorrect type of information for the features list. I added error handling so the program could reject these values and display clear messages.

I created another car object to test different vehicle information. I also added assertions to check the copying and namespace examples.

These tests helped me understand why checking unusual situations is important.

## Real-World Application

This program used a simple vehicle management example. A similar system could help a car dealership keep track of different vehicles, their models, years, and features.

Using inheritance could reduce repeated code when working with different types of vehicles. Checking invalid information could also help prevent mistakes when entering vehicle records.

## Testing and Program Output

I added test calls inside the `main()` function to demonstrate the parent class, child class, inheritance, namespaces, and object copying.

I also added a separate function called `demonstrate_edge_cases()` to check empty and invalid information.

The program included print statements to make the results easier to understand. The tests still needed to be verified by running the updated program in the course environment.

## Conclusion

This assignment helped me understand how Python classes and objects worked together. I learned how inheritance allowed one class to reuse another class's code.

I also learned how namespaces stored information and how shallow and deep copying handled lists differently.

These concepts could help me build programs that are easier to organize, update, and reuse in the future.

## Discussion Board Reflection

The 150–200-word reflection will be submitted separately in the UMGC LEO discussion forum.
