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
        self.pivot = None
        self.grandparent = None
        self.child = None
        self. grandchild = None

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
            print("Case 1 pivot does not exist ")
            return
        
        if current is None:
            current = self.root
            self.pivot = None
            parent = None

            temp = current
            while temp is not None:
                if(temp.balance != 0):
                    self.pivot = temp
                    self.grandparent = parent

                if(node.value <= temp.value):
                    parent = temp
                    temp = temp.left
                else:
                    parent = temp
                    temp = temp.right

            if self.pivot is None:
                print("Case 1: pivot does not exist")
            else:
                if(self.pivot.balance < 0 and node.value > self.pivot.value):
                    print("Case 2: pivot exists bit node is being inserted into shorter subtree")
                elif(self.pivot.balance > 0 and node.value <= self.pivot.value):
                    print("Case 2: pivot exists bit node is being inserted into shorter subtree")
                elif(self.pivot.balance < 0 and node.value <= self.pivot.value):
                    if(self.pivot.left.value >= node.value):
                        print("Case 3a: adding a node to an outside subtree")
                    elif(self.pivot.left.value < node.value):
                        print("Case 3b not supported")
                elif(self.pivot.balance > 0 and node.value > self.pivot.value):
                    if(self.pivot.right.value < node.value):
                        print("Case 3a: adding a node to an outside subtree")
                    elif(self.pivot.right.value >= node.value):
                        print("Case 3b: not supported")
                         
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

        if current == self.root and self.pivot is not None:
            if self.pivot.balance <= -1 and node.value < self.pivot.left.value:
                self.right_rotate()
            if self.pivot.balance >= 1 and node.value > self.pivot.right.value:
                self.left_rotate()
    

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
    
    def right_rotate(self):

        print("\nBefore right rotation:")
        self.print_tree()

        if(self.pivot is None or self.pivot.left is None):
            return
        self.child = self.pivot.left
        self.grandchild = self.child.right
        
        self.pivot.left = self.grandchild
        self.child.right = self.pivot
        
        if self.grandparent is None:
            self.root = self.child
        elif self.grandparent.left == self.pivot:
            self.grandparent.left = self.child
        
        self.update_balance(self.pivot)
        self.update_balance(self.child)

        print("\nAfter right rotation:")
        self.print_tree()
    
    def left_rotate(self):

        print("\nBefore left rotation:")
        self.print_tree()

        if(self.pivot is None or self.pivot.right is None):
            return
        
        self.child = self.pivot.right
        self.grandchild = self.child.left

        self.pivot.right = self.grandchild
        self.child.left = self.pivot

        if self.grandparent is None:
            self.root = self.child
        elif self.grandparent.right == self.pivot:
            self.grandparent.right = self.child


        self.update_balance(self.pivot)
        self.update_balance(self.child)

        print("\nAfter left rotation:")
        self.print_tree()
    
    def print_tree(self, current=None, prefix="", is_left=None):
        if current is None:
            current = self.root

        if current is None:
            print("Empty tree")
            return

        tree_height = self.height(current)
        levels = []
        queue = [current]

        for _ in range(tree_height):
            levels.append(queue[:])
            next_queue = []
            for node in queue:
                if node is None:
                    next_queue.extend([None, None])
                else:
                    next_queue.append(node.left)
                    next_queue.append(node.right)
            queue = next_queue

        max_label = 3
        for level in levels:
            for node in level:
                if node is not None:
                    max_label = max(max_label, len(f"{node.value}|{node.balance}"))

        label_width = max_label + 2
        canvas_width = max((2 ** (tree_height - 1)) * (label_width + 1), label_width + 2)

        for depth, level_nodes in enumerate(levels):
            step = max(2, canvas_width // (2 ** depth))
            line = [" "] * (canvas_width + label_width)

            for index, node in enumerate(level_nodes):
                if node is None:
                    continue

                label = f"{node.value}|{node.balance}"
                center = step // 2 + index * step
                start = max(0, center - len(label) // 2)

                for offset, char in enumerate(label):
                    if start + offset < len(line):
                        line[start + offset] = char

            print("".join(line).rstrip())

            if depth == tree_height - 1:
                continue

            edge_line = [" "] * (canvas_width + label_width)
            child_offset = max(1, step // 4)

            for index, node in enumerate(level_nodes):
                if node is None:
                    continue

                center = step // 2 + index * step
                if node.left is not None and center - child_offset >= 0:
                    edge_line[center - child_offset] = "/"
                if node.right is not None and center + child_offset < len(edge_line):
                    edge_line[center + child_offset] = "\\"

            if any(char != " " for char in edge_line):
                print("".join(edge_line).rstrip())

def run_test(values, name):
    print(f"\n{name}")
    tree = BST()
    for v in values:
        print(f"Inserting {v}")
        tree.insert(Node(v))
        
def test_cases():
    test1 = [10, 5, 15, 2, 12, 1]
    test2 = [20, 10, 30, 5, 25, 27]
    test3 = [50, 25, 75, 10, 60, 5]
    test4 = [40, 20, 60, 10, 50, 5]

    test5 = [1, 2, 4, 3, 5, 6]   # Case 3a on insert 5
    test6 = [30, 20, 40, 10, 15]  # Case 3b on insert 15

    run_test(test1, "Test Case 1")
    run_test(test2, "Test Case 2")
    run_test(test3, "Test Case 3")
    run_test(test4, "Test Case 4")
    run_test(test5, "Test Case 5 - Case 3a")
    run_test(test6, "Test Case 6 - Case 3b")

def main():
    test_cases()

if __name__ == "__main__":
    main()
