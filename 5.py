
needs = {}
ans = 0

def fixSequence(line, order):
    seq = list(map(int, line.split(',')))
    newSequence = [n for n in order if n in seq]
    print(newSequence)
    return newSequence[len(newSequence)//2]

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


def topoSort(g, seq):
    seq = set(seq)

    vis = set()
    order = []

    def dfs(u):
        # print(f'entering u: {u}')
        if u in vis:
            return
        
        vis.add(u)
        if u in g:
            for v in g[u]:
                if v not in vis and v in seq:
                    dfs(v)

        
        order.append(u)

    for u in g.keys():
        if u in seq:
            dfs(u)
    
    return order

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
        
        seq = list(map(int, line.split(',')))

        order = topoSort(needs, seq)

        aux = checkSequence(line)
        if aux == 0:
            aux = fixSequence(line, order)
            ans += aux
        else:
            print(f'for seq {line} the middle is {aux}')


    print(ans)

        

    