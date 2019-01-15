import math
import random
from PIL import Image
imgx = 500
imgy = 500
image = Image.new("L", (imgx, imgy))
pixels = image.load()
n = random.randint(0, 100)  # random number of seed points
m = 0
seedsX = [random.randint(0, imgx - 1) for i in range(n)]
seedsY = [random.randint(0, imgy - 1) for i in range(n)]
maxDist = 0.0

for ky in range(imgy):
    for kx in range(imgx):
        dists = [math.hypot(seedsX[i] - kx, seedsY[i] - ky) for i in range(n)]  # list of distances to all seed points
        dists.sort()
        if dists[m] > maxDist:
            maxDist = dists[m]
        pixels[kx, ky] = int(round(255 * (dists[m] / maxDist)))

image.save("voronoi_noise.png", "PNG")

