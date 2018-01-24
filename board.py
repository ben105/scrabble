import copy
from node import Neighbors
from node import Node
from node import Specials
from wordsearch import WordSearch

class Board(object):

	def __init__(self, board_layout=None):
		self.nodes = []
		if board_layout is not None:
			self.load(board_layout)

	def __iter__(self):
		self.i = 0
		self.j = 0
		return self

	def __next__(self):
		if self.i > len(self.nodes):
			raise StopIteration
		node = self.nodes[self.i][self.j]
		self.j += 1
		if self.j > len(self.nodes[0]):
			self.j = 0
			self.i += 1
		return node

	def create_node(self, data):
		node = Node()		
		if data.isalpha():
			node.placed = True
			node.letter = data
		return node

	def assign_neighbors(self, node, i, j):
		if j > 0:
			left_node = self.nodes[i][j - 1]
			node.neighbors.left = left_node
			left_node.neighbors.right = node
		if i > 0:
			up_node = self.nodes[i - 1][j]
			node.neighbors.up = up_node
			up_node.neighbors.down = node

	def load(self, board_layout):
		for i in xrange(len(board_layout)):
			# Add a new empty row.
			self.nodes.append([])
			for j in xrange(len(board_layout[0])):
				# Create a new node.
				node = self.create_node(board_layout[i][j])
				self.assign_neighbors(node, i, j)
				self.nodes[i].append(node)

	def copy(self):
		b = Board()
		b.nodes = copy.deepcopy(self.nodes)
		return b

	def valid(self):
		# Check the spelling of every word.		
		for node in self:
			words = WordSearch.words(node)
			if not Dictionary.contains(words):
				return False
		return True

	def place(self, placement):
		for (node, letter) in placement:
			if not node.placed and not node.letter:
				node.letter = letter


