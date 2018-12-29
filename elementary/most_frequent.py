def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    sort_data = sorted(data,key=lambda x: data.count(x),reverse=True)
    return sort_data[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))
    
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
