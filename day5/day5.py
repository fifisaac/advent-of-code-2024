f = open("input")

lines = f.readlines()

rules = [i.rstrip('\n').split('|') for i in lines[:lines.index('\n')]]
pages = [i.rstrip('\n').split(',') for i in lines[lines.index('\n') + 1:]]


def pagesetchecker(pageset):

    for i, page in enumerate(pageset):
        afterpages = [j[1] for j in rules if j[0] == page]
        
        for j in afterpages:
            if j in pageset[:i]:
                return False
            else:
                good = True

    return good


def getgoodsets():

    goodpagesets = []

    for pageset in pages:
        if pagesetchecker(pageset):
            goodpagesets.append(pageset)
    
    return goodpagesets


def pt1(goodpagesets):

    total = 0

    for i in goodpagesets:
        total += int(i[len(i) // 2])
    
    return total


goodpagesets = getgoodsets()

print(f'Part 1: {pt1(goodpagesets)}')


def reorder(pageset):

    for i, page in enumerate(pageset):
        afterpages = [j[1] for j in rules if j[0] == page]

        for j in afterpages:
            if j in pageset[:i]:
                del pageset[pageset.index(j)]
                pageset.insert(i+1, j)

    return pageset
            

def pt2():

    badpagesets = [i for i in pages if i not in goodpagesets]

    newpagesets = []

    for i in badpagesets:
        while not pagesetchecker(i):
            reorder(i)
        newpagesets.append(reorder(i))

    total = 0

    for i in newpagesets:
        total += int(i[len(i) // 2])
    
    return total


print(f'Part 2: {pt2()}')