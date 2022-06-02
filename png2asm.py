from PIL import Image
from sys import exit, argv
from os import path

def path_to_basename(file_path):
    return path.splitext(file_path)[0]

def write_hexels_to_file(fileName, hexels, width, height):
    outputName = fileName + '.inc'
    variableName = "var" + fileName
    f = open(outputName, "w")
    f.write(variableName + " DD ")

    for y in range(height):
        if y != 0:
            f.write(" "*len(variableName) + " DD ")
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

def img2bytes(imgPath, imgName):
    im = Image.open(imgPath)
    pixels = im.load()
    x = im.size[0]
    y = im.size[1]
    hexels = get_pixels_to_hex(pixels, x, y)
    write_hexels_to_file(imgName, hexels, x, y)

def main():
    if len(argv) > 1:

        imgPath = argv[1]
        imgName = path_to_basename(imgPath)

        img2bytes(imgPath, imgName)

        print("File " + imgName + " successfully created")
        input("Press anything to continue...")
        exit()

    print("Drag & drop a file on the executable to produce the assembly data output")
    input("Press anything to continue...")
    exit()
    

if __name__ == "__main__":
    main()