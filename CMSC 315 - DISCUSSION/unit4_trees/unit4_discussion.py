
"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Start at the root and use recursion to insert.
        # Smaller values go left and larger values go right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # Create a new node when an empty spot is found.
        if node is None:
            return Node(value)

        # Smaller values belong on the left.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong on the right.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored in this program.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # A BST can skip half of the remaining tree
        # at each step when it is reasonably balanced.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # An empty node means the value was not found.
        if node is None:
            return False

        # The value was found.
        if value == node.value:
            return True

        # Search only the left side for smaller values.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Search only the right side for larger values.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        if node is None:
            return

        # Visit smaller values on the left first.
        self._inorder_recursive(node.left, values)

        # Add the current value to the list.
        values.append(node.value)

        # Visit larger values on the right last.
        # This order produces a sorted list.
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Employee IDs are a real-world example of BST values.
    employee_ids = [1050, 1025, 1075, 1010, 1040,
                    1060, 1090, 1030, 1080]

    tree = BST()

    for employee_id in employee_ids:
        tree.insert(employee_id)

    print("Employee IDs inserted:", employee_ids)
    print("A BST places smaller IDs on the left and larger IDs on the right.")
    print("This helps searches skip branches that cannot contain the ID.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    sorted_ids = tree.inorder()
    print("Sorted employee IDs:", sorted_ids)

    # Left, root, right gives sorted output because
    # smaller IDs are stored before larger IDs.
    print("In-order traversal visits left, root, then right.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Two IDs exist and two IDs do not exist.
    search_ids = [1025, 1080, 1100, 1000]

    for employee_id in search_ids:
        result = tree.search(employee_id)
        print("Search for", employee_id, ":", result)

    # True means the ID was found.
    # False means the ID does not exist in the tree.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Test an empty tree.
    empty_tree = BST()
    print("Empty tree traversal:", empty_tree.inorder())
    print("Search empty tree for 1050:", empty_tree.search(1050))

    # Test a duplicate employee ID.
    # Duplicate IDs are ignored to avoid repeated records.
    tree.insert(1050)
    print("After inserting duplicate 1050:", tree.inorder())

    # Test a tree with only one employee ID.
    single_tree = BST()
    single_tree.insert(2000)
    print("Single-node tree:", single_tree.inorder())
    print("Search single-node tree for 2000:", single_tree.search(2000))

    # Demonstrate how insertion order can affect efficiency.
    sequential_tree = BST()
    for employee_id in [1001, 1002, 1003, 1004, 1005]:
        sequential_tree.insert(employee_id)

    print("Sequential insertion:", sequential_tree.inorder())
    print("Sequential insertion creates a right-heavy tree.")
    print("A badly unbalanced BST can become as slow as linear search.")


if __name__ == "__main__":
    main()
