def isIncreasing(v):
  for i in range(1, len(v)):
    if v[i-1] >= v[i] or abs(v[i] - v[i-1]) > 3:
      return False
  return True

def isDecreasing(v):
  for i in range(1, len(v)):
    if v[i-1] <= v[i] or abs(v[i] - v[i-1]) > 3:
      return False
  return True

def isSafe(v):
  if isIncreasing(v) or isDecreasing(v):
    return True
  for i in range(0, len(v)):
    newV = v[:i] + v[i+1:]
    if isIncreasing(newV) or isDecreasing(newV):
      return True

  return False

with open('inputs/2.txt', 'r') as file:
    safe = 0
    for line in file:
        record = list(map(int, line.split()))
        if isSafe(record):
          print(record, "safe")
          safe += 1
        else:
          print(record, "unsafe")

    print(safe)

