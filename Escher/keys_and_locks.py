def keys_and_locks(lock, some_key):

    if len(lock) == 0 or len(some_key) == 0:
        return False

    cut_key = cut_pattern(some_key)
    cut_lock = cut_pattern(lock)

    rotated_key = cut_key
    for i in range(0,3):
        if rotated_key == cut_lock:
            return True
        rotated_key = rotator(rotated_key)
    return False

def cut_pattern(pattern):
    rows = pattern.split()
    non_zero_rows = []
    for row in rows:
        if all([i == '0' for i in row]):
            continue
        non_zero_rows.append(row)

    columns = [''.join(i) for i in zip(*non_zero_rows)]
    non_zero_pattern = []

    for column in columns:
        if all([i == '0' for i in column]):
            continue
        non_zero_pattern.append(column)

    return '\n'.join(non_zero_pattern)

def rotator(pattern):
    rows = len(pattern.split())
    columns = len(pattern.split()[0])
    pattern = [list(*zip(*j)) for j in pattern.split()]
    rotated_matrix = []

    for i in range(columns):
        rotated_matrix.append([0 for i in range(rows)])
    for row in range(rows):
        for col in range(columns):
            rotated_matrix[columns-1-col][row] = pattern[row][col]
    str_rot_pat = '\n'.join(''.join(i) for i in rotated_matrix)

    return str_rot_pat

if __name__ == '__main__':
    print("Example:")
    print(keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert keys_and_locks('''
0##0
0##0
00#0
00##
00##''',
'''
00000
000##
#####
##000
00000''') == True

    assert keys_and_locks('''
###0
00#0''',
'''
00000
00000
#0000
###00
0#000
0#000''') == False

    assert keys_and_locks('''
0##0
0#00
0000''',
'''
##000
#0000
00000
00000
00000''') == True

    assert keys_and_locks('''
###0
0#00
0000''',
'''
##00
##00''') == False

    print("Coding complete? Click 'Check' to earn cool rewards!")
