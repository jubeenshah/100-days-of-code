def spiralMatrix(matrix):
    return matrix and [*matrix.pop(0)] + spiralMatrix([*zip(*matrix)][::-1])

spiralMatrix([
 [ 1, 2, 3,4 ],
 [ 4, 5, 6,5 ],
 [ 7, 8, 9,6 ]
])