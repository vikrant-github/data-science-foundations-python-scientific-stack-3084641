# %%
import numpy as np

arr = np.arange(3)
arr + 4

# %%
mat = np.arange(9).reshape((3,3))
vec = np.arange(3)
print(mat)
print(vec)
print(mat + vec)
# %%
v1 = np.arange(3)
v2 = np.arange(3).reshape((3, 1))
print(v1)
print(v2)
# %%
v1 + v2
# %%
