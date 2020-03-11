
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        if self.data is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node.prev = cur
            new_node.next = None
            
    def prepend(self,data):
        if self.data is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
    def add_after_node(self,key,data):
        curr_node = self.head
        while curr_node:
            if curr_node.next is None and curr_node.data == key:
                self.append(data)
                return
            elif curr_node.data == key:
                new_node = Node(data)
                nxt =  curr_node.next
                curr_node.next = new_node
                new_node.next = curr_node.next
                nxt.prev = new_node
            curr_node = curr_node.next
        
    def add_before_node(self,key,data):
        curr_node = self.head
        while curr_node:
            if curr_node.prev is None and curr_node.data == key:
                self.prepend(data)
            elif curr_node.data == key:
                new_node = Node(data)
                prv = curr_node.prev
                prv.next = new_node
                new_node.next = curr_node
                new_node.prev = prv
            curr_node = curr_node.next
            
    def delete(self,key):
        cur =  self.head
        while cur:
            if cur.data == key and cur == self.head:
            #Case 1
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                #Case 2
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
            elif cur.data == key:
                # Case 3
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                # Case 4
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
            cur = cur.next
    
    def reverse(self):
        tmp = None #Temporary Pointer
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev
            
    def delete_node(self,node):
        cur =  self.head
        while cur:
            if cur == node and cur == self.head:
            #Case 1
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                #Case 2
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
            elif cur == node:
                # Case 3
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                # Case 4
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
            cur = cur.next
            
    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt 
    
    def pairs_with_sum(self,sum_val):
        pairs = []
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append(tuple([p.data,q.data]))
                q = q.next
            p = p.next
        return pairs            
                
    def print_list(self):
        elems = []
        cur = self.head
        while cur:
            elems.append(cur.data)
            cur =  cur.next
        print(elems)
            