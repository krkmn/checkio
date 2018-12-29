def checkio(str_number: str, radix: int) -> int:
    list_numbers = []
    return_sum = 0
    for char in str_number:
        if ord(char)> 64:
            list_numbers.append(ord(char)-55)
        else:
            list_numbers.append(int(char))
    list_numbers = list_numbers[::-1]
    for i in range(len(list_numbers)):
        if list_numbers[i] >= radix:
            return -1
        else:
            return_sum += radix**i*list_numbers[i]
    return return_sum

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
