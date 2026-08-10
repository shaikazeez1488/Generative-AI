import numpy as np

# Input two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
print("\nAddition (A + B):")
print(A + B)

# Matrix Subtraction
print("\nSubtraction (A - B):")
print(A - B)

# Matrix Multiplication
print("\nMultiplication (A × B):")
print(np.dot(A, B))

# Matrix Transpose
print("\nTranspose of Matrix A:")
print(A.T)

# Matrix Inverse
print("\nInverse of Matrix A:")
print(np.linalg.inv(A))