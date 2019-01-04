'''
Return the equation for a circle after getting three points that
are not on a line
'''


import re

def checkio(data: str) -> str:
    
    numbers_junk = re.split('[,()\s]',data)
    number = [int(x) for x in numbers_junk if x]

    a = number[0]
    b = number[1]
    c = number[2]
    d = number[3]
    e = number[4]
    f = number[5]

    if f == d:
        x = (c**2-e**2)/(2*c-2*e)
        K = (a**2+b**2-c**2-d**2)/(2*b-2*d)
        M = (c-a)/(b-d)
        y = K+M*x
        
    elif b == d:
        x = (c**2-a**2) / (2*c-2*a)
        T = (e**2+f**2-d**2-c**2)/(2*f-2*d)
        S = (c-e)/(f-d)
        y = T+S*x
    else:
        T = (e**2+f**2-d**2-c**2)/(2*f-2*d)
        S = (c-e)/(f-d)
        K = (a**2+b**2-c**2-d**2)/(2*b-2*d)
        M = (c-a)/(b-d)
        x = (T-K)/(M-S)
        y = T+S*x

    r = ((a-x)**2 + (b-y)**2)**0.5
    r = "{0:.2f}".format(r).rstrip('0').strip('.')
    x = "{0:.2f}".format(x).rstrip('0').strip('.')
    y = "{0:.2f}".format(y).rstrip('0').strip('.')

    out_text = f"(x-{x})^2+(y-{y})^2={r}^2"

    
    return out_text

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
