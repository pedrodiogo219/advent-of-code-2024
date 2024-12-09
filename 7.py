def calc(pos, acc, n, seq):
    if pos >= len(seq):
        return n == acc
    
    thirdOperation = int(str(acc) + str(seq[pos]))
    return calc(pos+1, acc + seq[pos], n, seq) or calc(pos+1, acc * seq[pos], n , seq) or calc(pos+1, thirdOperation, n, seq)
     

total = 0
with open('inputs/mini7.txt', 'r') as file:
    for line in file:
        seq = list(map(int, ''.join(line.split(':')).split(' ') ))
        n, seq = seq[0], seq[1:]
        
        if calc(1, seq[0], n, seq):
            total += n

print(total)