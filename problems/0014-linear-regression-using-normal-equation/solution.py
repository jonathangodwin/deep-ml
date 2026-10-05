import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	cov_matrix = np.dot(np.transpose(X), X)
	return np.dot(np.linalg.inv(cov_matrix), np.dot(np.transpose(X), y))