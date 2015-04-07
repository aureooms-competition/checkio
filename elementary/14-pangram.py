#A pangram (Greek:παν γράμμα, pan gramma, "every letter") or holoalphabetic
#sentence for a given alphabet is a sentence using every letter of the alphabet
#at least once. Perhaps you are familiar with the well known pangram "The quick
#brown fox jumps over the lazy dog".
#
#For this mission, we will use the latin alphabet (A-Z). You are given a text
#with latin letters and punctuation symbols. You need to check if the sentence
#is a pangram or not. Case does not matter.
#
#Input: A text as a string.
#
#Output: Whether the sentence is a pangram or not as a boolean.
#
#Precondition:
#
#all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
#0 < len(text)


def c1 ( text ) :
	inascii = lambda c : 'a' <= c <= 'z'
	return len( set( filter( inascii , text.lower( ) ) ) ) == 26

def c2 ( text ) :
	inascii = lambda c : 97 <= ord( c ) <= 122
	return len( set( filter( inascii , text.lower( ) ) ) ) == 26

def c3 ( text ) :
	inascii = set( "abcdefghijklmnopqrstuvwxyz" ).__contains__
	return len( set( filter( inascii , text.lower( ) ) ) ) == 26

def check_pangram ( text ) :
	from random import choice
	return choice( ( c1 , c2 , c3 ) )( text )

if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
	assert not check_pangram("ABCDEF"), "ABC"
	assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
