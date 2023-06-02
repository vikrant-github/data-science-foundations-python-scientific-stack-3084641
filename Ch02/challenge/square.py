# %%
import matplotlib.pyplot as plt

img = plt.imread('flower.png')
img = img.copy()  # make img writable
plt.imshow(img)

#%%
type(img)
# %%
img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350
# Bottom-right: 680x850
# Line width: 5
# first dimension is rows (y)
tl_x, tl_y = 350, 190 # top right x and y
br_x, br_y = 850, 680 # bottom right x and y
width = 5 # width of the image

color = [0, 0, 0xFF] # blue

# Top line
img[tl_x:tl_x+width, tl_y:br_y] = color
# Bottom line
img[br_x:br_x+width, tl_y:br_y] = color
# Left line
img[tl_x:br_x, tl_y:tl_y+width] = color
# Right line
img[tl_x:br_x, br_y-width:br_y] = color

plt.imshow(img)

# %%
