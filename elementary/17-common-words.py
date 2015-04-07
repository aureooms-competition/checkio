#Let's continue examining words. You are given two string with words separated
#by commas. Try to find what is common between these strings. The words are not
#repeated in the same string.
#
#Your function should find all of the words that appear in both strings. The
#result must be represented as a string of words separated by commas in
#alphabetic order.
#
#Input: Two arguments as strings.
#
#Output: The common words as a string.
#
#Precondition: Each string contains no more than 10 words.  All words separated
#by commas.  All words consist of lowercase latin letters.

def checkio ( first , second ) :
    return ','.join( sorted( set( first.split( ',' ) ).intersection( set( second.split( ',' ) ) ) ) )

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
