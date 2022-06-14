from png2asm import utils

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
            utils.img2bytes(self.inputPath, utils.path_to_basename(self.inputPath), self.outputPath, self.variableName)

            return True
        except Exception as e:
            return str(e)