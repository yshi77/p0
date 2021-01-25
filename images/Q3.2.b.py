from skimage import io
import time

sum = 0
for i in range(10):
    A = io.imread('grizzlypeak.jpg')
    start = time.time()
    A[A<=50] = 0
    end = time.time()
    sum += (end - start)
average_time = sum / 10
print(average_time)