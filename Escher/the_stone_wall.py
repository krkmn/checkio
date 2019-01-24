def stone_wall(wall):
    #replace this for solution
    rows = wall.split()
    columns = list(zip(*rows))
    gaps = [i.count('0') for i in columns]
    index_of_max = gaps.index(max(gaps))
    return index_of_max

if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
