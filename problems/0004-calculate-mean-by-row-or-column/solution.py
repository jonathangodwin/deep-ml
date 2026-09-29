def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    rows, cols = len(matrix), len(matrix[0])
    means = []
    if mode == 'column' : 
        for j in range (cols) : 
            s = 0
            
            for i in range(rows) : 
                s += matrix[i][j]
            means.append(s / rows)
    else : 
        for i in range (rows) : 
            s = 0

            for j in range(cols) : 
                s += matrix[i][j]
            means.append(s / cols)

    return means

matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
print (calculate_matrix_mean(matrix, 'row'))