from collections import defaultdict
import math
data=initial_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
def _isvalid(data):
    rowlist = [set() for i in range(9)]
    collist = [set() for i in range(9)]
    glist = [set() for i in range(9)]

    for i,row in enumerate(data):
        for j,col in enumerate(row):
            if col !=0:
                if col in rowlist[i]:
                    return False
                else:
                    rowlist[i].add(col)
                if col in collist[j]:
                    return False
                else:
                    collist[j].add(col)
                gridindex=math.floor(i/3)*3+ math.floor(j/3)
                # print(f'{i},{j},{gridindex}')
                if col in glist[gridindex]:
                    return False
                else:
                    glist[gridindex].add(col)
    return True
print(_isvalid(data))