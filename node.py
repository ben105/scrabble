class Neighbors(object):
	def __init__(self, left=None, up=None, right=None, down=None):
		self.left = left
		self.up = up
		self.right = right
		self.down = down

class Specials(object):
	def __init__(self):
		self.multiplier = 1
		self.double_word = False
		self.triple_word = False

	def value(self):
		return self.multiplier + (10 * self.double_word) + (20 * self.triple_word)

class Node(object):
	def __init__(self, letter=None):
		self.letter = letter
		self.placed = False
		# Default to no neighbors.
		self.neighbors = Neighbors()
		# Default special.
		self.specials = Specials()

	def traverse(self, n, next_lambda):
		if n < 0:
			return self
		node = self
		for _ in range(0, n):
			node = next_lambda(node)
			if node is None:
				return None
		return node

	def is_leftmost(self):
		return self.neighbors.left is None or self.neighbors.left.letter is None

	def is_upmost(self):
		return self.neighbors.up is None or self.neighbors.up.letter is None

	def left(self, n):
		return self.traverse(n, lambda node: node.neighbors.left)

	def right(self, n):
		return self.traverse(n, lambda node: node.neighbors.right)

	def up(self, n):
		return self.traverse(n, lambda node: node.neighbors.up)

	def down(self, n):
		return self.traverse(n, lambda node: node.neighbors.down)

	def value(self):
		return self.specials.value()

	@staticmethod
	def lowest_value(nodes):
		values = [node.value() for node in nodes]
		return sorted(values)[0]
