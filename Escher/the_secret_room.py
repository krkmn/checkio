number_dictionary = {
0: '',
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
10: 'ten',
11: 'eleven',
12: 'twelve',
13: 'thirteen',
14: 'fourteen',
15: 'fifteen',
16: 'sixteen',
17: 'seventeen',
18: 'eighteen',
19: 'nineteen',
20: 'twenty',
30: 'thirty',
40: 'forty',
50: 'fifty',
60: 'sixty',
70: 'seventy',
80: 'eighty',
90: 'ninety',
100: 'hundred',
1000: 'onethousand',
}

def secret_room(number):

    text_num_array = sorted([number_to_text(i) for i in range(1,number+1)])
    l = [number_to_text(i) for i in range(1,number+1)]
    print(text_num_array)
    index = text_num_array.index(number_to_text(number))
    print(l.index(number_to_text(number))+1)
    print(index+1)
    return index+1

def number_to_text(number):
    text = ''
    if number>=100:
        if number == 1000:
            return number_dictionary[1000]
        hundred_digit = number // 100
        text = number_dictionary[hundred_digit]+'hundred'
        number -= hundred_digit * 100

    if number <= 20:
        text += ' '+number_dictionary[number]
    elif (number>20 and number <=100):
        ten_num = number // 10
        one_num = number - ten_num * 10
        text += ' '+ number_dictionary[ten_num*10] + number_dictionary[one_num]

    return text.strip()


if __name__ == '__main__':
    print("Example:")
    print(secret_room(5))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert secret_room(5) == 1 #five, four, one, three, two
    assert secret_room(3) == 2 #one, three, two
    assert secret_room(1000) == 551
    print("Coding complete? Click 'Check' to earn cool rewards!")
    for i in range(1,1000):
        print(number_to_text(i))
