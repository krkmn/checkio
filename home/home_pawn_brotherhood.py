def safe_pawns(pawns: set) -> int:
    coordinates = {(ord(i[0]) - ord('a')+1)+int(i[1])*10 for i in pawns }
    safe = 0;
    for coordinate in coordinates:
        if (coordinate - 11 in coordinates) or (coordinate - 9 in coordinates):
            safe += 1
    return safe

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
