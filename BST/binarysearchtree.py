class BST:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        

    def insert(self,data):
        if self.data is None:
            self.data = data
            return
        if self.data == data:
            return
        if self.data > data:
            if self.leftchild:
                self.leftchild.insert(data)
            else:
                self.leftchild = BST(data)
        else:
            if self.rightchild:
                self.rightchild.insert(data)
            else:
                self.rightchild = BST(data)
          

    def search(self,data):
        if self.data == data:
            print("Node found")
            return
        if self.data > data:
            if self.leftchild:
                self.leftchild.search(data)
            else:
                print("Node is not present in tree")
        else:
            if self.rightchild:
                self.rightchild.search(data)
            else:
                print("Node is not present tree!")
    
    
    def deletion(self,data):
        if self.data is None:
            print("Tree is empty")
            return 
        if self.data > data:
            if self.leftchild:
                self.leftchild = self.leftchild.deletion(data)
            else:
                print("\nGiven node is not present in tree")
        elif self.data < data:
            if self.rightchild:
                self.rightchild = self.rightchild.deletion(data)
            else:
                print("\nGiven node is not present in tree")
        else:
            if self.leftchild is None:
                temp = self.rightchild
                self = None
                return temp

            if self.rightchild is None:
                temp = self.leftchild
                self = None
                return temp
            
            node = self.rightchild
            while node.leftchild:
                node = node.leftchild
            self.data = node.data
            self.rightchild = self.rightchild.deletion(node.data)
        return self

        
    def printree(self):
        if self.leftchild:
            self.leftchild.printree()
        print(self.data,end = " ")
        if self.rightchild:
            self.rightchild.printree()
            
    
    def closest(self,target):
        current = self
        closest = current.data
        while current:
            if abs(target-closest) > abs(target-current.data):
                closest = current.data
            if target < current.data :
                current = current.leftchild
            elif target > current.data:
                current = current.rightchild
            else:
                break
        return closest
 


root = BST(25)
list1 = [20,4,39,4,1,5,6]
for i in list1:
    root.insert(i)
root.search(39)
root.printree()
root.deletion(25)
print("\nTree after deletion")
res = root.closest(22.5)
root.printree()
print("\n\nclosest value is=",res)
