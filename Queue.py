
class Queue:
    def __init__(self):
        #Creating an instance variable items
        self.item = []
        
    def push(self,obj):
        self.item.insert(0,obj)
        
    def pop(self):
        self.item.pop(-1)
        
    def display(self):
        for i in range(len(self.item)-1,-1,-1):
            print(self.item[i],end = " ")
        print()
