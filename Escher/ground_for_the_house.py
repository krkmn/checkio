def house_1(plan):

    width = 0
    row_floors = plan.split()

    # for i in range(len(row_floors)):
    #
    #     if row_floors[i].count('#') >0:
    #         d_width = len(row_floors[i])- row_floors[i][::-1].index('#')-row_floors[i].index('#')
    #         if d_width > width:
    #             width = d_width

    left_i = len(row_floors)-1
    right_i = len(row_floors)-1
    for i in range(len(row_floors)):
        # print(row_floors[i])
        if row_floors[i].count('#') >0:
            l_i = row_floors[i].index('#')
            r_i = row_floors[i][::-1].index('#')
            if l_i < left_i:
                left_i = l_i
            if r_i < right_i:
                right_i = r_i




    column_walls = [''.join(i) for i in list(zip(*plan.split()))]
    floor_i = len(column_walls)-1
    ceil_i = len(column_walls)-1
    for i in range(len(column_walls)):
        # print(column_floors[i])
        if column_walls[i].count('#') >0:
            f_i = column_walls[i].index('#')
            c_i = column_walls[i][::-1].index('#')
            if f_i < floor_i:
                floor_i = f_i
            if c_i < ceil_i:
                ceil_i = c_i

    ceil_i = len(column_walls) - ceil_i
    right_i = len(row_floors)-right_i
    if ceil_i == floor_i:
        ceil_i += 1

    if left_i == right_i:
        left_i += 1

    length = ceil_i-floor_i
    width = right_i-left_i
    print(width)
    print(length)
    print(width*length)
    return width*length

def house(plan):

    height_floors = plan.split()
    width_walls = [''.join(i) for i in list(zip(*plan.split()))]

    width_vector = ''
    height_vector = ''

    max_width = len(height_floors[0])
    max_height = len(width_walls[0])


    for i in range(max_width):
        if any([x[i] == '#' for x in height_floors]):
            width_vector += '#'
        else:
            width_vector +=' '

    for i in range(max_height):
        if any([x[i] == '#' for x in width_walls]):
            height_vector += '#'
        else:
            height_vector +=' '

    return len(height_vector.strip())*len(width_vector.strip())



if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
