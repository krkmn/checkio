import unicodedata
def checkio(in_string):
    "remove accents"
    new_string = ''
    for char in in_string:

        d = unicodedata.normalize('NFKD', char).encode('ASCII', 'ignore')
        if len(d) == 0 and unicodedata.category(char) != 'Mn':
            new_string += char
        else:
            new_string += d.decode('utf-8')
    return new_string

    # These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    checkio("完好無缺")
    print('Done')
