FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio ( number ) :
    
    s = ""
    
    upper = number // 100
    lower = number % 100
    
    if upper > 0 : s += FIRST_TEN[upper - 1] + " " + HUNDRED
    
    if lower == 0 : return s
    
    if s : s += " "
    
    if   lower < 10 : s += FIRST_TEN[lower - 1]
    elif lower < 20 : s += SECOND_TEN[lower - 10]
    else :
        
        unit = lower % 10
        tens = lower // 10
        
        s += OTHER_TENS[tens - 2]
        if unit > 0 : s += " " + FIRST_TEN[unit - 1]
    

    return s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
