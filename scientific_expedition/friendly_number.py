from math import log10, floor, ceil

def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """

    number, letter = return_power(number,base,powers)

    print(number)
    if decimals == 0 and number < 0:
        number = ceil(number)
    elif decimals == 0 and number > 0:
        number = floor(number)
    number_string = "%." + str(decimals) +"f"""
    number_string = number_string % number
    
    return number_string + letter + suffix


def return_power(number,base,powers):

    if number < 0:
        sign = -1
    elif number >0:
        sign = 1
    else:
        return number, powers[0]

    number = abs(number)

    powers_enum = list(enumerate(powers,0))
    power = int(log10(number)/log10(base))
    old = 0
    old_letter = powers[0]
    if power < 1:
        return sign*number,powers[0]
    for pow_letter,letter in powers_enum:
        if pow_letter > power:
            return sign*number/(base**old), old_letter
        old = pow_letter
        old_letter = letter

    return sign*number/(base ** powers_enum[-1][0]) , powers_enum[-1][1]

# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert friendly_number(102) == '102', '102'
#     assert friendly_number(10240) == '10k', '10k'
#     assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
#     assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
#     assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

a = friendly_number(-150, base=100, powers=["","d","D"])

print(a)
friendly_number(255000000000, powers=["", "k", "M"])
l = friendly_number(42, powers=["u","d"], suffix="-n")
print(l)