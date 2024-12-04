f = open("input")

lines = f.readlines()

# PART ONE
def checkchar(char, direc):

    nextchardict = {'X' : 'M',
                'M' : 'A',
                'A' : 'S'}

    x = direc[0]
    y = direc[1]

    if (char[2] + y >= 0) and (char[1] + x >=0) and char[2] + y < len(lines) and char[1] + x < len(lines[char[2] + y]):
        nextchar = lines[char[2] + y][char[1] + x] 
    else:
        return 0

    if nextchardict[char[0]] == nextchar:
        if nextchar == 'S':
            return 1
        else:
            return checkchar((nextchar, char[1] + x, char[2] + y), (x,y))
    
    return 0

def xfinder():

    total = 0

    locX = []

    for y, i in enumerate(lines):
        for x, j in enumerate(i):
            if i[x] == 'X':
                locX.append((j, x,y))

    for i in locX:
    
        for x in range(-1,2):
            for y in range(-1,2):
                
                total += checkchar(i, (x, y))

    return total

print(f'Part 1: {xfinder()}')

# PART TWO
def checkmas(char, direc):

    x = direc[0]
    y = direc[1]

    try:
     if (char[2] + y >= 0) and (char[1] + x >=0) and (char[1] - x >=0) and (char[2] + y >= 0):
        diag1 = lines[char[2] + y][char[1] + x]
        diag2 = lines[char[2] - y][char[1] - x]

        if diag1 in ['S', 'M'] and diag2 in ['S', 'M'] and diag2 != diag1:
            diag3 = lines[char[2] - y][char[1] + x]
            diag4 = lines[char[2] + y][char[1] - x]
            if diag3 in ['S', 'M'] and diag4 in ['S', 'M'] and diag3 != diag4:
                return 1
    except:
        pass
    
    return 0
            
def afinder():

    total = 0

    locA = []

    for y, i in enumerate(lines):
        for x, j in enumerate(i):
            if i[x] == 'A':
                locA.append((j, x,y))

    for i in locA:

        total += checkmas(i, (-1,-1))
    
    return total

print(f'Part 2: {afinder()}')