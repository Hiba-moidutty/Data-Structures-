# Max-Heap
def heapify(arr,n,i):
    largest = i 
    l = 2*i +1
    r =2*i +2
    if l < n and arr[i] < arr[l]:
        largest = l
        
    if r < n and arr[largest] < arr[r]:
        largest = r
        
    if largest!= i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)
        
        
def insert(array,newnum):
    size = len(array)
    if size == 0 :
        array.append(newnum)
    else:
        array.append(newnum)
        for i in range((size//2)-1,-1,-1):
            heapify(array,size,i)
            
            
def deletenode(array,num):
    size = len(array)
    for i in range(0,size):
        if num == array[i]:
            break 
    array[i],array[size-1] = array[size-1],array[i]
    array.remove(num)
    for i in range((size//2)-1,-1,-1):
        heapify(array,len(array),i)
     
    
    
arr=[2,36]
insert(arr,18)
insert(arr,14)
insert(arr,9)
insert(arr,4)
insert(arr,8)
print("Max-Heap array: ",str(arr))
deletenode(arr,4)
print("\n\nAfter deleting an element : ",str(arr))