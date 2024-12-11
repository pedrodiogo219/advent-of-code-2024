
def convertToDisk(seq):
    disk = []
    for i in range(len(seq)):
        id = i // 2

        if i % 2 == 0:
            for i in range(seq[i]):
                disk.append(id)
        else:
            for i in range(seq[i]):
                disk.append('.')
    return disk


def findNextFreeSpace(disk, pos):
    for i in range(pos, len(disk)):
        if disk[i] == '.':
            return i
    return -1

def reposition(disk):
    pos = len(disk) - 1
    nextFreeSpace = findNextFreeSpace(disk, 0)
    
    while pos >= 0 and nextFreeSpace != -1 and nextFreeSpace < pos:
        if pos == '.':
            pos -= 1
            continue
        
        disk[nextFreeSpace] = disk[pos]
        disk[pos] = '.'
        pos -= 1
        nextFreeSpace = findNextFreeSpace(disk, nextFreeSpace)
    
    return disk
        
def calcChecksum(disk):
    total = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            continue
        total += i * disk[i]
    return total


def moveBlocksOnDisk(disk):
    r = len(disk) - 1
    

    #count how many blocks for file
    while r > 0:
        while r > 0 and disk[r] == '.':
            r -= 1

        print(f'analizando r: {r}')

        id = disk[r]
        blocks = 0
        while r > 0 and disk[r] == id:
            r -= 1
            blocks += 1
        
        space = 0
        spacePos = 0
        for l in range(0, r):
            if disk[l] == '.':
                if space == 0:
                    spacePos = l
                space += 1
                continue
            
            if space < blocks:
                space = 0
            else:
                for i in range(spacePos, spacePos + blocks):
                    disk[i] = id
                
                i = r + 1
                while i < len(disk) and disk[i] == id:
                    disk[i] = '.'
                    i += 1

                # print(f'movi o id: {id}')
                # for c in disk:
                #     print(c, end='')
                # print()
                break

    return disk

with open('inputs/9.txt', 'r') as file:
    for line in file:
        seq = list(map(int,line))

    disk = convertToDisk(seq)
    print('acabei de converter')
    for c in disk:
        print(c, end='')
    print()
    cleanDisk = moveBlocksOnDisk(disk)
    print('nao da pra mover mais')
    for c in disk:
        print(c, end='')
    print()
    checkSum = calcChecksum(cleanDisk)
    print(checkSum)

