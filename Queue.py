
class Queue:
    def __init__(self):
        #Creating an instance variable items
        self.item = []
        
    def push(self,obj):
        #Push the elements at the last index. Returns None
        self.item.append(obj)
        
    def pop(self):
        #This will remove last item. Returns None
        self.item.pop(0)
        
    def display(self):
        for i in range(len(self.item)-1,-1,-1):
            print(self.item[i],end = " ")
        print()