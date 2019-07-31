
class Node(object):

	def __init__(self,data):
		self.data = data;
		self.height = 0;
		self.leftChild = None;
		self.rightChild = None;

class AVL(object):

	def __init__(self):
		self.root = None;

	def calcHeight(self, node):

		if not node:
			return -1;

		return node.height;

	def calcbalance(self, node):

		if not node:
			return 0;

		return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

	def rotateRight(self, node):

		print("Rotating to the right on node ", node.data);
		tempLeftChild = node.leftChild;
		t = tempLeftChild.rightChild;

		tempLeftChild.rightChild = node;
		node.leftChild = t;

		node.height = max(self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild)) + 1;
		tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild) , self.calcHeight(tempLeftChild.rightChild)) + 1;

		return tempLeftChild;

	def rotateLeft(self, node):

		print("Rotating to the left on node ", node.data);
		tempRightChild = node.rightChild;
		t = tempRightChild.leftChild;

		tempRightChild.leftChild = node;
		node.rightChild = t;

		node.height = max(self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild)) + 1;
		tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild) , self.calcHeight(tempRightChild.rightChild)) + 1;

		return tempRightChild;

	def insert(self, data):

		self.root = self.insertNode(data, self.root);

	def insertNode(self, data, node):

		if not node:
			return Node(data);

		if data < node.data:
			node.leftChild = self.insertNode(data, node.leftChild);
		else:
			node.rightChild = self.insertNode(data, node.rightChild);

		node.height = max(self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild))
		return self.settleViolation(data, node);

	def settleViolation(self, data, node):

		balance = self.calcbalance(node);
		if balance > 1 and data < node.leftChild.data:
			print("Left left heavy situation .....");
			return self.rotateRight(node);

		if balance < -1 and data > node.rightChild.data:
			print("Right right heavy situation......");
			return self.rotateLeft(node);

		if balance > 1 and data > node.leftChild.data:
			print("Left right heavy situation......")
			node.leftChild = self.rotateLeft(node.leftChild);
			return self.rotateRight(node);

		if balance < -1 and data < node.rightChild.data:
			print("Right left heavy situation......");
			node.rightChild = self.rotateRight(node.rightChild);
			return self.rotateLeft(node);

		return node;

	def traverseInOrder(self, node):
		if node.leftChild:
			self.traverseInOrder(node.leftChild);
		print("%s "% node.data);

		if node.rightChild:
			self.traverseInOrder(node.rightChild);

	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root);

	


avl = AVL();
avl.insert(10);
avl.insert(20);
avl.insert(5);
avl.insert(4);
avl.insert(15);



avl.traverse();


  