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
        self.grandchild = None

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
                        print("Case 3b: adding a node to an inside subtree (lr rotation)")
                elif(self.pivot.balance > 0 and node.value > self.pivot.value):
                    if(self.pivot.right.value < node.value):
                        print("Case 3a: adding a node to an outside subtree")
                    elif(self.pivot.right.value >= node.value):
                        print("Case 3b: adding a node to an inside subtree (rl rotation)")
                         
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
            elif self.pivot.balance >= 1 and node.value > self.pivot.right.value:
                self.left_rotate()
            elif self.pivot.balance <= -1 and node.value > self.pivot.left.value:
                self.lr_rotate()
            elif self.pivot.balance >= 1 and node.value < self.pivot.right.value:
                self.rl_rotate()
            

    

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

        # print("\nBefore right rotation:")
        # self.print_tree()

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

        # print("\nAfter right rotation:")
        # self.print_tree()
    
    def left_rotate(self):

        # print("\nBefore left rotation:")
        # self.print_tree()

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

        # print("\nAfter left rotation:")
        # self.print_tree()

    def lr_rotate(self):
        # print("\nBefore lr rotation:")
        # self.print_tree()

        if self.pivot is None or self.pivot.left is None or self.pivot.left.right is None:
            return

        self.child = self.pivot.left
        self.grandchild = self.child.right

        # left rotation on child
        self.child.right = self.grandchild.left
        self.grandchild.left = self.child
        self.pivot.left = self.grandchild

        # right rotation on pivot
        old_pivot = self.pivot
        old_grandchild = self.grandchild

        old_pivot.left = old_grandchild.right
        old_grandchild.right = old_pivot

        # reconnect to parent
        if old_pivot == self.root:
            self.root = old_grandchild
        elif self.grandparent.left == old_pivot:
            self.grandparent.left = old_grandchild
            
        self.update_balance(self.child)
        self.update_balance(self.pivot)
        self.update_balance(self.grandchild)

        # print("\nAfter lr rotation:")
        # self.print_tree()
    
    def rl_rotate(self):

        # print("\nBefore rl rotation:")
        # self.print_tree() 

        if(self.pivot is None or self.pivot.right is None):
            return
        
        self.child = self.pivot.right
        self.grandchild = self.child.left
        
        #right rotate on child
        self.child.left = self.grandchild.right
        self.pivot.right = self.grandchild
        self.grandchild.right = self.child

        #left rotate on pivot
        old_pivot = self.pivot
        old_grandchild = self.grandchild

        old_pivot.right = old_grandchild.left
        old_grandchild.left = old_pivot

        if(self.pivot == self.root):
            self.root = self.grandchild
        elif(self.grandparent.left == old_pivot):
            self.grandparent = self.grandchild
            
        self.update_balance(self.child)
        self.update_balance(self.pivot)
        self.update_balance(self.grandchild)

        # print("\nAfter rl rotation:")
        # self.print_tree() 


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

    test5 = [1, 2, 4, 3, 5, 6]      
    test6 = [30, 20, 40, 10, 15]   

    test7 = [20, 10, 40, 30, 50, 25, 35]  
    test8 = [40, 20, 50, 10, 30, 25, 35]   

    run_test(test1, "Test Case 1")
    run_test(test2, "Test Case 2")
    run_test(test3, "Test Case 3")
    run_test(test4, "Test Case 4")
    run_test(test5, "Test Case 5 - Case 3a")
    run_test(test6, "Test Case 6 - Case 3b")
    run_test(test7, "Test Case 7 - Case 3b")
    run_test(test8, "Test Case 8 - Case 3b")

def main():
    test_cases()

if __name__ == "__main__":
    main()
