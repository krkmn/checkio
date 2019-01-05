VOWELS = "aeiouy"


def translate(phrase):
    new_phrase = phrase[0]

    for i in range(1,len(phrase)):
        if (phrase[i-1] not in VOWELS+' '):
            continue
        new_phrase += phrase[i]

    for c in VOWELS:
        new_phrase = new_phrase.replace(c*3,c)

    return new_phrase


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
