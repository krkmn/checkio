def fibonacci(number):
    fib = [0, 1, 1]

    for i in range(number):
        fib.append(fib[-1]+fib[-2])
    return fib

def checkio(opacity):

    opac = 10000
    for age in range(0, 10001):
        if age in fibonacci(age):
            opac -= age
        else:
            opac +=1
        if opac == opacity:
            return age

    return None

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"