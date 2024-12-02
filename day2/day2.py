with open("input") as f:
    lines = f.readlines()

items = [i.split() for i in lines]

def pt1():

    total = 0

    for i in items:

        safe = True

        if int(i[0]) - int(i[1]) > 0:
            increasing = False
        else:
            increasing = True

        for j in range(0, len(i) - 1):

            diff = int(i[j]) - int(i[j+1])
        
            if increasing and diff >= 0:
                safe = False
            elif not increasing and diff <= 0:
                safe = False

            if abs(diff) > 3:
                safe = False

        if safe:
            total += 1

    return total


def pt2():
    pass



print(f'Part 1: {pt1()}')
print(f'Part 2: {pt2()}')