from board import Board
from wordsearch import WordSearch
import unittest

class WordsearchTests(unittest.TestCase):
	
	def testSearch(self):
		tiles = [
			['', '', '', 'x', 'z', 's', 'e', 'a', ''],
			['', '', '', 'i', '', 'a', '', '', ''],
			['', '', '', '', '', 'f', '', '', ''],
			['', '', '', '', '', 'e', '', '', ''],
		]
		board = Board(tiles)
		words = WordSearch.words(board.nodes[0][5])
		self.assertEqual(len(words), 2)
		self.assertTrue('safe' in words)
		self.assertTrue('sea' in words)

		words = WordSearch.words(board.nodes[0][3])
		print(words)
		self.assertEqual(len(words), 1)
		self.assertEqual(words[0], 'xi')


if __name__ == '__main__':
	unittest.main()