
class node:
    def __init__(self,data = None):
        '''
        Creates the node class.
        '''
        self.data = data
        self.next = None

class singlelinkedlist:
    def __init__(self):
        '''
        Init function. sets the head of the linkedlist.
        '''
        self.head = node()
        
    def append(self,data):
        '''
        Appends a node to the end of a list.
        '''
        new_node = node(data)
        cur = self.head
        while cur.next !=  None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        '''
        Obtains the length of a linkedlist.
        '''
        total = 0
        cur = self.head
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
        
    def get(self,index):
        '''
        Obtains data from a node in a linkedlist.
        '''
        if index >= self.length():
            return "Error: Index Object Out of Range"
        cur_index = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1
    
    def erase(self,index):
        '''
        Deletes a node from a linkedlist.
        '''
        if index >= self.length() or index < 0:
            return("Error: Index Out of Range")
        cur_index = 0
        cur_node = self.head
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1
    
    def prepend(self,data):
        '''
        Make new_node head of linkedlist
        '''
        new_node =  node(data)
        new_node.next = self.node
        self.head = new_node
        
        
    def display(self):
        '''
        Display elements of linkedlist
        '''
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)
        
