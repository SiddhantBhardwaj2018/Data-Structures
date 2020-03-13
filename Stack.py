
class Stack:
     def __init__(self):
        #Creating an instance variable items
        self.item = []
        
    def push(self,obj):
        #Push the elements at the last index. Returns None
        self.item.append(obj)
        
    def pop(self):
        #This will remove last item. Returns None
        self.item.pop()
        
    def peek(self):
       #Allows us to see the last elements. Returns last items.
       if self.item:
            return self.item[-1]
       else:
            return None
            
    def size(self):
        #Tells us the size of the stack.
        if self.item:
            return len(self.item)
        else:
            return None
    def is_empty(self):
        #Checks if the stack is empty.Returns a bool value.
        if self.item == []:
            return True
        else:
            return False