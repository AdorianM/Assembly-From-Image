from PIL import Image
from sys import exit, argv

def write_hexels_to_file(filePath, hexels, width, height):
    f = open(filePath, "w")
    f.write("picture DD ")

    for y in range(height):
        if y != 0:
            f.write("        DD ")
        for x in range(width - 1):
            f.write(hexels[height*x + y])
            f.write(", ")
        f.write(hexels[height*x + y])
        f.write("\n")

def get_pixels_to_hex(pixels, width, height):
    hexels = []
    
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            hexel = "0"
            for color in pixel[:3]:
                hexVal = "{:02x}".format(color)
                hexel += hexVal
            hexel += 'h'
            hexels.append(hexel)
    return hexels

def img2bytes(imgPath, filePath):
    im = Image.open(imgPath)
    pixels = im.load()
    x = im.size[0]
    y = im.size[1]
    hexels = get_pixels_to_hex(pixels, x, y)
    write_hexels_to_file(filePath, hexels, x, y)

def main():
    img2bytes(argv[1], "asm_image.inc")
    exit("Done")

if __name__ == "__main__":
    main()