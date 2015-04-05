from operator import mul
from functools import reduce

checkio = lambda n : reduce( mul , filter( bool , map( int , str( n ) ) ) )
