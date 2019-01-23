import re

def safe_code1(equation):

    for i in range(0,10):
        if str(i) in equation:
            continue
        eq = equation.replace('#',str(i))

        left_expression = eq.split("=")[0]
        right_expression = eq.split("=")[1]
        try:
            if eval(left_expression) == eval(right_expression):
                all_elements = [i for i in re.split("(\D)", eq) if i]
                if any(i[0] == '0' for i in all_elements):
                    continue
                return i
        except Exception as err:
            pass

    return -1

def safe_code(equation):

    for i in range(0,10):
        if str(i) in equation:
            continue
        eq = equation.replace('#',str(i))
        eq = eq.replace('=','==')

        try:
            if eval(eq):
                all_elements = [i for i in re.split("(\D)", eq) if i]
                if any(i[0] == '0' for i in all_elements):
                    continue
                return i
        except Exception as err:
            pass

    return -1

if __name__ == '__main__':
    print("Example:")
    print(safe_code("-5#*-1=5#"))
    print(safe_code("123*45#=5#088"))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_code("-5#*-1=5#") == 0
    assert safe_code("##*##=302#") == 5
    assert safe_code("19--45=5#") == -1
    assert safe_code("##--11=11") == -1
    assert safe_code("#9+3=22") == 1
    assert safe_code("11*#=##") == 2
    assert safe_code("#9+3=12") == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
