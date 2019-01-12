def repeat_inside(line):
    repeat_array = []

    if len(set(line)) <= 1:
        return line

    if max([line.count(i) for i in line]) == 1:
        return ''

    for i in range(len(line)):
        for j in range(i + 1, len(line) + 1):
            new = line[i:j]
            if all([(new.count(i) == new.count(new[0]) and new.count(new[0]) > 1) for i in new]):
                c = new.count(new[0])
                _len = len(new)
                arr = []
                jump = _len // c

                for x in range(c):
                    start_i = x * jump
                    end_i = (x + 1) * jump
                    arr.append(new[start_i:end_i])

                if all(i == arr[0] for i in arr):
                    # print(new)
                    repeat_array.append(new)

    return max(repeat_array,key=lambda x: len(x)) #max returns the first value that matches the conditions

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')