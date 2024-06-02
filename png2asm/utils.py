from os import path
from msilib.schema import Error
from PIL import Image, UnidentifiedImageError
from sys import exit
import re

TOKEN_LIMIT = 48 # 50 Max Tokens - 2 Tokens for variable name and type

def print_and_quit(message):
    print(message)
    input("Press anything to quit...")
    exit()

def path_to_basename(file_path):
    return path.splitext(path.basename(file_path))[0]
    
def write_variable_to_file(file, variableName, hexels, lowLimit, highLimit, height, varSize):
    file.write("{} {} ".format(variableName, varSize))
    for y in range(height):
        if y != 0:
            file.write(" "*len(variableName) + " " + varSize + " ")
        for x in range(lowLimit, highLimit - 1):
            file.write(hexels[height*x + y])
            file.write(", ")
        file.write(hexels[height*(highLimit - 1) + y])
        file.write("\n")

def write_asm_pixels_to_file(fileName, outputPath, variableName, pArray, width, height):
    print("Writing " + fileName + " to " + outputPath)
    outputName = path.join(outputPath, fileName + '.inc')
    f = open(outputName, "w")

    if f: 
        varSize = "DD" if re.search('[a-zA-Z]', pArray[0]) else "DB"
        splitCount = width // (TOKEN_LIMIT + 1)
        for i in range(splitCount + 1):
            currentVariableName = variableName + "_" + str(i)
            lowLimit = i * TOKEN_LIMIT
            highLimit = min((i + 1) * TOKEN_LIMIT, width)

            write_variable_to_file(f, currentVariableName, pArray, lowLimit, highLimit, height, varSize)
            f.write("\n")
        f.close()
    else:
        raise Exception("Unable to open file " + outputName)

def get_pixels_to_hex(image, width, height, forceRGB=False):
    pixels = image.load()
    pArray = []
    if type(pixels[0, 0]) == int and not forceRGB:
        is8Bit = True
        for x in range(width):
            for y in range(height):
                if pixels[x, y] > 255:
                    is8Bit = False
                    break
                pixel = "{:3}".format(pixels[x, y])
                pArray.append(pixel)
        if not is8Bit:
            pArray = []
        else:
            return pArray
        
    image = image.convert('RGB')
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            hexel = "0"
            try:
                for color in pixel[:3]:
                    hexVal = "{:02x}".format(color)
                    hexel += hexVal
            except IndexError as ie:
                raise Exception("Error: Color index out of bounds. Image is not RGB") from ie
            hexel += 'h'
            pArray.append(hexel)
    return pArray

def img2bytes(imgPath, imgName, outputPath, variableName="var", forceRGB=False):
    try:
        im = Image.open(imgPath)
        x = im.size[0]
        y = im.size[1]
        pArray = get_pixels_to_hex(im, x, y, forceRGB)
        write_asm_pixels_to_file(imgName, outputPath, variableName, pArray, x, y)

    except FileNotFoundError as fnfe:
        raise Exception("The specified file path is incorrect and could not be found") from fnfe
    except UnidentifiedImageError as uie:
        raise Exception("The provided file is either not an image or corrupt") from uie
    except AttributeError as ae:
        raise Exception("The provided path is not a file") from ae
    except Exception as e:
        raise Exception(str(e)) from e