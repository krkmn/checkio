import re

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    red_words = ['h+\W*e+\W*l+\W*p','a+\W*s+\W*a+\W*p','u+\W*r+\W*g+\W*e+\W*n+\W*t']
    if subj.isupper():
        return True
    if subj.endswith('!!!'):
        return True  
    subj = subj.lower()
    words = subj.split()
    print(words)
    for word in words:
        for reg in red_words:
            if re.match(reg,word):
                return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("h!e!l!p") == True, "Second"
    print('Done! Go Check it!')
