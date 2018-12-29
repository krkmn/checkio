import re

def popular_words(text: str, words: list) -> dict:
    # your code here
    text = text.lower()
    split_text = re.split("[\s.,]+",text)
    count_dict = {}
    for word in words:
        count_dict[word] = split_text.count(word)
    
    return count_dict


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
