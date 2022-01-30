import numpy as np

X = np.array([[0, 1], [1, 0]], dtype='float')
Z = np.array([[1, 0], [0, -1]], dtype='float')
H = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]], dtype='float')
CX = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype='float')
CZ = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]], dtype='float')
Swap = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype='float')
