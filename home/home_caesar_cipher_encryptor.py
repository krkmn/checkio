import string

def to_encrypt(text, delta):
    #replace this for solution
    num_to_text = dict(enumerate(string.ascii_lowercase,start=0))
    num_to_text[100] = ' '
    len_alphabet = len(string.ascii_lowercase)
    ascii_to_num = {string.ascii_lowercase[i-1]:((i+delta-1) % len_alphabet) \
                    for i in range(0,len_alphabet)}
    ascii_to_num[' '] = 100

    cipher_text = ''
    for c in text:
        cipher_text += num_to_text[ascii_to_num[c]]    

    return cipher_text

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
