m = []
with open('inputs/4.txt', 'r') as file:
    for line in file:
        m.append(line.strip())

R = len(m)
C = len(m[0])

DIRECTIONS = [ (0, 1),  # right
               (1, 1),  # down-right 
               (1, 0),  # down
               (1, -1), # down-left
               (0, -1), # left
               (-1, -1),# up-left
               (-1, 0), # up
               (-1, 1), # up-right
            ]

diagonalPrincipal = [(1, 1), (-1, -1)]
diagonalSecundaria = [(1, -1), (-1, 1)]

def inbounds(x, y):
    return 0 <= x < R and 0 <= y < C

def findXMAS(x, y, direction):
    nx, ny = x, y
    for letter in 'XMAS':
        # print(f'checkin for letter {letter} in pos {(nx, ny)}')
        if not inbounds(nx, ny) or not m[nx][ny] == letter:
            return False
        nx += direction[0]
        ny += direction[1]

    return True

def crossIsInbound(x, y):
    diagonalPrincipal = [(1, 1), (-1, -1)]
    diagonalSecundaria = [(1, -1), (-1, 1)]

    for dir in diagonalPrincipal:
        nx, ny = x + dir[0], y + dir[1]
        if not inbounds(nx, ny):
            return False
    for dir in diagonalSecundaria:
        nx, ny = x + dir[0], y + dir[1]
        if not inbounds(nx, ny):
            return False
        
    return True
        

def getLetterAfterDislocating(x, y, dir):
    return m[x + dir[0]][y + dir[1]]

def findCross(x, y):
    if not crossIsInbound(x, y):
        return False
    
    firstLetter = getLetterAfterDislocating(x, y, diagonalPrincipal[0])
    lastLetter = getLetterAfterDislocating(x, y, diagonalPrincipal[1])
    word = firstLetter + m[x][y] + lastLetter

    # print(word)
    if word != 'MAS' and word != 'SAM':
        return False
    
    firstLetter = getLetterAfterDislocating(x, y, diagonalSecundaria[0])
    lastLetter = getLetterAfterDislocating(x, y, diagonalSecundaria[1])
    word = firstLetter + m[x][y] + lastLetter

    # print(word)
    if word != 'MAS' and word != 'SAM':
        return False
    
    return True


def main():
    cont = 0
    for i in range(R):
        for j in range(C):
            if m[i][j] == 'A':
                # print(f'Achei A pos {(i, j)}')
                if findCross(i, j):
                    cont += 1
    
    print(cont)

main()