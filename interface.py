import tkinter as tk
from PIL import Image, ImageTk

default_padx = 10
default_pady = 5

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
        self.label = tk.Label(self, text=label)
        self.text = tk.Text(self,  height=1, width=5)

        self.label.pack(side="left")
        self.text.pack(side="left", fill='x', expand=True, padx=default_padx)

class SettingsFrame(tk.LabelFrame):
    def __init__(self, parent, *args, **kwargs):
        tk.LabelFrame.__init__(self, parent, *args, **kwargs)

        self.outputSettingsFrame = tk.LabelFrame(self, text="Output Settings", bg="#EFEFEA")
        self.otherSettingsFrame = tk.LabelFrame(self, text="Other Settings", bg="#EFEFEA")

        self.labeledText1 = LabeledText(self.outputSettingsFrame, "Output File Name:")
        self.labeledText2 = LabeledText(self.outputSettingsFrame, "Output File Name:")
        self.labeledText3 = LabeledText(self.otherSettingsFrame, "Output File Name:")
        self.labeledText4 = LabeledText(self.otherSettingsFrame, "Output File Name:")

        self.outputSettingsFrame.pack(side=tk.LEFT, fill="both", expand=True, padx=default_padx, pady=default_pady)
        self.otherSettingsFrame.pack(side=tk.RIGHT, fill="both", expand=True, padx=default_padx, pady=default_pady)

        self.labeledText1.pack(side=tk.TOP, fill="both", expand=True)
        self.labeledText2.pack(side=tk.TOP, fill="both", expand=True)
        self.labeledText3.pack(side=tk.TOP, fill="both", expand=True)
        self.labeledText4.pack(side=tk.TOP, fill="both", expand=True)

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.parent.title("Png to Asm Converter")
        self.parent.geometry("480x260")
        self.parent.iconbitmap("assets/chef.ico")

        baseFrame = tk.Frame(self.parent, borderwidth=14, bg="#EFEFEA")

        self.logoLabel = ImageLabel(baseFrame, "assets/chef.ico")
        self.settingFrame = SettingsFrame(baseFrame, text="Settings Panel", bg="#EFEFEA")
        self.convertButton = tk.Button(baseFrame, text="Convert", command=())

        baseFrame.pack(fill="both", expand=True)

        self.logoLabel.pack(side=tk.TOP)
        self.settingFrame.pack(side=tk.TOP, fill="both", expand=True, padx=default_padx, pady=default_pady)
        self.convertButton.pack(side=tk.BOTTOM, padx=default_padx, pady=default_pady)

def main():
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()