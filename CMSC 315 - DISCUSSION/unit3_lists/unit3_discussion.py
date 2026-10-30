
"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Items at and after the insertion position shift to the right.
    # Inserting at the beginning or middle takes O(n) time because
    # existing elements must move. Inserting at the end is usually O(1).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Only allow valid non-negative indexes to avoid an IndexError.
    # This also prevents accidentally deleting the wrong item.
    if not isinstance(index, int) or index < 0 or index >= len(lst):
        return None

    # Removing an item shifts later elements one position left.
    # Deleting near the beginning takes O(n) time.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Linear search checks each item in order, starting at index 0.
    # It takes O(n) time in the worst case because it may scan all items.
    for index, item in enumerate(lst):
        if item == value:
            return index

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # This list represents customers waiting for service.
    customers = ["John", "Maria", "David"]
    print("Original list:", customers)

    # Insert at the beginning.
    insert_at(customers, 0, "Sarah")
    print("After beginning insertion:", customers)

    # Insert in the middle.
    insert_at(customers, 2, "Alex")
    print("After middle insertion:", customers)

    # Insert at the end.
    insert_at(customers, len(customers), "James")
    print("After end insertion:", customers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Delete the first customer.
    removed = delete_at(customers, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", customers)

    # Delete a customer from the middle.
    removed = delete_at(customers, 2)
    print("Removed from middle:", removed)
    print("Updated list:", customers)

    # Delete the last customer.
    removed = delete_at(customers, len(customers) - 1)
    print("Removed from end:", removed)
    print("Updated list:", customers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # John is still in the list, so this search should return 0.
    position = search_value(customers, "John")
    print("John found at index:", position)

    # Michael is not in the list, so this search should return -1.
    position = search_value(customers, "Michael")
    print("Michael search result:", position)
    print("-1 means the customer was not found.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Invalid indexes return None instead of causing an error.
    print("Invalid deletion:", delete_at(customers, 100))
    print("Negative index deletion:", delete_at(customers, -1))

    # Deleting from an empty list safely returns None.
    empty_list = []
    print("Delete from empty list:", delete_at(empty_list, 0))

    # Inserting into an empty list works.
    insert_at(empty_list, 0, "New Customer")
    print("Insert into empty list:", empty_list)

    # Searching for a missing value returns -1.
    print("Missing customer:", search_value(empty_list, "Unknown"))


if __name__ == "__main__":
    main()
