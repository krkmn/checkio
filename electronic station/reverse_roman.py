'''
You are given a Roman number as a string and your job is to convert
this number into its decimal representation.
'''

from collections import OrderedDict

def reverse_roman(roman_string):
  
    numerals = {1:'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40 :  'XL', 50: 'L',
    90: 'XC', 100: 'C', 400: 'CD', 500 : 'D', 900 : 'CM', 1000 : 'M'} ##Building on a previous exercise on this island
    
    deci =  {v:k for k,v in numerals.items()}
    reverse_numerals = OrderedDict(sorted(deci.items(),key=lambda t: t[1], reverse=True))
    
    digit = 0
    text = roman_string
    while len(text) > 0:
    
        if text[:2] in reverse_numerals.keys():
            digit += reverse_numerals[text[:2]]
            text = text[2:]
        else:
            digit += reverse_numerals[text[:1]]
            text = text[1:]
            
    return digit

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');
