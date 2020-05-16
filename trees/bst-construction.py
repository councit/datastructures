class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	
	def insert(self, value):
		current_node = self
		while True:
			if value < current_node.value:
				if current_node.left is None:
					current_node.left = BST(value)
					break
				else: current_node = current_node.left
			else:
				if current_node.right is None:
					current_node.right = BST(value)
					break
				else:
					current_node = current_node.right
		return self


	def contains(self, value):
		current_node = self
		while current_node is not None:
			if value < current_node.value:
				current_node = current_node.left
			elif value > current_node.value:
				current_node = current_node.right
			else:
				return True
		return False


	def remove(self, value, parentNode = None):
		pass

root = BST(10)

root.insert(15)

root.insert(5)

root.insert(35)

print(root.value)