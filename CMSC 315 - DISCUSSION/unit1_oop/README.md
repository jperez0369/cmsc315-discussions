
# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explored object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

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

For this assignment, I created a Python program using vehicles and cars as examples.

### Parent Class

I created a parent class called `ParentClass`. It stored the brand and model of a vehicle. I also added a class variable and a method that displayed information about the vehicle.

### Child Class

I created a child class called `ChildClass` that inherited from the parent class. I added the year and features of the car. I also added methods to display the car's information and features.

### Namespaces

I created two car objects to demonstrate namespaces. I accessed a class variable through both the class and an object. I also added an owner attribute to only one car and displayed each object's information using `__dict__`.

### Shallow and Deep Copying

I created a car object with a list of features. I then made a shallow copy and a deep copy of the object.

After adding a new feature to the original car, I demonstrated that the shallow copy shared the same features list, while the deep copy kept its own separate list.

### Student-Created Extension

I added a method called `start_engine()`. This method displayed a message when the car's engine started.

### Testing

I added test calls in the `main()` function to display information about the parent and child objects and demonstrate the other functions.

The program was designed to show how inheritance, namespaces, and object copying worked in Python.

## Discussion Board Reflection

The discussion board reflection was completed separately in the UMGC LEO discussion forum.
