from PIL import Image

imageSize = (2560, 1440)

def mandlebrot(x, y, max_iterations = 31):
    (c, z) = (complex(x, y), 0)
    for i in range(max_iterations):
        z = z ** 2 + c
        if z.imag ** 2 + z.real ** 2 > 4:
            return i + 1
    return 0


image = Image.new('RGB', imageSize)
pixels = image.load()

for x in range(imageSize[0]):
    for y in range(imageSize[1]):
        # This involved some trial and error to center the graph.
        cordx = (x - imageSize[0] / 2 - 0.3 * imageSize[1]) / (imageSize[1] * 0.5)
        cordy = (y - imageSize[1] / 2) / (imageSize[1] * 0.5)
        # We'll just vary the red.
        pixels[x, y] = (mandlebrot(cordx, cordy) * 8, 0, 0)

image.save('fractal.png')
image.close()
