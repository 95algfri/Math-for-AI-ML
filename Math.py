import numpy as np
from scipy.linalg import solve

A = np.array([[3, 2, -1, 4, 5],
              [1, 1, 3, 2, -2],
              [4, -1, 2, 1, 0],
              [3, 1, -2, 5, 0],
              [4, 2, 1, -3, 3]])

B = np.array([12, 5, 7, 9, 10])

solution = solve(A, B)

print(solution)
