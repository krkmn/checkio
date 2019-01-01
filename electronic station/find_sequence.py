'''
    Check for 4 repeating numbers in an NxN matrix
    row-wise, column-wise or diagonally
    Return true if found, else false
'''

def checkio(matrix):
    vector = []
    cols = list(zip(*matrix))
    rows = matrix
    for m in matrix:
        vector += m
    uniques = set(vector)
    diagonalsnw, diagonalsne = diagonal_coord(matrix)
    
    for num in uniques:
        for col in cols:
            for i, x in enumerate(cols[:-3]):
                if all([x == num for x in col[i:i+4]]):
                   
                    return True
        for row in rows:
            for i, x in enumerate(rows[:-3]):
                if all([x == num for x in row[i:i+4]]):
                    return True
        for diag in diagonalsnw:
            if all( [matrix[x][y] == num for x,y in diag]):
                return True
        for diag in diagonalsne:
            if all( [matrix[x][y] == num for x,y in diag]):
                return True
    return False

def diagonal_coord(m):
    diagonalsnw = []
    diagonalsne = []
    n = len(m)
    for i in range(n-3):
        for j in range(n-3):
            diagonalsnw.append([(i,j), (i+1,j+1), (i+2,j+2), (i+3,j+3)]) 
            diagonalsne.append([(i,(n-1)-j), (i+1,(n-1)-(j+1)), (i+2,(n-1) - (j+2)), (i+3,(n-1)-(j+3))])        
       
    return diagonalsnw, diagonalsne


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
