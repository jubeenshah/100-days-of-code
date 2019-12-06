from operator import add
def pascalsTriangle(numRows):
    res = [[1]]
    for _ in range(1, numRows):
        map_ = map(add, [0] + res[-1], res[-1] + [0])
        res.append(list(map_))
    return res if numRows else []
        
    

pascalsTriangle(5)