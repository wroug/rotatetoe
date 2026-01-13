from copy import *

example = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
]



def wincheck(datain):
    patterns = [
        [(0, 0), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]
    xwin, owin = 0, 0
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
        for cellnum in range(len(data[0])):
            for pattern in patterns:
                try:
                    a, b, c = pattern
                    vals = [safedata[rownum + a[0]][cellnum + a[1]],
                            safedata[rownum + b[0]][cellnum + b[1]],
                            safedata[rownum + c[0]][cellnum + c[1]]]
                    if vals[0] != " " and vals[0] == vals[1] == vals[2]:
                        if vals[0] == 'X':
                            xwin += 1
                        elif vals[0] == 'O':
                            owin += 1
                except IndexError:
                    continue

    return xwin, owin
