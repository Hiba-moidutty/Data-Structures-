class BST:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        

    def insert(self,data):
        if self.data is None:
            self.data = data
            return
        if self.data == data:
            return
        if self.data > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)



    def isBST(self):
            if self is None:
                return True

            # Traverse the left subtree and check if all nodes are less than the root
            if self.lchild is not None and self.lchild.data > self.data:
                return False

            # Traverse the right subtree and check if all nodes are greater than the root
            if self.rchild is not None and self.rchild.data < self.data:
                return False

            # Recursively check if left and right subtrees are BSTs
            if (self.lchild and not self.lchild.isBST()) or (self.rchild and not self.rchild.isBST()):
                return False

            return True


bst = BST(20)
array = [19,8,3,15,34,17,22,73,65]
for i in array:
    bst.insert(i)
res = bst.isBST()
print("is BST: ", res )