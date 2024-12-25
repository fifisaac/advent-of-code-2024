f = open("input")

diskmap = list(f.read().rstrip('\n'))

def createDisk():

    disk = []

    for i in range(0, len(diskmap), 2):
        disk += [i // 2 for j in range(int(diskmap[i]))]
        if i+1 < len(diskmap):
            disk += ['.' for j in range(int(diskmap[i+1]))]

    return disk

def moveBlocks(disk):

    moves = 0

    for i in range(len(disk)):
        if disk[-i] == '.' and disk[-i] != disk[i]:
            back = i + 1
            continue
        else:
            back = i
        if disk[i] == '.' and disk[-back] != '.':
            disk[i] = disk[-back]
            disk[-back] = '.'
            print(disk)

    return disk

def checkDisk(disk):

    total = 0

    for i, j in enumerate(disk):
        total += i * int(j)
    
    return total

disk = createDisk()
print(len(disk))
print(checkDisk(moveBlocks(disk)))

def runLengthEncode(disk):

    encoDisk = []
    count = 1
    curr = ''
    
    for i, j in enumerate(disk):
        #print(curr, i)
        if curr != j:
            if curr != '':
                encoDisk.append([curr, count])
            curr = j
            count = 1
        else:
            count += 1
    
    encoDisk.append([curr, count])

    return encoDisk

print(runLengthEncode)