left, right = ([], [])

frequency = {}

with open('inputs/1.txt', 'r') as file:
    for line in file:
        a, b = list(map(int, line.split()))
        left.append(a)
        right.append(b)

        if b not in frequency:
            frequency[b] = 0
        frequency[b] += 1

left.sort()
right.sort()

total = 0
similarityScore = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])
    if left[i] not in frequency:
        continue
    similarityScore += (left[i] * frequency[left[i]])
print(total) 
print(similarityScore)
