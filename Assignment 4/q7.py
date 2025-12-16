def matrix_operations(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])

    add_result = []
    sub_result = []

    for i in range(rows):
        add_row = []
        sub_row = []
        for j in range(cols):
            add_row.append(mat1[i][j] + mat2[i][j])
            sub_row.append(mat1[i][j] - mat2[i][j])
        add_result.append(add_row)
        sub_result.append(sub_row)

    return add_result, sub_result



matrix1 = [
    [2, 8, 3, 4],
    [5, 5, 7, 8],
    [9, 11, 13, 12]
]

matrix2 = (
    (13, 15, 11, 9),
    (6, 8, 6, 5),
    (5, 3, 2, 1)
)

addition, subtraction = matrix_operations(matrix1, matrix2)

print("Matrix Addition:")
for row in addition:
    print(row)

print("\nMatrix Subtraction:")
for row in subtraction:
    print(row)