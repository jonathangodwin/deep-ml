from statistics import mean

def compute_distance_from_mean(X) : 
    return [x - mean(X) for x in X]



def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n, m = len(vectors), len(vectors[0])
    distances_from_means = [compute_distance_from_mean(distance) for distance in vectors]
    var_cov_matrix = [[0] * n for _ in range(n)]

    for i in range(n) : 
       print(f"Pour la population X{i} = {vectors[i]},\nLa distance à la moyenne est ==> {distances_from_means[i]}")
       var_cov_matrix[i][i] =  sum(current_value**2 for current_value in distances_from_means[i]) / (m-1)
       for j in range(i+1, n) : 
        current_covariance = sum(c1 * c2 for c1, c2 in zip(distances_from_means[j], distances_from_means[i])) /(m-1)
        var_cov_matrix[i][j] = current_covariance # The upper matrix value
        var_cov_matrix[j][i] = current_covariance # The lower matrix value
        print (f"Cov(X{i}, X{j}) = {var_cov_matrix[i][j]}")
       print("---------------------------------------------------------------")

    return var_cov_matrix