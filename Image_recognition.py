#!/usr/bin/env python
# coding: utf-8

# In[3]:


from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread
from matplotlib import cm
#from skimage.color import rgb2gray if the image is color image


# In[4]:


example_file = glob.glob(r"wint_sky.gif")[0]
im = imread(example_file, as_grey=True)
#image_gray = rgb2gray(image) to convert color image to greyscale image
plt.imshow(im, cmap=cm.gray)
plt.show()


# In[16]:


blobs_log = blob_log(im, max_sigma=30, num_sigma=10, threshold=.1)
# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
numrows = len(blobs_log)
print("Number of stars counted : " ,numrows)


# In[17]:


fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap=cm.gray)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)


# In[ ]:




