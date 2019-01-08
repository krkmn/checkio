import math

def checkio(n, m):

    bytes_n = []
    bytes_m= []

    power_of = math.log(max(n,m))/math.log(2)
    power_of = math.ceil(power_of)
    start = 2**power_of

    for i in range(power_of+1):
        bytes_n.append(int(n / start))
        n = n - int(n / start)*start
        bytes_m.append(int(m / start))
        m = m - int(m / start) * start

        start /= 2

    ham_before_sum = [x^y for x,y in zip(bytes_n,bytes_m)]
    ham = sum(ham_before_sum)
    return ham

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
