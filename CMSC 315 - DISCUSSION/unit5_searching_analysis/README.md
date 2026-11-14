# Unit 5 Discussion: Search Algorithms

**Student:** Jonathan Perez  
**Course:** CMSC 315 – Data Structures and Analysis

## Overview

This assignment compared linear search and binary search using Python. I created a student score lookup example and tested both algorithms to understand their differences and performance.

## Learning Objectives

- Implemented linear search
- Implemented binary search
- Compared performance
- Analyzed algorithm efficiency

## Requirements

1. Tested both algorithms on a small dataset of six student scores.
2. Tested both algorithms on a large dataset of 100,000 numbers.
3. Tested edge cases, including empty lists, single-element lists, missing values, and first and last positions.
4. Compared the number of comparisons each algorithm needed.
5. Used a student score lookup tool as a real-world example.

## Implementation and Performance Analysis

Linear search checked each value one at a time until it found the target or reached the end of the list. Its worst-case time complexity was O(n).

Binary search used a sorted list and checked the middle value. It removed half of the remaining values after each unsuccessful comparison. Its worst-case time complexity was O(log n).

## Testing Results

| Test | Linear Search | Binary Search |
|---|---|---|
| Small dataset: Find 81 | 4 comparisons | 3 comparisons |
| Small dataset: Missing 100 | 6 comparisons | 3 comparisons |
| Large dataset: Find 100,000 | 100,000 comparisons | 17 comparisons |
| Large dataset: Missing 100,001 | 100,000 comparisons | 17 comparisons |
| Empty list | Returned -1 | Returned -1 |
| Single-element list | Returned index 0 | Returned index 0 |

All verification tests passed.

## Discussion Board Reflection

During this assignment, I learned how linear search and binary search work and why choosing the right algorithm matters. Linear search was easier for me to understand because it checks each value one at a time. Binary search was more challenging because I had to understand how the left, right, and middle positions changed during the search.

One challenge I faced was getting my Python program to run in IntelliJ. I solved this by using the terminal to run the Python file. After that, I checked the results and confirmed that all my tests passed.

The biggest thing I learned was how much more efficient binary search can be with large sorted datasets. When I searched through 100,000 numbers, linear search needed 100,000 comparisons, while binary search needed only 17.

In a real-world situation, I would use linear search for a small or unsorted list, such as checking new inventory items. I would use binary search for a large, sorted list of student records or product IDs. Binary search is better for repeated searches, but sorting data first takes additional work. I learned that the best method depends on the size and organization of the data.
