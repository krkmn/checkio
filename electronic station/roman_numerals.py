'''For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.

Input: A number as an integer.

Output: The Roman numeral as a string.'''

numerals = {1:'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40 :  'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500 : 'D', 900 : 'CM', 1000 : 'M'}

def checkio(data):
    
    possible_numerals = [i for i in numerals.keys() if i<=data]

    return_string = ''
    while (data >0):
        letter_number = possible_numerals.pop()
        times, data = divmod(data, letter_number)
        return_string += f"{numerals[letter_number]*times}"

    #replace this for solution
    return return_string

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')