f = open("input")

lines = [list(i.rstrip('\n')) for i in f.readlines()]

# pad edges with '-'
for i in lines:
    i.append('-')
    i.insert(0, '-')

lines.append(['-' for i in lines[0]])
lines.insert(0, ['-' for i in lines[0]])

def checkforward(current, direc, positions, counter):

    mult = 1
    forward = lines[current['y'] + mult*direc['y']][current['x'] + mult*direc['x']]

    while forward == '.' or forward == '^':
        if {'x': current['x'] + (mult)*direc['x'] , 'y': current['y'] + (mult)*direc['y']} not in positions:
            positions.append({'x': current['x'] + (mult)*direc['x'] , 'y': current['y'] + (mult)*direc['y']})
        mult += 1

        forward = lines[current['y'] + mult*direc['y']][current['x'] + mult*direc['x']]

    if forward == '-':
        return 0
    elif forward == '#':

        options = [{'x': 0, 'y': -1}, {'x': 1, 'y': 0}, {'x': 0, 'y': 1}, {'x': -1, 'y': 0}]
        newdirec = options[(options.index(direc) + 1) % 4]

        counter += 1

        if counter > 995:
            print(counter)
            return 1

        checkforward({'x': current['x'] + (mult-1)*direc['x'] , 
                        'y': current['y'] + (mult-1)*direc['y']}, newdirec, positions, counter)


    return 0


def pt1():

    for i, j in enumerate(lines):
        if '^' in j:
            current = {'x': j.index('^'), 'y': i}
    
    direction = {'x': 0, 'y': -1}
    positions = [current]
    checkforward(current, direction, positions, 0)

    return positions

positions = pt1()
print(f'Part 1: {len(positions)}')

def pt2():
    total = 0

    for i in positions:

        #print(i)

        for j, k in enumerate(lines):
            if '^' in k:
                current = {'x': k.index('^'), 'y': j}

        direction = {'x': 0, 'y': -1}
        newpositions = []
        hits = []
        counter = 0

        newlines = lines
        if newlines[i['y']][i['x']] != "^":
            newlines[i['y']][i['x']] = "#"

        total += checkforward(current, direction, [], counter)


    #print(hits)
            #total += 1

        # for i in hits:
        #     if hits.count(i) > 1:
        #         total += 1
        #         break

    print(total)
        

pt2()