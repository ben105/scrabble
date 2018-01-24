from board import Board
from collision import Collision
from node import Node
from placement import Placement
import unittest

class CollisionTests(unittest.TestCase):

	def create_nodes(self, tiles, previous_lambda, next_lambda):
		nodes = [Node(tile) for tile in tiles]
		for (i, tile) in enumerate(tiles):
			# Set up previous neighbor.
			if i > 0:
				previous_lambda(nodes, i)
			# Set up next neighbor.
			if i < len(tiles) - 1:
				next_lambda(nodes, i)
			nodes[i].placed = True
		return nodes

	def create_horizontal_nodes(self, tiles):
		def prev(nodes, i): nodes[i].neighbors.left = nodes[i - 1]
		def next(nodes, i): nodes[i].neighbors.right = nodes[i + 1]
		return self.create_nodes(tiles, prev, next)

	def create_vertical_nodes(self, tiles):
		def prev(nodes, i): nodes[i].neighbors.up = nodes[i - 1]
		def next(nodes, i): nodes[i].neighbors.down = nodes[i + 1]
		return self.create_nodes(tiles, prev, next)

	def testHorizontalSafe(self):
		tiles = [None, 's', None, 'f', None]
		nodes = self.create_horizontal_nodes(tiles)
		placements = Placement.placements('safe', nodes[1])
		self.assertEqual(len(placements), 2)

		placement = placements[0]
		# Test that we have the right start node.
		self.assertEqual(placement.node(0), nodes[1])

		# Make sure that there is no collision.
		self.assertTrue(Collision.safe(placement))

		vertical_placement = placements[1]
		self.assertEqual(vertical_placement.node(0), nodes[1])
		self.assertFalse(Collision.safe(vertical_placement))

	def testRedundancy(self):
		# Run the test again, but without any empty space.
		tiles = ['s', 'a', 'f', 'e', None, None]
		nodes = self.create_horizontal_nodes(tiles)
		placements = Placement.placements('safe', nodes[0])
		placement = placements[0]
		self.assertFalse(Collision.safe(placement))
		tiles = ['a', 'b', 's', 'a', 'f', 'e', 't', 'b', 'z', 'x', 'h']
		nodes = self.create_horizontal_nodes(tiles)
		placements = Placement.placements('safe', nodes[2])
		placement = placements[0]
		self.assertEqual(placement.node(0), nodes[2])
		self.assertEqual(placement.node(0).letter, 's')
		self.assertFalse(Collision.safe(placement))

	def testRedundancyMultipleOccurence(self):
		tiles = ['s', 'a', 'f', 'e', None, None, 's', 'a', 'f', None]
		nodes = self.create_horizontal_nodes(tiles)
		placements = Placement.placements('safe', nodes[0])
		placement = placements[0]
		self.assertFalse(Collision.safe(placement))
		placements = Placement.placements('safe', nodes[6])
		placement = placements[0]
		self.assertTrue(Collision.safe(placement))

	def testHorizontalCollision(self):
		tiles = [None, 's', 'a', 'e', None]
		nodes = self.create_horizontal_nodes(tiles)
		placements = Placement.placements('safe', nodes[1])
		# We expect the vertical and horizontal placements.
		placement = placements[0]
		self.assertEqual(placement.node(0), nodes[1])
		self.assertFalse(Collision.safe(placement))

	def testVerticalSafe(self):
		tiles = [None, 's', None, 'f', None]
		nodes = self.create_vertical_nodes(tiles)
		placements = Placement.placements('safe', nodes[1])
		# There should be two placement objects returned from the previous static
		# method.
		# One would attempt to place it to the right, and the other downward. Of
		# course the downward placement would fall right off the board, and should
		# not pass the collision safety test.
		self.assertEqual(len(placements), 2)
		placement = placements[1]
		# Test that we have the right start node.
		self.assertEqual(placement.node(0), nodes[1])
		# Make sure that there is no collision.
		self.assertTrue(Collision.safe(placement))
		horizontal_placement = placements[0]
		self.assertEqual(horizontal_placement.node(0), nodes[1])
		self.assertFalse(Collision.safe(horizontal_placement))

	def testPreexistingLetters(self):
		tiles = [None, None, None, 'x', 'z', 's', None, 'f', None]
		nodes = self.create_vertical_nodes(tiles)
		placements = Placement.placements('safe', nodes[5])
		self.assertEqual(len(placements), 2)
		placement = placements[1]
		self.assertTrue(placement, Collision.safe(placement))
		# The preexisting letters should contain the lettera 's' and 'f' because 
		# when placing the word 'safe' across from the letter 's' the letter 'f'
		# would be used as well.
		letters = Collision.preexisting_letters(placement)
		self.assertEqual(len(letters), 2)
		self.assertEqual(letters[0], 's')
		self.assertEqual(letters[1], 'f')

	def testNodesMatchingLetter(self):
		tiles = [['', '', '', 'x', 'z', 's', '', 'f', '']]
		board = Board(tiles)
		first_row = board.nodes[0]
		placements = Placement.placements('safe', first_row[5])
		placement = placements[0]
		nodes = Collision.nodes_matching_letter(placement, 'f')
		self.assertEqual(len(nodes), 1)
		f_node = nodes[0]
		self.assertEqual(f_node.letter, 'f')
		self.assertTrue(f_node.placed)


if __name__ == '__main__':
	unittest.main()
