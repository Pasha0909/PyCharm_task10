from PIL import Image
import numpy as np

def get_illumination(pixels, p_x, p_y, size):
    summa = np.sum(pixels[p_x: p_x + size, p_y: p_y + size])
    result = int(summa // 3)
    return int(result // (size * size))

def install_color(pixels, illumination, size, p_x, p_y, step):
    pixels[p_x: p_x + size, p_y: p_y + size] = int(illumination // step) * step

def get_gray(pixels, gradation, size):
    step = 255 // (gradation - 1)
    hei = len(pixels)
    wid = len(pixels[1])
    for y in range(0, hei, size):
        for x in range(0, wid, size):
            illumination = get_illumination(pixels, x, y, size)
            install_color(pixels, illumination, size, x, y, step)
    return pixels
img = Image.open('img2.jpg')
pixels = np.array(img)
size_mosaics = 10
gradation = 50
res = Image.fromarray(get_gray(pixels, gradation, size_mosaics))
res.save('res1.jpg')