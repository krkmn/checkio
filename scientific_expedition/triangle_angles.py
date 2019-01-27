from typing import List
from math import acos, degrees


def checkio(a: int, b: int, c: int) -> List[int]:
    list_sides = sorted([a, b, c])
    if list_sides[0] + list_sides[1] <= list_sides[2]:
        return [0, 0, 0]

    a_angle = round(degrees(acos(((b**2 + c**2 - a**2) / (2*b*c)))))
    b_angle = round(degrees(acos(((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))))
    c_angle = round(degrees(acos(((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))))

    angles = sorted([a_angle, b_angle, c_angle])
    return angles
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")