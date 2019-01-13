from functools import reduce
import re
cipher_text = 'ADFGVX'


def encode(message, secret_alphabet, keyword):

    message = message.lower()
    message = re.sub('\W','',message)

    enumerated_c = dict(enumerate(cipher_text))
    string = ''
    for c in message:
        i = secret_alphabet.index(c)
        row = i // len(cipher_text)
        col = i % len(cipher_text)

        string += enumerated_c[row] + enumerated_c[col]

    cipher_no_dup, encode_index, _ = cipher_sort(keyword)
    len_cip = len(cipher_no_dup)
    rows = []
    for i in range(len(string)//len_cip+1):
        if not string[i*len_cip:(i+1)*len_cip]=='':
            rows.append(string[i*len_cip:(i+1)*len_cip].ljust(len_cip,' '))
    columns = list(zip(*rows))
    new_cols = []
    for i in range(len(cipher_no_dup)):
        new_cols.append(columns[encode_index[i]])
    reduced_cols = reduce(lambda x,y : x+y, new_cols)

    return ''.join(reduced_cols).replace(' ', '')

def cipher_sort(keyword):
    cipher_no_dup = ''
    #Removing duplicate chars after their first occurence
    for i in range(0,len(keyword)):
        if i == keyword.index(keyword[i]):
            cipher_no_dup += keyword[i]

    enum_cip = list(enumerate(cipher_no_dup))
    sort_indices = sorted(enum_cip, key=lambda x: x[1])

    decode_index = {}
    encode_index = {}
    for i in range(len(sort_indices)):
        decode_index[sort_indices[i][0]] = i
        encode_index[i] = sort_indices[i][0]

    return cipher_no_dup, encode_index, decode_index

def decode(message, secret_alphabet, keyword):

    cipher_unique, encode_index, decode_index = cipher_sort(keyword)

    len_key = len(cipher_unique)
    n_letter_pair = len(message)
    len_rows = []
    len_count = n_letter_pair

    while len_count > 0:

        if len_count >= len_key:
            len_rows.append(len_key)
            len_count -= len_key
        else:
            len_rows.append(len_count)
            len_count = 0

    n_rows = len(len_rows)
    len_letter_pair_decoded = []
    for i in range(len_key):
        if i<len_rows[-1]:
            len_letter_pair_decoded.append(n_rows)
        else:
            len_letter_pair_decoded.append(n_rows-1)

    len_letter_pair_encoded = []

    for i in range(len_key):
        len_letter_pair_encoded.append(len_letter_pair_decoded[encode_index[i]])

    code_cols = []
    r=0
    for i in range(len(len_letter_pair_encoded)):
        code_cols.append(message[r:(r+len_letter_pair_encoded[i])])
        r += len_letter_pair_encoded[i]

    correct_cols = []

    for i in range(len_key):
        correct_cols.append(code_cols[decode_index[i]])
    almost_decoded_rows = list(zip(*[i.ljust(n_rows,' ') for i in correct_cols]))
    almost_decoded_rows =''.join([''.join(i).strip() for i in almost_decoded_rows])
    letters = []
    for i in range(n_letter_pair//2+1):
        if almost_decoded_rows[(i*2):(2*i+2)]:
            letters.append(almost_decoded_rows[(i*2):(2*i+2)])
    enumerated_c = dict(enumerate(cipher_text))
    enumerate_c_flip = {v:k for k,v in enumerated_c.items()}
    string = ''

    for c in letters:
        row = enumerate_c_flip[c[0]]
        col = enumerate_c_flip[c[1]]
        string += secret_alphabet[row*len(cipher_text)+col]

    return string


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"

    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"