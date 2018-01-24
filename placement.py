class Placement(object):

	def __init__(self, start_node, word, to_right):
		self._node = start_node
		self.word = word
		self.to_right = to_right

	def __iter__(self):
		self.i = 0
		return self

	def __next__(self):
		if self.i == len(word):
			raise StopIteration
		self.i += 1
		return (self.node(self.i), word[self.i])

	def node(self, index):
		if self.to_right:
			return self._node.right(index)
		return self._node.down(index)

	@staticmethod
	def verified_placements(placements):
		return [placement for placement in placements if Collision.safe(placement)]

	@staticmethod
	def placements(word, node):
		if node.letter is None:
			return []
		# The following is a list of indicies of where the node's letter exists in the attempted word.
		# For example, if node.letter == 'a' and we want to place the word 'against', we would get the
		# resulting indicies:
		#       against
		#       ^ ^
		#       0 2
		# (zero and two)
		letter_locations = [index for (index, c) in enumerate(word) if c == node.letter]
		# And we can get the various starting nodes based on the previous results.
		nodes_to_left = [node.left(index) for index in letter_locations if node.left(index) is not None]
		nodes_above = [node.up(index) for index in letter_locations if node.up(index) is not None]
		# Create placement objects from the start nodes.
		horizontal_placements = [Placement(start_node, word, True) for start_node in nodes_to_left]
		vertical_placements = [Placement(start_node, word, False) for start_node in nodes_above]
		return horizontal_placements + vertical_placements


	@classmethod
	def placements_on_node(cls, node):
		# Given the node we are pivoting around, find all valid placements for each word in the dictionary.
		return [Placement.placements(word, node) for word in dictionary.dictionary]