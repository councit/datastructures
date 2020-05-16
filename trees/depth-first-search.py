#Depth-first Search

'''
The idea here is that a search is performed on a tree prioritised with a deepth approach

the return function is an array with the order of nodes are a result of the depth search. 
'''

class Node:
	def __init__(self, name):
		self.children = []
		self.name = name

	def add_child(self, name):
		self.children.append(Node(name))
		return self

	def depth_first_search(self, array):
		array.append(self.name)
		for child in self.children:
			child.depth_first_search(array)
		return array




# Sandbox
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')



node_a.add_child(node_b.name)
node_a.add_child(node_c.name)

node_b.add_child(node_d.name)


print(node_a.depth_first_search(child_array))

