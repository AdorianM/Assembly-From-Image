from png2asm import utils
from os import path
from os import listdir

class Model:
    def __init__(self):
        self.inputPath = ""
        self.outputPath = "/"
        self.variableName = "var"
    
    def setInputPath(self, inputPath):
        self.inputPath = inputPath

    def setOutputPath(self, outputPath):
        self.outputPath = outputPath

    def setVariableName(self, variableName):
        self.variableName = variableName

    def convert(self):
        try:
            if path.isdir(self.inputPath):
                files = [path.join(self.inputPath, f) for f in listdir(self.inputPath) if path.isfile(path.join(self.inputPath, f))]
                for file in files:
                    utils.img2bytes(file, utils.path_to_basename(file), self.outputPath, self.variableName)
                return True
            utils.img2bytes(self.inputPath, utils.path_to_basename(self.inputPath), self.outputPath, self.variableName)

            return True
        except Exception as e:
            return str(e)