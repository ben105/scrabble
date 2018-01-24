def getValue(node):
	return node.value()

class Player(object):

	def __init__(self, letters_in_hand, number_of_blanks):
		self.letters = letters_in_hand
		self.number_of_blanks = number_of_blanks
		# Keep track of which nodes we used our blank tiles for.
		self.blank_nodes = []

	def playable(self, placement):
		self.blank_nodes = []
		usable_letters = Collision.preexisting_letters(placement) + self.letters
		if len(placement.word) > (len(usable_letters) + self.number_of_blanks):
			return False
		missing_letters = [letter for letter in placement.word if letter not in usable_letters]
		if missing_letters > self.number_of_blanks:
			return False
		for letter in missing_letters:
			nodes = sorted(Collision.nodes_matching_letter(placement, letter), key=getValue)
			unused_nodes = [node for node in nodes if node not in self.blank_nodes and not node.placed]
			self.blank_nodes.append(unused_nodes[0])
		return True
