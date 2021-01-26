from skimage import io, img_as_float32
import matplotlib.pyplot as plt
import numpy as np

I =  io.imread('gigi.jpg')
I[I<50] = 50
I = I - 50
I = img_as_float32(I)
plt.imshow(I)
plt.show()
##plt.savefig('gigi_reduced.jpg')