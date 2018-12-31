def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    if not data:
        return ()
    sorted_data = sorted(data)
    begin_i = [sorted_data[0]]
    end_i = []

    for i in range(len(sorted_data)-1):
        if (sorted_data[i+1]-sorted_data[i] > 1):
            begin_i.append(sorted_data[i+1])
            end_i.append(sorted_data[i])

    end_i.append(sorted_data[-1])
    return_list = list(zip(begin_i, end_i))
    return return_list

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
