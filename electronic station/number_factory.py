def checkio(number):
    array = []

    def prime(number):
        for i in range(2, int(number ** 0.5) + 1):

            if number / i == int(number / i) and not number / i == 1:
                array.append(i)
                prime(number / i)
                return None

        array.append(int(number))
        return 0

    prime(number)
    if any([x > 9 for x in array]):
        return 0

    joined_array = ','.join(map(str, array))
    joined_array = joined_array.replace('3,3', '9')
    joined_array = joined_array.replace('2,2,2', '8')
    joined_array = joined_array.replace('2,3', '6')
    joined_array = joined_array.replace('2,2', '4')

    return_number = int(''.join(sorted(joined_array.split(','))))

    return 0 if return_number == number else return_number

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
