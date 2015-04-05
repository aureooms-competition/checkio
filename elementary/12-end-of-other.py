
class Trie ( object ) :

	def __init__ ( self , data ) :

		self.data = data
		self.dict = {}


	def insert ( self , string , i , j , data ) :

		"""
			Inserts string[i:j] in the trie. Satellite data can be attached
			through parameter `data`. Cannot insert empty strings using this
			method.
		"""

		if i >= j : return

		node = Trie( data if i == j - 1 else None )

		character = string[i]

		self.dict[character] = node

		node.insert( string , i + 1 , j , data )


	def longestprefix ( self , string , i , j ) :

		"""
			Returns where a string should be inserted in the trie and what
			range of character would have to be inserted.
		"""

		if i >= j : return ( i , self )

		character = string[i]

		node = self.dict.get( character , None )

		if node is None : return ( i , self )

		return node.longestprefix( string , i + 1 , j )


def checkio ( words ) :

	"""
		O(n), where n is the sum of the number of characters in each string of
		the input set `words`.
	"""

	# We will use this trie to store suffixes of words. A node in this trie
	# will have satellite data set to `True` iff this node corresponds to the
	# end of a word of the input set.
	trie = Trie( None )

	for word in words :

		# `drow` is the reversed word. Prefixes of reversed words are suffixes
		# of the original words.
		n , drow = len( word ) , word[::-1]

		# This call returns where `drow` could be inserted in the trie.
		# `i` is the position of the first character of `drow` that should be
		# inserted in the trie. `node` is where we should insert this `i`th
		# character.
		i , node = trie.longestprefix( drow , 0 , n )

		# If the position where we should insert is a whole reversed word, i.e.
		# `node.data` is `True`, or if our reversed word is the prefix of a
		# reversed word already in the trie, i.e. `i` is `n`, then we must
		# conclude that the input contains two words from which one is the
		# suffix of the other.
		if node.data or i == n : return True

		# Otherwise we just insert the end of the reversed word in the trie.
		# The satellite data of the last inserted node will contain the Boolean
		# value `True`.
		node.insert( drow , i , n , True )

	return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio({"hello", "lo", "he"}) == True, "helLO"
	assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
	assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
	assert checkio({"one"}) == False, "Only One"
	assert checkio({"helicopter", "li", "he"}) == False, "Only end"
