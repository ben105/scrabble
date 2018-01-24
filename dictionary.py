def binary_search(a, x, lo=0, hi=None):  # Can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)   
    pos = bisect_left(a, x, lo, hi)  # Find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # Don't walk off the end

dictionary = Dictionary.open()

class Dictionary(object):

	@staticmethod
	def open():
		# The folloing dictionary path will be configurable with a flag, and will
		# eventually be defaulted to a path in this bundle.
		dictionary = [line.strip().lower() for line in open('/Users/benrooke/scrabble.dict').readlines()]
		return sorted(dictionary)

	def contains(self, words):
		for word in words:
			if binary_search(dictionary, word) == -1:
				return False
		return True







