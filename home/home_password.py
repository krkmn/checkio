import re

def checkio(data: str) -> bool:
    upper = re.search("[A-Z]+",data)
    lower = re.search("[a-z]+",data)
    digits = re.search("[0-9]+",data)
    if upper is None:
        return False
    if lower is None:
        return False
    if digits is None:
        return False
    if (len(data)<10):
        return False
    if (len(data)>64):
        return False

    return True
    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
