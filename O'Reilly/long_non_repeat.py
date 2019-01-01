def non_repeat(line: str) -> str:
    """
        the longest substring without repeating chars
    """
    if not line:
        return line
        
    line_uniques = []
    for i in range(len(line)):
        line_short = line[i:]
        line_new = ''
        for c in line_short:
            if c and c in line_new:
                line_uniques.append(line_new)
                line_new = c
            else:
                line_new += c
        line_uniques.append(line_new)

    return max(line_uniques,key=lambda x: len(x))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
