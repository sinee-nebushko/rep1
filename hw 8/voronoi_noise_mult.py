from threading import Thread
import math
import random
from PIL import Image
imgx = 900
imgy = 500
image = Image.new("L", (imgx, imgy))
pixels = image.load()
n = random.randint(0, 100)

seedsX = [random.randint(0, imgx - 1) for i in range(n)]
seedsY = [random.randint(0, imgy - 1) for i in range(n)]

imgx1 = [int(i) for i in range(0, 300)]
imgx2 = [int(i) for i in range(300, 600)]
imgx3 = [int(i) for i in range(600, 900)]
imgy1 = [int(i) for i in range(0, 500)]


def f(x, y):
    max_dist = 0.0
    m = 0
    for ky in y:
        for kx in x:
            dists = [math.hypot(seedsX[i] - kx, seedsY[i] - ky) for i in range(n)]
            dists.sort()
            if dists[m] > max_dist:
                max_dist = dists[m]
            pixels[kx, ky] = int(round(255 * (dists[m] / max_dist)))


thread1 = Thread(target=f, args=(imgx1, imgy1))
thread2 = Thread(target=f, args=(imgx2, imgy1))
thread3 = Thread(target=f, args=(imgx3, imgy1))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

image.save("voronoi_noise_mult.png", "PNG")
