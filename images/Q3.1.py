from skimage import io
import matplotlib.pyplot as plt

A = io.imread('grizzlypeak.jpg')
(height, width, channel) = A.shape
for i in range(height):
    for j in range(width):
        for c in range(channel):
            if A[i, j, c] <= 50:
                A[i, j, c] = 0

plt.imshow(A)
plt.show()