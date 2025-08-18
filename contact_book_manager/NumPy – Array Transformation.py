import numpy as np

def reshape_and_rotate(arr):
    n = len(arr)
    root = int(n ** 0.5)
    
    if root * root != n:
        return -1  # Not a perfect square
    
    mat = arr.reshape((root, root))
    # Rotate 90 degrees clockwise = Transpose + reverse each row
    rotated = np.array([row[::-1] for row in mat.T])
    
    return rotated

# Example
arr = np.array([1,2,3,4,5,6,7,8,9])
print(reshape_and_rotate(arr))
