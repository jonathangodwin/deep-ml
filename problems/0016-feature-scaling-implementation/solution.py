import numpy as np

def feature_scaling(data) : 
    m, n = data.shape
    standardized_data, normalized_data = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]    
    for j in range(n) : 
        data_min, data_max = float(np.min(data[:, j])), float(np.max(data[:, j]))
        data_mean,data_std = float(np.mean(data[:, j])), float(np.std(data[:, j]))
        for i in range (m) : 
            standardized_data[i][j] = (data[i,j] - data_min) / (data_max - data_min)
            normalized_data[i][j] = (data[i, j] - data_mean) / data_std

    return normalized_data, standardized_data