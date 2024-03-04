import numpy as np
from PIL import Image

# Loading the image as an Image object using the Pillow's Image.open function.
img = Image.open("../Files/confidential.jpg")

# Loading the image's pixels
pixels = img.load()

# Array to store the coords from the 5ecr3t_c0de.txt
coords = []

# Reading the coords as a tuple from the 5ecr3t_c0de.txt
with open("5ecr3t_c0de/5ecr3t_c0de.txt", "r") as key:
    for line in key.readlines():
        x,y = line.strip().rstrip(")").lstrip("(").split(",")
        coords.append((int(x), int(y)))

# Changing all the pixels at the given coords into white (I decided to use white since the background was black so it would be most visible)
for x,y in coords:
    pixels[x,y] = (255,255,255)

# Saving the image
img.save("decoded.jpg")