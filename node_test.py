from node import Node
import unittest

class NodeTests(unittest.TestCase):
	
	def testLeft(self):
		n1 = Node(letter='a')
		n2 = Node()
		n3 = Node()
		n3.neighbors.left = n2
		n2.neighbors.left = n1
		self.assertEqual(n3.left(2), n1)
		self.assertEqual(n3.left(2).letter, 'a')

	def testRight(self):
		n1 = Node(letter='a')
		n2 = Node()
		n3 = Node()
		n3.neighbors.right = n2
		n2.neighbors.right = n1
		self.assertEqual(n3.right(2), n1)
		self.assertEqual(n3.right(2).letter, 'a')

	def testDown(self):
		n1 = Node(letter='a')
		n2 = Node()
		n3 = Node()
		n3.neighbors.down = n2
		n2.neighbors.down = n1
		self.assertEqual(n3.down(2), n1)
		self.assertEqual(n3.down(2).letter, 'a')

	def testUp(self):
		n1 = Node(letter='a')
		n2 = Node()
		n3 = Node()
		n3.neighbors.up = n2
		n2.neighbors.up = n1
		self.assertEqual(n3.up(2), n1)
		self.assertEqual(n3.up(2).letter, 'a')

	def testNoneNeighbor(self):
		n1 = Node()
		n2 = Node()
		n1.neighbors.left = n2
		n2.neighbors.right = n1
		self.assertIsNone(n2.left(2))
		self.assertIsNone(n1.right(2))
		self.assertIsNone(n2.left(1))


if __name__ == '__main__':
	unittest.main()