with open("input") as f:
    lines = f.readlines()

items = [i.split() for i in lines]

def isSafe(item):

    safe = True

    if int(item[0]) - int(item[1]) > 0:
        increasing = False
    else:
        increasing = True

    for j in range(0, len(item) - 1):

        diff = int(item[j]) - int(item[j+1])
    
        if increasing and diff >= 0:
            safe = False
        elif not increasing and diff <= 0:
            safe = False

        if abs(diff) > 3:
            safe = False

    return safe
    

def pt1():

    total = 0

    for i in items:

        if isSafe(i):
            total += 1

    return total


def pt2():

    total = 0

    for i in items:

        for j in range(0, len(i)):

            missing = i[:j] + i[(j+1):]

            if isSafe(missing):
                total += 1
                break

    return total


print(f'Part 1: {pt1()}')
print(f'Part 2: {pt2()}')