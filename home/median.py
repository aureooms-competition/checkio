from random import shuffle

def hoare ( compare , a , i , j ) :

    o = i
    x = a[o]

    while True :

        while True :

            j -= 1

            if i >= j :

                a[o] = a[j]
                a[j] = x
                return j

            elif compare( x , a[j] ) > 0 : break

        while True :

            i += 1

            if i >= j :

                a[o] = a[j]
                a[j] = x
                return j

            elif compare( x , a[i] ) < 0 : break

        # invariant i < j

        t    = a[i]
        a[i] = a[j]
        a[j] =    t


def quickselect ( compare , k , a , i, j ) :

    if j - i < 2 : return
    
    pivot = hoare( compare , a , i , j )

    if k == pivot  : return
    elif k < pivot : quickselect( compare , k , a ,         i , pivot )
    else           : quickselect( compare , k , a , pivot + 1 ,     j )


def asc ( a , b ) :

    return -1 if a < b else 0 if a == b else 1


def checkio(data):

    shuffle( data ) # otherwise sorted array would produce worst case

    n = len( data )

    k = n // 2

    quickselect( asc , k , data , 0 , n )

    median = data[k]

    if not n & 1 : median = ( median + max( data[:k] ) ) / 2

    return median


#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")

