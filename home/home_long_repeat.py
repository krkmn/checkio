import re

def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    sub_strings = [max(re.findall(i+'+',line),key=len) for i in set(line)]
    if not sub_strings:
        return 0
    else:
        return len(max(sub_strings,key=len))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
