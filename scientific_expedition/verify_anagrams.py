def verify_anagrams(first_word, second_word):

    first_word = first_word.lower().replace(' ','')
    second_word = second_word.lower().replace(' ','')

    first_count = {}
    second_count = {}

    for char in first_word:
        first_count[char] = first_word.count(char)
    for char in second_word:
        second_count[char] = second_word.count(char)

    if first_count == second_count:
        return True

    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

