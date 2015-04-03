def checkio ( n ) :
    
    i = 1
    k = 2
    
    while n > 2 * i :
        
        n -= i
        i += k
        k += 1
    
    return min( n , i )

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
