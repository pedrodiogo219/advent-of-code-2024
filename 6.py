

m = []

with open('inputs/6.txt', 'r') as file:
    for line in file:
        m.append(list(line.strip()))

R = len(m)
C = len(m[0])
x, y  = 0, 0

dirs = ['^', '>', 'v', '<']
dir_idx = 0


def isOutbound(x, y):
    return not (0 <= x < R and 0 <= y < C)


for i in range(R):
    for j in range(C):
        if m[i][j] == '^':
            x, y = i, j
            m[x][y] = 'X'
            break


#returns true if loop, returns false if not
def simulate(startPos, m):
    vis = set()
    x, y = startPos
    direction = '^'
    vis.add((x, y, '^'))
    dirs = ['^', '>', 'v', '<']
    dir_idx = 0

    while True:
        # print(f'im here {(x, y)}')
        # print(f'direction: {direction}')

        # for i in range(R):
        #     for j in range(C):
        #         print(m[i][j], end="")
        #     print()

        if direction == '^':
            nx, ny = x - 1, y
        if direction == '>':
            nx, ny = x, y + 1
        if direction == 'v':
            nx, ny = x + 1, y
        if direction == '<':
            nx, ny = x, y - 1

        if isOutbound(nx, ny):
            return False

        if m[nx][ny] == '#':
            dir_idx = (dir_idx + 1) % 4
            direction = dirs[dir_idx]
        if m[nx][ny] == '.' or m[nx][ny] == 'X':
            m[nx][ny] = 'X'
            if (nx, ny, direction) in vis:
                return True
            vis.add((nx, ny, direction))
            x, y = nx, ny

cont = 0
for i in range(R):
    for j in range(C):
        print(f'TESTING NEW OBS IN POS {(i, j)}')
        if m[i][j] != '#' and (i, j) != (x, y):
            m[i][j] = '#'
            if simulate((x, y), m):
                cont += 1
            m[i][j] = '.'
 
print(cont)

# for i in range(R):
#     for j in range(C):
#         print(m[i][j], end="")
#     print()

