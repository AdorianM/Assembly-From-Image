from msilib.schema import Error
from PIL import Image, UnidentifiedImageError
from sys import exit, argv
from os import path

def print_and_quit(message):
    print(message)
    input("Press anything to quit...")
    exit()

def path_to_basename(file_path):
    return path.splitext(file_path)[0]

def write_hexels_to_file(fileName, hexels, width, height):
    outputName = fileName + '.inc'
    variableName = "var" + fileName
    f = open(outputName, "w")
    if f:
        f.write(variableName + " DD ")
        for y in range(height):
            if y != 0:
                f.write(" "*len(variableName) + " DD ")
            for x in range(width - 1):
                f.write(hexels[height*x + y])
                f.write(", ")
            f.write(hexels[height*x + y])
            f.write("\n")
    else:
        print_and_quit("Error writing to file")
    

def get_pixels_to_hex(pixels, width, height):
    hexels = []
    
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            hexel = "0"
            try:
                for color in pixel[:3]:
                    hexVal = "{:02x}".format(color)
                    hexel += hexVal
            except IndexError:
                print_and_quit("Error: Color index out of bounds. Image is not RGB")
            hexel += 'h'
            hexels.append(hexel)
    return hexels

def img2bytes(imgPath, imgName):
    try:
        im = Image.open(imgPath)
        pixels = im.load()
        x = im.size[0]
        y = im.size[1]
        hexels = get_pixels_to_hex(pixels, x, y)
        write_hexels_to_file(imgName, hexels, x, y)
    except FileNotFoundError:
        print_and_quit("The specified file path is incorrect")
    except UnidentifiedImageError:
        print_and_quit("The provided file is either not an image or corrupt")
    except Exception as e:
        print_and_quit("An error occurred: " + str(e))

def main():
    if len(argv) > 1:
        imgPath = argv[1]
        imgName = path_to_basename(imgPath)

        img2bytes(imgPath, imgName)

        print_and_quit("File " + imgName + " successfully created")

    print_and_quit("Drag & drop a file on the executable to produce the assembly data output")
    

if __name__ == "__main__":
    main()