import numpy as np

def compute_jacobi_matrix (A : np.ndarray) -> np.ndarray : 
    B = np.dot(np.transpose(A), A)
    a,b,d = B[0,0], B[0, 1], B[1, 1]
    thetha = np.arctan(2*b / (a-d)) / 2
    
    return np.array([np.cos(thetha), np.sin(thetha)])

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    J = compute_jacobi_matrix (A)
    B = np.dot(np.transpose(A), A)
    V = np.array ([[J[0], -J[1]], [J[1], J[0]]])
    rotation = np.dot (np.transpose(V), np.dot(B,V))
    S = np.array([np.sqrt(rotation[0, 0]), np.sqrt(rotation[1, 1])])
    U = np.zeros((2, 2))
    U[:, 0] = np.dot(A, V[:, 0]) / S[0]
    U[:, 1] = np.dot(A, V[:, 1]) / S[1]

    return U, np.sort(S)[::-1], np.transpose(V)
