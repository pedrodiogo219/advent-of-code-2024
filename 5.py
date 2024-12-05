
needs = {}
ans = 0

def checkSequence(line):
    seq = list(map(int, line.split(',')))
    vis = set()
    # print(f'checkin sequence {line}')

    for n in seq:
        # print(f'analyzing n: {n}')
        if n not in needs:
            vis.add(n)
            continue
        for pre in needs[n]:
            if (pre not in vis) and (pre in seq):
                return 0
        vis.add(n)

    if len(seq) % 2 == 0:
        print("EH PAR EH PAR EH PAR")

    return seq[len(seq)//2]


with open('inputs/5.txt', 'r') as file:
    while True:
        line = file.readline().strip()
        if not line or line == '':
            break
        
        a, b = list(map(int, line.split('|')))
        if b not in needs:
            needs[b] = []
        needs[b].append(a)

    
    while True:
        line = file.readline().strip()
        if not line or line == '':
            break
        
        ans += checkSequence(line)

    print(ans)

        

    