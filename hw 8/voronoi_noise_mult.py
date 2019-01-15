from threading import Thread
import math
import random
from PIL import Image, ImageDraw
imgx = 900
imgy = 500
image = Image.new("L", (imgx, imgy),0)
draw = ImageDraw.Draw(image)
pixels = image.load()
n = random.randint(0, 100)  # random number of seed points
m = 0
seedsX = [random.randint(0, imgx - 1) for i in range(n)]
seedsY = [random.randint(0, imgy - 1) for i in range(n)]
maxDist = 0.0


def f(maxDist):
    for ky in range(imgy):
        for kx in range(imgx):
            dists = [math.hypot(seedsX[i] - kx, seedsY[i] - ky) for i in
                     range(n)]  # list of distances to all seed points
            dists.sort()
            if dists[m] > maxDist:
                maxDist = dists[m]  # find max distance
            pixels[kx, ky] = int(round(255 * (dists[m] / maxDist)))


thread1 = Thread(target=f, args=(imgx, imgy))
thread2 = Thread(target=f)
thread3 = Thread(target=f)
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()

image.save("WorleyNoiseIM12.png", "PNG")
