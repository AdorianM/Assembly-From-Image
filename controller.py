from os import path

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def convert(self, inputPath, outputPath):
        if path.isdir(inputPath):
            self.view.showError("Please select an input file.")
            return
        
        self.model.setInputPath(inputPath)
        self.model.setOutputPath(outputPath)
        conversionResult = self.model.convert()
        if conversionResult is True:
            self.view.showSuccess("Conversion completed.")
        else:
            self.view.showError(conversionResult)