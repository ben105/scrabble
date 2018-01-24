class Collision(object):

	@staticmethod
	def safe(placement):
		"""Will return True if there is room for the placement. Letters already
		placed on the board will be ignored if they match the letter in the
		placement.
		"""
		# We want to make sure that there is some space to place at least one
		# letter from our hand, and that not all letters are already placed.
		# This flag will keep track of if we saw empty space.
		empty_space = False
		for (index, c) in enumerate(placement.word):
			node = placement.node(index)
			if node is None:
				# We went over the edge of the board :(
				return False
			if node.letter is not None and node.letter != c:
				return False
			if node.letter is None:
				empty_space = True
		# At this point, there definitely wasn't a preexisting letter that clashes
		# with any of the letter of the word. So we only want to return true if
		# there was empty space for us to use.
		return empty_space

	@staticmethod
	def preexisting_letters(placement):
		letters = []
		for (index, c) in enumerate(placement.word):
			node = placement.node(index)
			if node is None:
				return letters
			if node.letter is not None and node.placed and node.letter == c:
				letters.append(c)
		return letters

	@staticmethod
	def nodes_matching_letter(placement, letter):
		nodes = []
		for (index, c) in enumerate(placement.word):
			node = placement.node(index)
			if node is None:
				return nodes
			if c == letter:
				nodes.append(node)
		return nodes
