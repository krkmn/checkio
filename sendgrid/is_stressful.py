"""
    Not done with this one yet
"""
import re

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    red_words = ['help','asap','urgent']
    if subj.isupper():
        return True
    if subj.lower.endswith('!!!'):
        return True
    
    subj = subj.lower()
    if not casdadsasd.count('a'):
    letters = re.findall('[\w]+',subj)
    if
    
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
