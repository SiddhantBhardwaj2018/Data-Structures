class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = None
		self.nextNode = None

class Linkedlist(object):

	def __init__(self):
		self.head = None
		self.size = 0

	def insertStart(self,Data):

		self.size = self.size + 1
		newNode = Node(data)

		if not self.head:
			self.head = newNode

		else:
			newNode.nextNode = self.head
			self.head = newNode


	def remove(self,data):

		if self.head is None:
			return;

		self.size = self.size - 1

		currentNode = self.head;
		previousNode = None;

		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode

		if previousNode is not None:
			self.head = currentNode.nextNode;

		else:
			previousNode.nextNode = currentNode.nextNode
    

    # O(1)
	def size1(self):
		return self.size

    # O(N) not good
	def size2(self):

		actualNode = self.head
		size = 0

		while actualNode is not None:
			size += 1
			actualNode = actualNode.nextNode

		return size

   

     # O(N) 
    def insertEnd(self, Data):

    	self.size =  self.size + 1
    	newNode = Node(Data)
    	actualNode = self.head

    	while actualNode.nextNode is not None:
    		actualNode = actualNode.nextNode

    	actualNode.nextNode = newNode

    def traverseList(self):

    	actualNode = self.head

    	while actualNode is not None:
    		print("%d " % actualNode.data)
    		actualNode = actualNode.nextNode



linkedlist = Linkedlist()

linkedlist.insertStart(12);
linkedlist.insertStart(122);
linkedlist.insertStart(3);
linkedlist.insertEnd(31);

linkedlist.traverseList();
print(linkedlist.size1());

linkedlist.remove(3);
linkedlist.remove(12);
linkedlist.remove(122);
linkedlist.remove(31);

print(linkedlist.size1());
