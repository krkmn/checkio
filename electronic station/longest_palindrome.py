'''Write a function that finds the longest palindromic substring of a given string.
Try to be as efficient as possible! If you find more than one substring you should
return the one which is closer to the beginning.
Input: A text as a string.

Output: The longest palindromic substring.
'''

def longest_palindromic(text: str):
    
    strings = [text[i:] for i in range(len(text))]
    all_palindromes = []

    for string in strings:
        fl = string[0]
        if string.count(string[0]) == 1:
            continue
        for i in range(1,len(string)+1):
            if (fl == string[i-1]) and (string[:i] == string[i-1::-1]):
                all_palindromes.append(string[:i])
    
    return max(all_palindromes,key=lambda x: len(x)) if all_palindromes else text[0]

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
