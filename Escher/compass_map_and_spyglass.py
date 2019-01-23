symbols = {'Y', 'C', 'M','S'}

def navigation(seaside):

    nRows = len(seaside)
    nCols = len(seaside[0])
    symbolCoordinates = {}
    for i in range(nRows):
        for j in range(nCols):
            if seaside[i][j] in symbols:
                symbolCoordinates[seaside[i][j]] = [i,j]

    distance = []

    for k,v in symbolCoordinates.items():
        distance.append([abs(symbolCoordinates['Y'][0] - v[0]), abs(symbolCoordinates['Y'][1]-v[1])])

    steps = 0

    for i in distance:

        steps += max(i)

    return steps

if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
