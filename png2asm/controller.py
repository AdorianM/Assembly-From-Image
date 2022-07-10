from os import path
import re

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def convert(self, inputPath, outputPath, variableName):
        if inputPath == "":
            self.view.showError("Please select an input file or directory.")
            return
        
        if variableName != "" and not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", variableName):
            self.view.showError("The variable name is invalid.\nIt must start with a letter or underscore and contain only letters, numbers, and underscores.")
            return
        
        self.model.setInputPath(inputPath)
        self.model.setOutputPath(outputPath)
        if variableName != "":
            self.model.setVariableName(variableName)
        
        conversionResult = self.model.convert()
        if conversionResult is True:
            self.view.showSuccess("Conversion completed.")
        else:
            self.view.showError(conversionResult)