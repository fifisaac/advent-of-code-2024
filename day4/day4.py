# failed solution i want to come back to
# need to figure out how to get an array of the diagonals

f = open("input")

mainwordsearch = f.readlines()

def finder(wordsearch):

    count = 0

    for i in wordsearch:
        count += i.count('XMAS')
        count += i.count('SAMX')

    return count


def pt1():

    total = 0

    # horizontal
    total += finder(mainwordsearch)

    #vertical
    verticalwordsearch = [''.join([mainwordsearch[j][i] for j in range(0, len(mainwordsearch[1])-1)]) for i in range(0, len(mainwordsearch))]

    total += finder(verticalwordsearch)

    diagonalwordsearch = []

    for i in range(0, len(mainwordsearch)):

        string1 = ''
        string2 = ''

        for j in range(0, len(mainwordsearch)):

            if mainwordsearch[j][j-i] != '\n':
                string1 += (mainwordsearch[j][j-i])
                #string2 += (mainwordsearch[j][i-j])
            else:
                break

        diagonalwordsearch.append(string1)
        diagonalwordsearch.append(string2)

    print(diagonalwordsearch)

    total += finder(diagonalwordsearch)


    return total

print(pt1())

