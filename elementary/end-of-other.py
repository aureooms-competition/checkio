
class Trie ( object ) :

	def __init__ ( self , data ) :

		self.data = data
		self.dict = {}


	def insert ( self , string , i , j , data ) :

		if i >= j : return

		node = Trie( data if i == j - 1 else None )

		character = string[i]

		self.dict[character] = node

		node.insert( string , i + 1 , j , data )


	def longestprefix ( self , string , i , j ) :

		if i >= j : return ( i , self )

		character = string[i]

		node = self.dict.get( character , None )

		if node is None : return ( i , self )

		return node.longestprefix( string , i + 1 , j )


def checkio ( words ) :

	trie = Trie( None )

	for word in words :

		drow = word[::-1]

		n = len( drow )

		i , node = trie.longestprefix( drow , 0 , n )

		if node.data or i == n : return True

		node.insert( drow , i , n , True )

	return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio({"hello", "lo", "he"}) == True, "helLO"
	assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
	assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
	assert checkio({"one"}) == False, "Only One"
	assert checkio({"helicopter", "li", "he"}) == False, "Only end"
