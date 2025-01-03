from itertools import product as lister

f = open("input")

lines = f.readlines()
f.close()

solns = [i[:i.index(':')] for i in lines]
eqns = [i[i.index(':')+1:].rstrip('\n').split() for i in lines]

def product(j):
    mult = 1
    for k in j:
        mult = mult * k
    return mult

def operate(a, op, b):
    return eval(f'{a}{op}{b}')

def pt1():

    total = 0

    for i, j in enumerate(eqns):
        j = [int(k) for k in j]
        s = sum(j)

        if s == int(solns[i]):
            total += int(solns[i])
            continue
        elif s > int(solns[i]):
            continue
        m = product(j)
        if m == int(solns[i]):
            total += int(solns[i])
            continue
        elif m < int(solns[i]) and 1 not in j:
            continue

        listops = list(lister(['*', '+'], repeat=len(j)))
        listops = [list(k) for k in listops]
        
        found = False

        for ops in listops:
            ops.append('')

            t = []
            for m, n in enumerate(j):
                t.append(n)
                t.append(ops[m])

            o = operate(t[0], t[1], t[2])
            for m in range(3, len(t)-1, 2):
                o = operate(o, t[m], t[m+1])

            if o == int(solns[i]):
                total += o
                found = True
                break

    return total

def newoperate(a, op, b):
    if op == '|':
        r = int((str(a)+str(b)))
    else:
        r = eval(f'{a}{op}{b}')
    return r

def pt2():

    total = 0

    for i, j in enumerate(eqns):
        j = [int(k) for k in j]

        listops = list(lister(['*', '+', '|'], repeat=len(j)))
        listops = [list(k) for k in listops]
        
        found = False

        for ops in listops:
            ops.append('')

            t = []
            for m, n in enumerate(j):
                t.append(n)
                t.append(ops[m])

            o = newoperate(t[0], t[1], t[2])
            for m in range(3, len(t)-1, 2):
                o = newoperate(o, t[m], t[m+1])

            if o == int(solns[i]):
                total += o
                found = True
                break

    return total

print(pt2())