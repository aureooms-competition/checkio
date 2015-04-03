
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

		character = string[i]

		if i == j - 1 : return ( i , self.dict.get( character , None ) )

		node = self.dict.get( character , None )

		if node is None : return ( i , None )

		k , next = node.longestprefix( string , i + 1 , j )

		return ( i , node ) if next is None else ( k , next )

def checkio ( words ) :

	trie = Trie( None )

	for word in words :

		drow = word[::-1]

		n = len( drow )

		i , node = trie.longestprefix( drow , 0 , n )

		if ( node and node.data ) or i == n - 1 : return True

		if node : node.insert( drow , i + 1 , n , True )
		else    : trie.insert( drow ,   0   , n , True )

	return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio({"hello", "lo", "he"}) == True, "helLO"
	assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
	assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
	assert checkio({"one"}) == False, "Only One"
	assert checkio({"helicopter", "li", "he"}) == False, "Only end"
