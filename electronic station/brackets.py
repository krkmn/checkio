'''
You are given an expression with numbers, brackets and operators.
For this task only the brackets matter. Brackets come in three flavors:
"{}" "()" or "[]". Brackets are used to determine scope or to restrict
some expression. If a bracket is open, then it must be closed with a
closing bracket of the same type. The scope of a bracket must not
intersected by another bracket. In this task you should make a decision,
whether to correct an expression or not based on the brackets.
Do not worry about operators and operands
'''

import re

def checkio(expression):

    brackets = re.findall('[\[{()}\]]', expression)
    if not brackets:
        return True
    bracket_o_c = {'[' : 'open','(' : 'open','{' : 'open', ']':'close', ')':'close', '}': 'close',}
    pairs = {'[' : ']','(' : ')','{' : '}', ']':'[', ')':'(', '}': '{',}
    status = [bracket_o_c[x] for x in brackets]

    if  brackets.count('[') != brackets.count(']')  or brackets.count('(') != brackets.count(')') or \
    brackets.count('{') !=  brackets.count('}'):
        return False
    
    while (len(brackets)>0):
        
        if status[0] != 'open':
            return False
            
        for i in range(len(brackets)-1):
            if (status[i] =='open' and status[i+1] == 'close') and (pairs[brackets[i]] ==  brackets[i+1]):
                del brackets[i+1]
                del brackets[i]
                del status[i+1]
                del status[i]
                break
            elif (status[i] =='open' and status[i+1] == 'close') and (pairs[brackets[i]] !=  brackets[i+1]):
                return False
    
    return True



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
