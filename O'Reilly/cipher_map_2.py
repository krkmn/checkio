def transformation(grille_vector):

    dummy_vector = grille_vector.copy()
    
    new_vectors = grille_vector.copy()
    trans_matrix = { (0,0) : (0,3),
                     (0,1) : (1,3),
                     (0,2) : (2,3),
                     (0,3) : (3,3),
                     (1,3) : (3,2),
                     (2,3) : (3,1),
                     (3,3) : (3,0),
                     (3,2) : (2,0),
                     (3,1) : (1,0),
                     (3,0) : (0,0),
                     (2,0) : (0,1),
                     (1,0) : (0,2),
                     (1,1) : (1,2),
                     (1,2) : (2,2),
                     (2,2) : (2,1),
                     (2,1) : (1,1),
                     }
    for j in range(3):
        new_vector = []
        for i in dummy_vector:
            new_vector.append(trans_matrix[i])
        new_vector = sorted(new_vector)
        dummy_vector = new_vector
        new_vectors += new_vector
    return new_vectors


def vectorize(code_matrix):
    grille_vector = []
    for i in range(len(code_matrix)):
        for j in range(len(code_matrix[i])):
            if code_matrix[i][j] == 'X':
                grille_vector.append((i,j))

    return grille_vector

def decrypt(cipher_map, decrypt_vector):
    out_text = ''
    for c in decrypt_vector:
        out_text += cipher_map[c[0]][c[1]]
        
    return out_text
 

def recall_password(cipher_grille, ciphered_password):
    grille_vector = vectorize(cipher_grille)
    map_vector = transformation(grille_vector)
   
    out_text = decrypt(ciphered_password, map_vector)
    return out_text


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

