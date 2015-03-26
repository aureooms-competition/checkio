import itertools

def checkio ( tableau ) :
    
    rows = tableau
    columns = ( "".join( row[i] for row in tableau ) for i in range( 3 ) )  
    diagonal = "".join( tableau[i][i] for i in range( 3 ) )
    antidiagonal = "".join( tableau[2-i][i] for i in range( 3 ) )
    
    diagonals = ( diagonal , antidiagonal )
    
    lines = itertools.chain( rows , columns , diagonals )
    
    for line in lines :

        if line == "XXX" : return "X"
        if line == "OOO" : return "O"
    
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

