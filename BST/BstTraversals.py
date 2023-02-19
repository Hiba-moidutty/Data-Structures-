#PREORDER Traversal
#INORDER traversal
#POSTORDER traversal
#Min and Max 


class BinaryST:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    
    def insertion(self,data):
        if self.data is None:
            self.data = data
            return
        if self.data == data:
            return
        if self.data < data:
            if self.lchild:
                self.lchild.insertion(data)
            else:
                self.lchild = BinaryST(data)
        else:
            if self.rchild:
                self.rchild.insertion(data)
            else:
                self.rchild = BinaryST(data)
            
            
    def pre_order(self):
        print(self.data,end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()
            
            
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.data,end=" ")
        if self.rchild:
            self.rchild.in_order()
        
        
    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.data,end=" ")
        

    def level_order(self):
        node = self
        q=[]
        q.append(node)
        while q:
            root = q.pop(0)
            print(root.data)
            if root.lchild is not None:
                q.append(root.lchild)

            if root.rchild is not None:
                q.append(root.rchild)
        

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("\n\nthe minimum node: ",current.data)
        
        
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("\nthe maximum node: ",current.data)
        
        
        
bst = BinaryST(20)
array = [19,8,3,15,34,17,22,73,65]
for i in array:
    bst.insertion(i)
# bst.display()
print("\n\nPre-Order traversal")
bst.pre_order()
print("\n\nIn-Order traversal")
bst.in_order()
print("\n\nPost-Order traversal")
bst.post_order()
bst.min_node()
bst.max_node()