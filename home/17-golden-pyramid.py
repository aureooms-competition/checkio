import functools

@functools.lru_cache( None )
def count_gold ( pyramid , i = 0 , j = 0 ) :

    if i >= len( pyramid ) : return 0

    return pyramid[i][j] + max( count_gold( pyramid , i + 1 , j ) , count_gold( pyramid , i + 1 , j + 1 ) )
