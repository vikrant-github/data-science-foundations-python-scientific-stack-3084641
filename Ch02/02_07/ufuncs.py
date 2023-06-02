# %%
import numpy as np
len(dir(np))

# %%
np.sin(90) # output is in radians i.e., not in degrees
# %%
v = np.arange(-3, 3)
np.sin(v)

# %%
def relu(n):
    if n < 0:
        return 0.0
    return n

relu(-2)

# %%
relu(v) # running on vector, this will yeild an error. Solution is to vectorize
# %%

@np.vectorize
def relu(n):
    if n < 0:
        return 0.0
    return n

relu(v)
# %%
relu(-2)

# %%
relu(-2) - 7

# %%
nv = np.array([-1.0, np.nan, 1.0]) # nan i..e, not a number
np.sin(nv)
# %%
