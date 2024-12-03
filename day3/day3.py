import re

f = open("input")
txt = f.read()

def mulall():

    total = 0

    muls = [i[4:].rstrip(')').split(',') for i in re.findall("mul\(\d+,\s*\d+\)", txt)]

    for i in muls:
        total += int(i[0]) * int(i[1])

    return total

def dontmulall():

    total = 0

    dos = re.finditer("do\(\)", txt)
    donts = re.finditer("don't\(\)", txt)

    dopos = [i.end() for i in dos]
    dontpos = [i.end() for i in donts]

    switch = [0]
    lastdont = False
    i = 0
    j = 0

    while i < len(dopos) and j < len(dontpos):

        if not lastdont:
            if dontpos[j] > switch[-1]:
                switch.append(dontpos[j])
                lastdont = True
            else:
                j += 1
        else:
            if dopos[i] > switch[-1]:
                switch.append(dopos[i])
                lastdont = False
            else:
                i += 1

    muls = {i.end(): i.group()[4:].rstrip(')').split(',') for i in re.finditer("mul\(\d+,\s*\d+\)", txt)}

    if len(switch) % 2 != 0:
        switch.append(99999999999999999999999999) # hopefully there can't be a file this long, janky solution

    for i in muls.keys():

        for j in range(0, len(switch) - 1, 2):
            if i in range(switch[j], switch[j+1]):
                total += int(muls[i][0]) * int(muls[i][1])

    return total


print(f'Part 1: {mulall()}')
print(f'Part 2: {dontmulall()}')