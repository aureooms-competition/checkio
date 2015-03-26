
"""
    http://en.wikipedia.org/wiki/Independent_set_%28graph_theory%29
"""

def break_rings ( edges ) :
    
    # We compute the set of nonisolated
    # vertices.
    
    vertices = notisolated( edges )
    
    n = len( vertices )
    
    # The starting lower bound is
    # "removing no vertices", which is an
    # infeasible solution.
        
    lb = 0
    
    # The starting upper bound is
    # "removing all vertices but 1",
    # which is a feasible solution.
    
    ub = n - 1
    
    # The call to `bnb` computes "`n` minus the size of the maximum stable set"
    # of the input graph,
    # which is exactly the minimal number of vertices to remove
    # to get a graph with no edge. In other words, this computes the minimal
    # number of rings our apprentice must break.
    
    return bnb( edges , vertices , lb , ub )


def notisolated ( edges ) :
    
    """
        Returns the list of vertices covered by `edges`.
    """
    
    return list( set.union( *edges ) )
    
    
def remove ( edges , vertex ) :
    
    """
        Returns a new graph from which `vertex` has been removed.
    """
    
    return list( filter ( lambda edge : vertex not in edge , edges ) )
    
    
def neighbours ( edges , vertex ) :
    
    """
        Returns the neighbours of `vertex` in the edge set.
    """
    
    return [ u if v == vertex else v  for ( u , v ) in edges if u == vertex or v == vertex ]


def bnb ( edges , vertices , lb , ub ) :
    
    """
        Returns the the number of vertices minus the size of a maximum stable set
        of the input graph.
    """
    
    # If the graph contains no edge the current solution is
    # feasible. Its value is lb < ub.
    
    if not edges : return lb
    
    while True :
        
        # If removing a vertex cannot produce a better
        # solution, we return the best known solution.
    
        if lb + 1 >= ub : return ub
        
        # We remove the first vertex.
        
        val = bnb( remove( edges , vertices[0] ) , vertices[1:] , lb + 1 , ub )

        # If removing this first vertex produces a better
        # solution we update the best known solution.

        if val < ub : ub = val
        
        # Now we try the other possibility, i.e. keeping the first vertex.
        # A solution where this vertex is kept cannot contain any of its
        # neighbours, hence we remove them.
            
        for u in neighbours( edges , vertices[0] ) :
            
            lb += 1
            edges = remove( edges , u )
                
        # If after this removal the graph contains no edge,
        # we are done. We return the best solution
        # between the candidate one and the best known one.
        
        if not edges : return min( lb , ub )
        
        # Otherwise, we simply update
        # the set of nonisolated vertices.
        
        vertices = notisolated( edges )
        

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"


