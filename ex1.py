from timeit import timeit
import sys
import random
import matplotlib.pyplot as plt

sys.setrecursionlimit(100000)

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.balance = 0
        self.height = 1

class BST:
    def __init__(self):
        self.root = None

    def height(self, current):
        if current is None:
            return 0
        return 1 + max(self.height(current.left), self.height(current.right))

    def update_balance(self, current):
        if current is None:
            return
        
        left_height = 0 if current.left is None else current.left.height
        right_height = 0 if current.right is None else current.right.height

        current.height = 1 + max(left_height, right_height)
        current.balance = right_height - left_height

    def insert(self, node, current=None):
        
        if self.root is None:
            self.root = node
            return
        
        if current is None:
            current = self.root
        
        if node.value <= current.value:
            if current.left is None:
                current.left = node
            else:
                self.insert(node, current.left)
        elif node.value > current.value:
            if current.right is None:
                current.right = node
            else:
                self.insert(node, current.right)

        self.update_balance(current)

    def search(self, value, current=None):
        
        if current is None:
            current = self.root
        
        if current is None:
            return False
        
        if current.value == value:
            return True
        
        if value <= current.value:
            if(current.left is None):
                return False
            else:
                return self.search(value, current.left)
        elif value > current.value:
            if(current.right is None):
                return False
            else:
                return self.search(value, current.right)


def create_tasks():
    tasks = []
    lst = list(range(1000))
    for i in range(1000):
        random.shuffle(lst)
        tasks.append(lst.copy())
    return tasks


def create_tree(task):
    tree = BST()
    
    for x in task:
        tree.insert(Node(x))

    return tree       

def search_tree(tree, task):
    for x in task:
        tree.search(x)

def search_abs_balance(tree):
    def helper(current):
        if current is None:
            return 0

        return max(
            abs(current.balance),
            helper(current.left),
            helper(current.right)
        )

    return helper(tree.root)

def run_tasks():
    tasks = create_tasks()
    times = []
    abs_balances = []
    for task in tasks:
        tree = create_tree(task)
        times.append(timeit(lambda : search_tree(tree, task), number=10)/10)
        abs_balances.append(search_abs_balance(tree))
    
    generate_plot(abs_balances, times)
    
def generate_plot(balances, times):
    plt.scatter(balances, times)
    plt.ylabel("times")
    plt.xlabel("balances")
    plt.show()

def main():
    run_tasks()


if __name__ == "__main__":
    main()