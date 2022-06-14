import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

from os import path

default_padx = 10
default_pady = 5
baseColor = '#EFEFEA'

class ImageLabel(tk.Label):
    def __init__(self, parent, imgPath, *args, **kwargs):
        tk.Label.__init__(self, parent, *args, **kwargs)
        self.image = ImageTk.PhotoImage(Image.open(imgPath))
        self.draw()

    def draw(self):
        self.configure(image=self.image)

class LabeledText(tk.Frame):
    def __init__(self, parent, label, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Component definitions
        self.label = tk.Label(self, text=label)
        self.text = tk.Entry(self)

        # Component placement
        self.label.pack(side="left")
        self.text.pack(side="left", fill='x', expand=True, padx=default_padx)

class FileBrowser(tk.Frame):
    def __init__(self, parent, buttonMessage="Select a file", isDir=True, defaultPath="", *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.filePathVar = tk.StringVar()
        self.filePathVar.set(defaultPath)
        self.command = self.browseDir if isDir else self.browseFile

        # Component Definitions
        self.fileBrowser = tk.Button(self, text=buttonMessage, command=self.command, width=20)
        self.filePath = tk.Label(self, textvariable=self.filePathVar, border=1, relief="sunken")

        # Component Placement
        self.fileBrowser.pack(side=tk.TOP, fill="none", expand=True)
        self.filePath.pack(side=tk.TOP, fill="x", pady=default_pady)
    
    def browseFile(self):
        currentDir = path.dirname(path.realpath(__file__))
        file = filedialog.askopenfilename(initialdir = currentDir, title = "Select a File", filetypes = (("Images","*.png*"),
                                                ("all files","*.*")))
        self.filePathVar.set(file)

    def browseDir(self):
        dir = filedialog.askdirectory(initialdir = "/", title = "Select a Directory")
        self.filePathVar.set(dir)

class SettingsFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        currentDir = path.dirname(path.realpath(__file__))

        # Component definitions
        self.fileManagementFrame = tk.LabelFrame(self, text="Input\\Output", bg=baseColor)
        self.otherSettingsFrame = tk.LabelFrame(self, text="Others", bg=baseColor)

        self.inputBrowser = FileBrowser(self.fileManagementFrame, "Select Input File", isDir=False, bg=baseColor)
        self.outputBrowser = FileBrowser(self.fileManagementFrame, "Select Output Directory", isDir=True, defaultPath=currentDir, bg=baseColor)

        self.variableName = LabeledText(self.otherSettingsFrame, "Variable Name:")

        # Component placement
        self.fileManagementFrame.pack(side=tk.TOP, fill="x", expand=False, padx=default_padx, pady=default_pady)
        self.otherSettingsFrame.pack(side=tk.TOP, fill="x", expand=True, padx=default_padx, pady=default_pady)

        self.inputBrowser.pack(side=tk.TOP, fill="x", expand=True, padx=default_padx, pady=default_pady)
        self.outputBrowser.pack(side=tk.TOP, fill="x", expand=True, padx=default_padx, pady=default_pady)
        self.variableName.pack(side=tk.TOP, fill="x", expand=True, padx=default_padx, pady=default_pady)

class View(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.parent.title("Asm Converter")
        self.parent.geometry("280x350")
        self.parent.resizable(False, False)
        self.parent.iconbitmap("assets/chef.ico")
        self.parent.eval('tk::PlaceWindow . center')

        # Component definitions
        baseFrame = tk.Frame(self.parent, bg=baseColor)

        self.logoLabel = ImageLabel(baseFrame, imgPath="assets/chef.ico", text="Settings", compound=tk.TOP, font="Arial 14 bold", bg=baseColor)
        self.settingFrame = SettingsFrame(baseFrame)
        self.convertButton = tk.Button(baseFrame, text="Convert", command=self.convertButtonClicked, padx=20)

        # Component placement
        baseFrame.pack(fill="both", expand=True)

        self.logoLabel.pack(side=tk.TOP)
        self.settingFrame.pack(side=tk.TOP, fill="x", expand=False, padx=default_padx, pady=default_pady)
        self.convertButton.pack(side=tk.TOP, padx=default_padx, pady=default_pady)

        self.controller = None
    
    def setController(self, controller):
        self.controller = controller
    
    def convertButtonClicked(self):
        if self.controller:
            inputPath = self.settingFrame.inputBrowser.filePathVar.get()
            outputPath = self.settingFrame.outputBrowser.filePathVar.get()
            variableName = self.settingFrame.variableName.text.get()
            self.controller.convert(inputPath, outputPath, variableName)
    
    def showError(self, message):
        messagebox.showerror("Error", message)

    def showSuccess(self, message):
        messagebox.showinfo("Conversion", message)