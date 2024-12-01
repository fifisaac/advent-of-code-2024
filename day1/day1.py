with open("input") as f:
    lines = f.readlines()

left = sorted([i.split()[0] for i in lines])
right = sorted([i.split()[1] for i in lines])

def pt1():

    total = 0

    for i, j in enumerate(left):
        total += abs(int(j) - int(right[i]))

    return total


def pt2():

    total = 0

    for i, j in enumerate(left):
        mult = right.count(j)
        total += int(j) * mult
    
    return total


print(pt1())
print(pt2())