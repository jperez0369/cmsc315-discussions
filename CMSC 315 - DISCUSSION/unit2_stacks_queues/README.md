# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored two important data structures in Python:

- Stack (Last In, First Out)
- Queue (First In, First Out)

## Learning Objectives

During this assignment, I learned how to:

- Create and use stacks and queues in Python.
- Add, remove, and view items in both structures.
- Understand the differences between LIFO and FIFO.
- Handle empty stacks and queues.
- Apply these concepts to a real-world situation.

## Program Implementation

I completed the TODO sections in the Python starter code.

For the stack, I used a Python list and implemented push, pop, peek, and is_empty methods. For the queue, I used collections.deque and implemented enqueue, dequeue, front, and is_empty methods.

I created a technical support desk scenario. The queue managed incoming support tickets in the order they arrived, while the stack tracked actions so the most recent action could be removed first.

I also added four items to each structure and demonstrated how they were removed. I included examples of empty structures and single-item structures to explain how the program handled these situations.

## Discussion Board Reflection

This assignment helped me understand how stacks and queues work and why they are important in programming. Before working on this project, I understood the basic idea of organizing information, but I did not fully understand how the order of removing items could affect a program.

One thing I learned was that a stack uses Last In, First Out (LIFO), meaning the last item added is the first one removed. A good example is the undo feature in a computer program. A queue uses First In, First Out (FIFO), meaning the first item added is the first one removed. This is similar to customers waiting in line or support tickets being handled in order.

One challenge was understanding how to handle empty stacks and queues without causing errors. I addressed this by checking whether the structure was empty before removing or viewing an item.

Overall, this assignment helped me understand how choosing the correct data structure can make a program more organized, reliable, and efficient.
