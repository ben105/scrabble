class WordSearch(object):

	@classmethod
	def words(cls, start_node):
		if start_node.is_leftmost:
			horizontal_word = cls.searchHorizontal(start_node)
		if start_node.is_upmost:
			vertical_word = cls.searchVertical(start_node)
		return horizontal_word + vertical_word

	@staticmethod
	def search(start_node, next_lambda):
		letters = []
		node = start_node
		while node is not None and node.letter is not None:
			letters.append(node.letter)
			node = next_lambda(node)
		if len(letters) == 1:
			return []
		return [''.join(letters)]

	@classmethod
	def searchHorizontal(cls, start_node):
		return cls.search(start_node, lambda node: node.neighbors.right)

	@classmethod
	def searchVertical(cls, start_node):
		return cls.search(start_node, lambda node: node.neighbors.down)		
