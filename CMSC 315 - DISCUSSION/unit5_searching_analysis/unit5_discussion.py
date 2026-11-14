
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================
INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.
You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.
    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks each value one at a time.
    # In the worst case, it checks all n values: O(n).
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.
    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    left = 0
    right = len(lst) - 1

    # Binary search removes half of the remaining
    # values each time, giving it O(log n) complexity.
    while left <= right:
        middle = left + (right - left) // 2

        if lst[middle] == target:
            return middle

        if lst[middle] < target:
            # Ignore the lower half.
            left = middle + 1
        else:
            # Ignore the upper half.
            right = middle - 1

    return -1


def count_linear_checks(lst, target):
    """Count how many values linear search examines."""
    for index, value in enumerate(lst):
        if value == target:
            return index + 1

    return len(lst)


def count_binary_checks(lst, target):
    """Count how many middle values binary search examines."""
    left = 0
    right = len(lst) - 1
    checks = 0

    while left <= right:
        middle = left + (right - left) // 2
        checks += 1

        if lst[middle] == target:
            return checks

        if lst[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return checks


def show_search_results(scores, target):
    """Display results and comparison counts."""
    linear_index = linear_search(scores, target)
    binary_index = binary_search(scores, target)

    print(f"Target: {target}")
    print(f"Linear search: index {linear_index}, "
          f"{count_linear_checks(scores, target)} comparisons")
    print(f"Binary search: index {binary_index}, "
          f"{count_binary_checks(scores, target)} comparisons")

    if linear_index == -1:
        print("Result: The target was not found in the list.")
    else:
        print("Result: Both methods found the target.")

    print()


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    small_scores = [55, 67, 72, 81, 90, 95]

    # Both searches find 81 at index 3.
    # Both return -1 when searching for 100.
    show_search_results(small_scores, 81)
    show_search_results(small_scores, 100)

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    large_scores = list(range(1, 100001))

    # Linear search may check every value.
    # Binary search skips half of the remaining values.
    show_search_results(large_scores, 100000)
    show_search_results(large_scores, 100001)

    print("Large dataset explanation: Binary search needs fewer "
          "comparisons because it cuts the sorted search range in half.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Empty list: both methods return -1.
    print("Empty list: no values are available.")
    show_search_results([], 81)

    # Single item: both methods return index 0.
    print("Single-item list: the target is the only value.")
    show_search_results([81], 81)

    # Missing value: both methods return -1.
    print("Missing value: the target is not in the list.")
    show_search_results([55, 67, 72], 81)

    # First position: the target is at index 0.
    print("First position: the target is at index 0.")
    show_search_results([55, 67, 72, 81], 55)

    # Last position: the target is at the final index.
    print("Last position: the target is at the final index.")
    show_search_results([55, 67, 72, 81], 81)

    # Check that both algorithms return correct results.
    assert linear_search([], 81) == -1
    assert binary_search([], 81) == -1

    assert linear_search([81], 81) == 0
    assert binary_search([81], 81) == 0

    assert linear_search([55, 67, 72], 81) == -1
    assert binary_search([55, 67, 72], 81) == -1

    assert linear_search(large_scores, 100000) == 99999
    assert binary_search(large_scores, 100000) == 99999

    print("All verification tests passed.")


if __name__ == "__main__":
    main()
