def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)   
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end

dictionary = Dictionary.open()

class Dictionary(object):

	@staticmethod
	def open():
		dictionary = [line.strip().lower() for line in open('/Users/benrooke/scrabble.dict').readlines()]
		return sorted(dictionary)

	def contains(self, words):
		for word in words:
			if binary_search(dictionary, word) == -1:
				return False
		return True







