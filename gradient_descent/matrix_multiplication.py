# To use the '@' operator, a class must define __matmul__

# Ex: NumPy Arrays
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
             [9, 10],
             [11, 12]])
C = A@B
print(C)


# Ex: Torch Tensors
import torch
A = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
B = torch.tensor([[7, 8],
                  [9, 10],
                  [11, 12]])
C = A@B
print(C)
