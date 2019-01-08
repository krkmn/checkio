from math import sqrt
from functools import reduce
def checkio(number):

    def find_all_factors(number):
        factors = []
        for i in range(2,int(sqrt(number))+2):
            if number/i == int(number/i):
                second_number = int(number/i)
                factors += find_all_factors(second_number)

        return factors + [number]

    A = find_all_factors(number)
    print(A)

    return 0
    # print(i)
    # string_of_numbers = f"{i}{int(number/i)}"
    # if not factors:
    #     return 0
    #
    #
    # for lines in factors:
    #     answer =  reduce(lambda x, y: int(x) * int(y),lines)
    #     print(answer)
    #     if answer == number:
    #         return int(lines)
    #
    # return 0


# A = checkio(20)
B = checkio(20)
# if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio(20) == 45, "1st example"
#     assert checkio(21) == 37, "2nd example"
#     assert checkio(17) == 0, "3rd example"
#     assert checkio(33) == 0, "4th example"
#     assert checkio(3125) == 55555, "5th example"
#     assert checkio(9973) == 0, "6th example"
