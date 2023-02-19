class Minheap:
    def __init__(self,array):
        self.heap = None
        self.build_heap(array)
        
        
    def build_heap(self,array):
        self.heap = array
        last = len(self.heap) - 1
        for i in range(self.parent(last),-1,-1):
            self.shift_down(i)
            
            
    def shift_down(self,current):
        end = len(self.heap)-1
        left = self.left_child(current)
        while left <= end:
            
            right = self.right_child(current)
            
            if right <= end and self.heap[right] < self.heap[left]:
                indexswap = right
            else:
                indexswap =left
                
            if self.heap[current] > self.heap[indexswap]:
                self.heap[current],self.heap[indexswap] = self.heap[indexswap],self.heap[current]
                current = indexswap
                left = self.left_child(current)
            else:
                return
             
    def shift_up(self,current):
        parent = self.parent(current)
        while current > 0 and self.heap[parent] > self.heap[current]:
            self.heap[parent],self.heap[current] = self.heap[current],self.heap[parent]
            current = parent
            parent = self.parent(current)
            
            
    def peek(self):
        return self.heap[0]
    
    
    def insert(self,value):
        self.heap.append(value)
        self.shift_up(len(self.heap)-1)
        
        
    def parent(self,i):
        return (i-1)//2
    
    
    def left_child(self,i):
        return i*2 + 1
    
    
    def right_child(self,i):
        return i*2 + 2
    
    
    def display(self):
        for i in range(0,len(self.heap),1):
            print(self.heap[i],end=" ")
    
    
minh = Minheap([5,4,90,88,43,52])
print("Heap:")
minh.display()

minh.insert(22)
minh.insert(33)
minh.insert(44)

print("\n\nMIN_HEAP After insert:")
minh.display()