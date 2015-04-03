
class FifoQueue ( object ) :

	class Node ( object ) :

		def __init__ ( self , item , prev , next ) :

			self.item = item
			self.prev = prev
			self.next = next

	def __init__ ( self ) :

		self.head = FifoQueue.Node( None , None , None )
		self.tail = FifoQueue.Node( None , None , None )

		self.head.next = self.tail
		self.tail.prev = self.head

	def empty ( self ) :

		return self.head.next == self.tail

	def put ( self , item ) :

		node = FifoQueue.Node( item , self.tail.prev , self.tail )

		node.prev.next = node
		self.tail.prev = node

	def get ( self ) :

		node = self.head.next

		self.head.next = node.next
		node.next.prev = self.head

		return node.item


def neighbours ( m , n , i , j ) :

	if j + 1 < n : yield "E" , ( i , j + 1 )
	if i + 1 < m : yield "S" , ( i + 1 , j )
	if j > 0 : yield "W" , ( i , j - 1 )
	if i > 0 : yield "N" , ( i - 1 , j )


def bfs ( used , m , n , source , sink ) :

	queue = FifoQueue( )

	i , j = source

	used[i][j] = 1

	queue.put( ( "" , i , j ) )

	while not queue.empty( ) :

		path , i , j = queue.get( )

		for direction , position in neighbours ( m , n , i , j ) :

			if position == sink : return path + direction

			x , y = position

			if used[x][y] : continue

			used[x][y] = 1

			queue.put( ( path + direction , x , y ) )


def checkio ( maze ) :

	source = ( 1 , 1 )
	sink = ( 10 , 10 )

	return bfs( maze , 12 , 12 , source , sink )
