import re

with open('inputs/3.txt', 'r') as file:
    total = 0
    doing = True
    for line in file:
        matches = re.findall(r'(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don\'t\(\))', line)
        for match in matches:
            op, do, dont = match
            if do:
                doing = True
            if dont:
                doing = False
            if op and doing:
                s = ""
                for i in range(len(op)):
                    if op[i] == '(' or op[i] == ")":
                        s += ","
                    else:
                        s += op[i]

                a, b = list(map(int, s.split(',')[1:3]))
                total += a*b

    print(total)