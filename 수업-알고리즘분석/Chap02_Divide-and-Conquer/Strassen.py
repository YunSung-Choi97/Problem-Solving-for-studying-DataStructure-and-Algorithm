import numpy as np

def strassen(n, A, B, C):
    threshold = 2
    half_n = n // 2  # 여러번 계산되는 값이라 변수에 저장

    A11 = np.array([[A[rows][cols] for cols in range(half_n)] for rows in range(half_n)])
    A12 = np.array([[A[rows][cols] for cols in range(half_n, n)] for rows in range(half_n)])
    A21 = np.array([[A[rows][cols] for cols in range(half_n)] for rows in range(half_n, n)])
    A22 = np.array([[A[rows][cols] for cols in range(half_n, n)] for rows in range(half_n, n)])
    B11 = np.array([[B[rows][cols] for cols in range(half_n)] for rows in range(half_n)])
    B12 = np.array([[B[rows][cols] for cols in range(half_n, n)] for rows in range(half_n)])
    B21 = np.array([[B[rows][cols] for cols in range(half_n)] for rows in range(half_n, n)])
    B22 = np.array([[B[rows][cols] for cols in range(half_n, n)] for rows in range(half_n, n)])

    # 동작 확인
    # for submatrix in [A11, A12, A21, A22, B11, B12, B21, B22]:
    #     print(submatrix)

    if (n <= threshold):
        C = np.array(A) @ np.array(B)
    else:
        M1 = M2 = M3 = M4 = M5 = M6 = M7 = np.array([])
        M1 = strassen(half_n, A11+A22, B11+B22, M1)
        M2 = strassen(half_n, A21+A22, B11, M2)
        M3 = strassen(half_n, A11, B12-B22, M3)
        M4 = strassen(half_n, A22, B21-B11, M4)
        M5 = strassen(half_n, A11+A12, B22, M5)
        M6 = strassen(half_n, A21-A11, B11+B12, M6)
        M7 = strassen(half_n, A12-A22, B21+B22, M7)

        C = np.vstack([np.hstack([M1+M4-M5+M7, M3+ M5]), np.hstack([M2+M4, M1+M3-M2+M6])])
    
    return C

n = 4
A = [[1, 2, 0, 2], [3, 1, 0, 0], [0, 1, 1, 2], [2, 0, 2, 0]]
B = [[0, 3, 0, 2], [1, 1, 4, 0], [1, 1, 0, 2], [0, 5, 2, 0]]
C = np.array(A) @ np.array(B)
D = [[0 for cols in range(n)] for rows in range(n)]
print(C)
D = strassen(n, A, B, D)
print(D)