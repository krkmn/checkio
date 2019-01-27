from collections.abc import Iterable


def completely_empty(val):
    try:
        val[0]
    except Exception as err:
        return True

    flat_val = [i for i in flatten(val)]
    if not flat_val:
        return True

    try:
        flat_val[0]
    except Exception as err:
        return True

    return False


def flatten(val):
    if isinstance(val, Iterable):
        for i in val:
            yield from flatten(i)
        pass
    else:
        yield val

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert completely_empty([]) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[],[]]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[],[1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[],[{'':'No WAY'}]]) == True
    print('Done')