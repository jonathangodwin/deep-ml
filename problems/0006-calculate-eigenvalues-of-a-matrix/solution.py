def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0] + matrix[1][1]
	det_mat = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	delta = trace**2 - 4*det_mat
	eigenvalues = []
	
	if delta >= 0 : 
		lambda1 = (trace+ delta**(0.5))/2
		lambda2 = (trace - delta**(0.5))/2
		eigenvalues = [lambda1, lambda2]
		eigenvalues.sort(reverse = True)

	return eigenvalues