from skimage import io
import time

sum = 0
for i in range(10):
    A = io.imread('grizzlypeak.jpg')
    start = time.time()
    (height, width, channel) = A.shape
    for i in range(height):
        for j in range(width):
            for c in range(channel):
                if A[i, j, c] <= 50:
                    A[i, j, c] = 0
    end = time.time()
    sum += (end - start)
average_time = sum / 10
print(average_time)