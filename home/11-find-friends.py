def pairs ( network ) :
    
    for pair in network : yield pair.split( '-' )
    

def names ( network ) :
    
    for first , second in pairs( network ) :
        
        yield first
        yield second
        

def check_connection( network , first , second ) :
    
    pos = { name : i for i , name in enumerate( set( names( network ) ) ) }
    
    n = len( pos )
    
    graph = [ [0] * n for i in range( n ) ]
    
    for i , j in ( ( pos[i] , pos[j] ) for ( i , j ) in pairs( network ) ) :
    
        graph[i][j] = 1
        graph[j][i] = 1
        
    first , second = pos[first] , pos[second]
    
    neighbours = [ j for j in range( n ) if graph[first][j] ]
    
    if second in neighbours : return True
    
    while neighbours :
        
        j = neighbours.pop( )
            
        for k in range( n ) :
            
            if graph[first][k] : continue
                
            if graph[j][k] :
                
                if k == second : return True
                
                graph[first][k] = 1
                
                neighbours.append( k )
                
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
