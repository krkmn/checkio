import re

def checkio(text: str) -> str:
    letters = [i.lower() for i in text if re.match('[a-zA-Z]',i)]
##    print(letters)
    unique_letters = list(set(letters))
    unique_letters.sort()
    count_letters = {i:text.lower().count(i) for i in unique_letters}
    max_value = max(count_letters.values())
    for i in count_letters.keys():
        if count_letters[i] == max_value:
            return i
    
    

if __name__ == '__main__':
    print("Example:")
    checkio("Hello world")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
