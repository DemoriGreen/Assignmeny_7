"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # A set is a good choice because it allows fast checking for values we have
    # already seen. Adding and checking values is O(1) on average, so the
    # overall runtime is O(n).
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        # A list stores tasks in the order they were added.
        self.tasks = []

    def add_task(self, task):
        # Adding to the end of a list is O(1) on average.
        self.tasks.append(task)

    def remove_oldest_task(self):
        # Removing from the front requires shifting the remaining items,
        # so this operation is O(n).
        if len(self.tasks) == 0:
            return None

        return self.tasks.pop(0)


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        # A set automatically keeps only unique values.
        self.values = set()

    def add(self, value):
        # Adding to a set is O(1) on average.
        self.values.add(value)

    def get_unique_count(self):
        # Getting the size of a set is O(1).
        return len(self.values)
