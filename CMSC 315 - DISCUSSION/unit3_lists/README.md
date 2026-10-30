
# Unit 3 Discussion: List Operations

## Overview

This assignment focused on insertion, deletion, and searching in Python lists. I used a customer waiting list to show how these operations worked in a real-world situation.

## Learning Objectives

- Insert values into a list.
- Delete values from a list.
- Search for values in a list.
- Understand how list operations affect performance.

## Program Description

I created a customer waiting list using Python.

The `insert_at()` function added customers at the beginning, middle, and end of the list. When I inserted a customer at the beginning or middle, the existing elements shifted to the right.

The `delete_at()` function removed customers using their index. I checked whether the index was valid before removing anything. If the index was invalid, the function returned `None`.

The `search_value()` function used linear search. It checked each customer one at a time and returned the index when it found a match. If the customer was not found, it returned `-1`.

## Testing

I successfully tested:

- Insertion at the beginning, middle, and end.
- Deletion at the beginning, middle, and end.
- Searching for an existing customer.
- Searching for a missing customer.
- Deleting with an invalid index.
- Deleting from an empty list.
- Inserting into an empty list.
- Searching an empty list.

## Performance Analysis

Inserting or deleting an item at the beginning or middle of a Python list usually took O(n) time because other elements needed to shift.

Inserting at the end was usually O(1), although resizing could occasionally take longer.

Searching for a value using linear search took O(n) time in the worst case.

Linked lists could be better for frequent insertions and deletions when the correct node was already known because other elements would not need to shift. However, Python lists provided faster access to items by index.

## Reflection

While completing this assignment, I learned how Python lists handled inserting, deleting, and searching for information. I used a customer waiting list as my example because it was easy to understand and showed how lists could be useful in a real business.

One important thing I learned was that inserting or removing an item could cause other elements to change positions. I also learned that linear search checked each item one at a time until it found the correct value.

One challenge I had was testing the search function. At first, I searched for a customer who had already been deleted. The program returned -1 because that customer was no longer in the list. I corrected the test by searching for John, who was still in the list.

I also tested invalid indexes and empty lists to make sure the program handled those situations without crashing.

This assignment helped me understand why performance matters. I learned that larger lists could take more time when elements needed to shift or when a search had to check many items. It also helped me understand when a linked list might be a better choice.
