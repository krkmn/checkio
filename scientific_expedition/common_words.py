def checkio(first, second):

    first_words = sorted(first.split(','))
    second_words = second.split(',')

    common_words = ''

    for word in first_words:
        if word in second_words:
            if len(common_words) == 0:
                common_words += word
            else:
                common_words += ',' +word

    return common_words

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
