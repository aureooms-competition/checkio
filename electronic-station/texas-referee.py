from collections import Counter

# poker hand list (lowest is best)
STRAIGHT_FLUSH = 0
FOUR_OF_A_KIND = 1
FULL_HOUSE = 2
FLUSH = 3
STRAIGHT = 4
THREE_OF_A_KIND = 5
TWO_PAIR = 6
ONE_PAIR = 7
HIGH_CARD = 8

# ranks and suits symbols (descending order)
RANKS = "AKQJT98765432"
SUITS = "hdcs"

# dict for efficiency (instead of str.index)
KEY_RANKS = { rank : index for index , rank in enumerate( RANKS ) }
KEY_SUITS = { suit : index for index , suit in enumerate( SUITS ) }

# key methods for ranks, suits, and cards (descending order)
key_ranks = lambda rank : KEY_RANKS[rank]
key_suits = lambda suit : KEY_SUITS[suit]
key_cards = lambda card : ( key_ranks( card[0] ) , key_suits( card[1] ) )

def key_hands ( hand ) :

    """
        Key method for hands. Orders hands in descending order.
    """

    ranks = [ rank for rank , _ in hand ]

    # check if straight by looking for a common substring with RANKS
    straight = "".join( ranks ) in RANKS

    # check if the hand contains cards from a unique suit
    flush = len( Counter( suit for _ , suit in hand ) ) == 1

    # look for pairs, three of a kind, and four of a kind
    pairs , three , four = 0 , 0 , 0

    for _ , count in Counter( ranks ).items( ) :

        if count == 2 : pairs += 1
        if count == 3 : three += 1
        if count == 4 : four += 1

    # generate a key to handle hand rank ties
    key = tuple( key_cards( card ) for card in hand )

    # Straight flush
    if straight and flush : return ( STRAIGHT_FLUSH , key )

    # Four of a kind
    if four == 1 : return ( FOUR_OF_A_KIND , key )

    # Full house
    if three == 1 and pairs == 1 : return ( FULL_HOUSE , key )

    # Flush
    if flush :  return ( FLUSH , key )

    # Straight
    if straight : return ( STRAIGHT , key )

    # Three of a kind
    if three == 1 : return ( THREE_OF_A_KIND , key )

    # Two Pair
    if pairs == 2 : return ( TWO_PAIR , key )

    # One Pair
    if pairs == 1 : return ( ONE_PAIR , key )

    # High card.
    return ( HIGH_CARD , key )


def choose ( cards , k ) :

    """
        Generates all (n choose k) hands of size k from as set of n cards.
        Stable, i.e. the ordering of the generated hands is identical to the
        ordering of the input cards sequence.
    """

    def _choose ( i , j , k ) :

        if k == 0 :
            yield ( )
            return

        while i < j :

            for choice in _choose( i + 1 , j , k - 1 ) :

                yield ( cards[i] , ) + choice

            i += 1

    yield from _choose( 0 , len( cards ) , k )


# input/output, nothing fancy
parse = lambda s : [ ( card[0] , card[1] ) for card in s.split(",") ]
stringify = lambda cards : ",".join( "".join( card ) for card in cards )

def texas_referee ( s ) :

    """
        Sorts input then outputs the best hand out of all possible hands on
        this input.
    """

    # Ordered from highest to lowest value
    cards = sorted( parse( s ) , key = key_cards )

    # Find the best hand
    best = min( choose( cards , 5 ) , key = key_hands )

    return stringify( best )


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert texas_referee("Kh,Qh,Ah,9s,2c,Th,Jh") == "Ah,Kh,Qh,Jh,Th", "High Straight Flush"
    assert texas_referee("Qd,Ad,9d,8d,Td,Jd,7d") == "Qd,Jd,Td,9d,8d", "Straight Flush"
    assert texas_referee("5c,7h,7d,9s,9c,8h,6d") == "9c,8h,7h,6d,5c", "Straight"
    assert texas_referee("Ts,2h,2d,3s,Td,3c,Th") == "Th,Td,Ts,3c,3s", "Full House"
    assert texas_referee("Jh,Js,9h,Jd,Th,8h,Td") == "Jh,Jd,Js,Th,Td", "Full House vs Flush"
    assert texas_referee("Js,Td,8d,9s,7d,2d,4d") == "Td,8d,7d,4d,2d", "Flush"
    assert texas_referee("Ts,2h,Tc,3s,Td,3c,Th") == "Th,Td,Tc,Ts,3c", "Four of Kind"
    assert texas_referee("Ks,9h,Th,Jh,Kd,Kh,8s") == "Kh,Kd,Ks,Jh,Th", "Three of Kind"
    assert texas_referee("2c,3s,4s,5s,7s,2d,7h") == "7h,7s,5s,2d,2c", "Two Pairs"
    assert texas_referee("2s,3s,4s,5s,2d,7h,8h") == "8h,7h,5s,2d,2s", "One Pair"
    assert texas_referee("3h,4h,Th,6s,Ad,Jc,2h") == "Ad,Jc,Th,6s,4h", "High Cards"
