import re
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):

    words = [word.upper() for word in re.split("[,.;?! ]",text) if len(word) > 1]
    count = 0

    for word in words:
        stripe_1 = word[::2]
        stripe_2 = word[1::2]

        if (all(i in VOWELS for i in stripe_1) and all(i in CONSONANTS for i in stripe_2)) or \
            (all(i in CONSONANTS for i in stripe_1) and all(i in VOWELS for i in stripe_2)):
            count += 1

    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
