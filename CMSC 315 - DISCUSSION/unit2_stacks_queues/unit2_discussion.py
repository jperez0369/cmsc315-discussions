
"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

This program demonstrates how a technical support desk
uses queues for incoming tickets and stacks for action history.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # New values are placed at the end, which is the top of the stack.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return "Stack is empty. Nothing to remove."

        # LIFO: The last value added is removed first.
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return "Stack is empty. Nothing to view."

        # Peek shows the most recent value without removing it.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New tickets join the back of the waiting line.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return "Queue is empty. No tickets to process."

        # FIFO: The oldest ticket is removed first.
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return "Queue is empty. No tickets waiting."

        # Front displays the first ticket without removing it.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
    print("Scenario: Technical Support Desk")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: ACTION HISTORY ===")

    history = Stack()

    actions = [
        "Reset password",
        "Install printer",
        "Update software",
        "Restart computer"
    ]

    for action in actions:
        history.push(action)
        print("Added action:", action)

    print("\nMost recent action:", history.peek())
    print("LIFO: The last action added is removed first.")

    while not history.is_empty():
        print("Undo action:", history.pop())

    print("\nTesting empty stack:")
    print(history.pop())
    print(history.peek())

    print("\nTesting a stack with one item:")
    single_stack = Stack()
    single_stack.push("One action")
    print("Removed:", single_stack.pop())
    print("Is stack empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: SUPPORT TICKETS ===")

    tickets = Queue()

    requests = [
        "Password issue",
        "Printer not working",
        "Software update",
        "Internet connection issue"
    ]

    for request in requests:
        tickets.enqueue(request)
        print("Ticket added:", request)

    print("\nNext ticket:", tickets.front())
    print("FIFO: The first ticket added is processed first.")

    while not tickets.is_empty():
        print("Processing ticket:", tickets.dequeue())

    print("\nTesting empty queue:")
    print(tickets.dequeue())
    print(tickets.front())

    print("\nTesting a queue with one item:")
    single_queue = Queue()
    single_queue.enqueue("One ticket")
    print("Processed:", single_queue.dequeue())
    print("Is queue empty?", single_queue.is_empty())

    print("\n=== DEMONSTRATION COMPLETE ===")


if __name__ == "__main__":
    main()
