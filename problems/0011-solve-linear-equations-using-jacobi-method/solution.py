import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list: 
    rowsA, colsA = A.shape[0], A.shape[1]
    X = np.zeros(colsA, dtype=np.float64)
    for k in range (n) : 
        currentX = X.copy()
        for i in range (rowsA) : 
            a = np.array(0.0, dtype=np.float64)
            for j in range (colsA) : 
                if i != j :
                    a += A[i, j] * currentX[j]
            X[i] = (b[i] - a) / A[i, i]

    return np.round(X, 4)