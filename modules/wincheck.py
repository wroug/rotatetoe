from copy import *

example = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
]


patterns = [
    [(0, 0), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)]
]

def wincheck(datain):
    data = deepcopy(datain)
    tmp_data = [list(col) for col in zip(*data)]
    tmp_data.append(tmp_data[0])
    tmp_data.append(tmp_data[1])
    data = [list(row) for row in zip(*tmp_data)]
    safedata = deepcopy(data)
    safedata.append([" "]*len(data[0]))
    safedata.append([" "]*len(data[0]))
    tmp_data = [list(col) for col in zip(*safedata)]
    safedata.append([" "] * len(data[0]))
    safedata.append([" "] * len(data[0]))
    safedata = [list(row) for row in zip(*tmp_data)]

    for rownum in range(len(data)):
        row = safedata[rownum]
        for cellnum in range(len(row)):
            cell = row[cellnum]
            for patternnum in range(len(patterns)):
                pattern = patterns[patternnum]
                if safedata[rownum+pattern[0][0]][cellnum+pattern[0][1]] == safedata[rownum+pattern[1][0]][cellnum+pattern[1][1]] == safedata[rownum+pattern[2][0]][cellnum+pattern[2][1]] and safedata[rownum+pattern[0][0]][cellnum+pattern[0][1]] != " ":
                    if safedata[rownum+pattern[0][0]][cellnum+pattern[0][1]] == 'X':
                        return "X"
                    elif safedata[rownum+pattern[0][0]][cellnum+pattern[0][1]] == 'O':
                        return "O"
                    else:
                        return " "
                else:
                    return " "
