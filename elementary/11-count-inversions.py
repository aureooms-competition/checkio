
def mergesort ( a , b , i , j ) :

    if j - i < 2 : return 0

    m = ( i + j ) // 2

    x = mergesort( b , a , i , m )
    y = mergesort( b , a , m , j )
    z = merge( a , i , m , a , m , j , b , i )

    return x + y + z


def merge ( a , ai , aj , b , bi , bj , c , ci ) :

    z = 0

    while ai < aj and bi < bj :

        if a[ai] <= b[bi] :
            c[ci] = a[ai]
            ai += 1

        else :
            c[ci] = b[bi]
            bi += 1

            z += aj - ai

        ci += 1

    while ai < aj :
        c[ci] = a[ai]
        ai += 1
        ci += 1

    while bi < bj :
        c[ci] = b[bi]
        bi += 1
        ci += 1

    return z


count_inversion = lambda s : mergesort( list( s ) , list( s ) , 0 , len( s ) )


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
