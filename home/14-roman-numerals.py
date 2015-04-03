

def checkio ( n ) :

    s = ""

    L = [  'M' , 'CM' , 'D' , 'CD' , 'C' , 'XC' , 'L' , 'XL' , 'X' , 'IX' , 'V' , 'IV' , 'I' ]
    V = [ 1000 ,  900 , 500 ,  400 , 100 ,   90 ,  50 ,   40 ,  10 ,    9 ,   5 ,    4 ,   1 ]

    for letter , value in zip( L , V ) :

        s += letter * ( n // value )
        n %= value

    return s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
