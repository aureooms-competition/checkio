def safe_pawns ( pawns ) :
    
    n = 0
    
    for file , rank in pawns :
        
        if rank < "2" : continue
        
        if file > "a" :
            
            first = chr( ord(file) - 1) + str( int(rank) - 1 )
            
            if first in pawns :
                n += 1
                continue
        
        if file < "h" :
            
            second = chr( ord(file) + 1) + str( int(rank) - 1 )
            
            if second in pawns :
                n += 1
                continue
    
    return n

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
