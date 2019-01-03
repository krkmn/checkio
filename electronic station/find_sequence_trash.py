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


A=[[1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5],]

B= [
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1],
    ]

L = [1,2,3,4,5,6,7,8]


print(checkio(A))

diagonalnw, diagonalne = diagonal_coord(A)
diagonaknw, diagonakne = diagonal_coord(B)
