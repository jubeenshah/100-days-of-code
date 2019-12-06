from operator import add
def pascalsTriangleDos(rowIndex):
    result = [[1]]
    for _ in range(rowIndex):
        map_ = map(add, [0] +result[-1],result[-1]+[0])
        result.append(list(map_))
    return result[rowIndex] if rowIndex else [[1]]
pascalsTriangleDos(2)