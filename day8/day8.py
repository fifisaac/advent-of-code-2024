f = open("input")
lines = [list(i.rstrip("\n")) for i in f.readlines()]

coorddict = {}

for i, j in enumerate(lines):
    for k, l in enumerate(j):
        if lines[i][k] not in ['-', '.']:
            if lines[i][k] not in coorddict.keys():
                coorddict[lines[i][k]] = [[i, k]]
            else:
                coorddict[lines[i][k]].append([i,k])

def pt1():

    antinodes = []

    for i in coorddict:
        for j in coorddict[i]:
            for l in coorddict[i]:
                if (j[1] - l[1] == 0 or (j[0] - l[0]) / (j[1] - l[1])) and j != l:
                    loc = [j[0] + (j[0] - l[0]), j[1] + j[1] - l[1]]
                    if loc not in antinodes and loc[0] in range(len(lines)) and loc[1] in range(len(lines[0])):
                        antinodes.append(loc)

    return(len(antinodes))

print(f'Part 1: {pt1()}')

def pt2():

    antinodes = []

    for i in coorddict:
        for j in coorddict[i]:
            for l in coorddict[i]:
                if (j[1] - l[1] == 0 or (j[0] - l[0]) / (j[1] - l[1])) and j != l:
                    k = 0
                    loc = [j[0] + k*(j[0] - l[0]), j[1] + k*(j[1] - l[1])]
                    while loc[0] in range(len(lines)) and loc[1] in range(len(lines[0])):
                        loc = [j[0] + k*(j[0] - l[0]), j[1] + k*(j[1] - l[1])]
                        if loc not in antinodes and loc[0] in range(len(lines)) and loc[1] in range(len(lines[0])):
                            antinodes.append(loc)
                        k+=1

    return(len(antinodes))

print(f'Part 2 {pt2()}')
