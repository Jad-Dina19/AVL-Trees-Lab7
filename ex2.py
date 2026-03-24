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

            temp = current
            while temp is not None:
                if(temp.balance != 0):
                    self.pivot = temp

                if(node.value <= temp.value):
                    temp = temp.left
                else:
                    temp = temp.right

            if self.pivot is None:
                print("Case 1 pivot does not exist")
            else:
                if(self.pivot.balance < 0 and node.value > self.pivot.value):
                    print("Case 2 pivot exists bit node is being inserted into shorter subtree")
                elif(self.pivot.balance > 0 and node.value <= self.pivot .value):
                    print("Case 2 pivot exists bit node is being inserted into shorter subtree")
                elif(self.pivot.balance < 0 and node.value <= self.pivot.value):
                    print("Case 3 is not supported")
                elif(self.pivot.balance > 0 and node.value > self.pivot.value):
                    print("Case 3 is not supported")

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

    run_test(test1, "Test Case 1")
    run_test(test2, "Test Case 2")
    run_test(test3, "Test Case 3")
    run_test(test4, "Test Case 4")

def main():
    test_cases()

if __name__ == "__main__":
    main()