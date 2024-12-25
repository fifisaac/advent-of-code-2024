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

    for i, j in enumerate(disk[::-1]):
        if j != '.':
            for k, l in enumerate(disk):
                if l == '.':
                    disk[k] = j
                    moves += 1
                    break

    print(disk[:-moves])

    return disk[:-moves]

def checkDisk(disk):

    total = 0

    for i, j in enumerate(disk):
        if j != '.':
            total += i * j
    
    return total

# disk = createDisk()
# print(disk)
# print(checkDisk(moveBlocks(disk)))

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

def rearrange(disk):

    newDisk = list(disk)

    for i in range(len(disk)):
        item = disk.pop()
        if item[0] != '.':
            for i, j in enumerate(newDisk):
                if j[0] == '.'  and j[1] >= item[1] and i < newDisk.index(item):
                    newDisk[newDisk.index(item)] = ['.', item[1]]
                    newDisk.insert(i, item)
                    newDisk[i+1][1] += -item[1]
                    break

    

    finalDisk = []

    for i in newDisk:
        for j in range(0, i[1]):
                finalDisk.append(i[0])

    print(finalDisk)
    
    return finalDisk


disk = runLengthEncode(createDisk())
print(checkDisk(rearrange(disk)))