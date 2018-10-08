import numpy as np
from PIL import Image

g_scale_high = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
g_scale_low = '@%#*+=-:. '


def get_average_l(image):
    img = np.array(image)
    w, h = img.shape
    return np.average(img.reshape(w * h))


def covert_image_to_ascii(fileName, cols, scale, moreLevels):
    global g_scale_high, g_scale_low
    image = Image.open(fileName).convert('L')
    image_width, image_height = image.size[0], image.size[1]
    tile_width = image_width / cols
    tile_height = tile_width / scale
    rows = int(image_height / tile_height)
    if cols > image_width or rows > image_height:
        print("Obraz jest za mały dla podanej liczby kolumn!")
        exit(0)

    aimg = []
    for j in range(rows):
        y1 = int(j * tile_height)
        y2 = int((j + 1) * tile_height)
        if j == rows - 1:
            y2 = image_height
        aimg.append("")
        for i in range(cols):
            x1 = int(i * tile_width)
            x2 = int((i + 1) * tile_width)
            if i == cols - 1:
                x2 = image_width
            img = image.crop((x1, y1, x2, y2))
            avg = int(get_average_l(img))
            if moreLevels:
                gsval = g_scale_high[int((avg * 69) / 255)]
            else:
                gsval = g_scale_low[int((avg * 9) / 255)]
            aimg[j] += gsval

    return aimg


def start_converting(file, low_grayscale):
    low_grayscale = low_grayscale
    imgFile = file
    outFile = file.split('.')[0] + '.txt'
    scale = 0.43
    cols = Image.open(imgFile).size[0]

    aimg = covert_image_to_ascii(imgFile, cols, scale, low_grayscale)

    f = open(outFile, 'w')
    for row in aimg:
        f.write(row + '\n')
    f.close()
