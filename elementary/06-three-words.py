def checkio ( words ) :

    words = iter( words.split( ) )

    while True :

        for word in words :
            if word.isalpha( ) : break
        else : return False

        n = 1
        for word in words :
            if not word.isalpha( ) : break
            n += 1
            if n == 3 : return True
