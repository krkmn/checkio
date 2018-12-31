def checkio(number: int) -> int:
    minute = 0
    pigeons = 0
    while True:
        number -= pigeons
        if (number <= 0):
            return pigeons  
        number -= minute
        if (number <= 0):
            return pigeons+(number+minute)
        pigeons += minute
        minute += 1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
