import tkinter as tk
from PIL import Image, ImageTk

default_padx = 10
default_pady = 5

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

        self.logo = ImageTk.PhotoImage(Image.open("assets/chef.ico"))
        self.logoLabel = tk.Label(baseFrame, image=self.logo)
        self.settingFrame = tk.LabelFrame(baseFrame, text="Settings Panel", bg="#EFEFEA")
        self.convertButton = tk.Button(baseFrame, text="Convert", command=())

        self.outputSettingsFrame = tk.LabelFrame(self.settingFrame, text="Output Settings", bg="#EFEFEA")
        self.otherSettingsFrame = tk.LabelFrame(self.settingFrame, text="Other Settings", bg="#EFEFEA")

        self.outputEntry1 = tk.Frame(self.outputSettingsFrame, bg="#EFEFEA")
        self.outputLabel1 = tk.Label(self.outputEntry1, text="Output File Name:")
        self.outputText1 = tk.Text(self.outputEntry1, height=1, width=5)

        self.outputEntry2 = tk.Frame(self.outputSettingsFrame, bg="#EFEFEA")
        self.outputLabel2 = tk.Label(self.outputEntry2, text="Output File Name:")
        self.outputText2 = tk.Text(self.outputEntry2, height=1, width=5)

        self.outputEntry3 = tk.Frame(self.otherSettingsFrame, bg="#EFEFEA")
        self.outputLabel3 = tk.Label(self.outputEntry3, text="Output File Name:")
        self.outputText3 = tk.Text(self.outputEntry3, height=1, width=5)

        self.outputEntry4 = tk.Frame(self.otherSettingsFrame, bg="#EFEFEA")
        self.outputLabel4 = tk.Label(self.outputEntry4, text="Output File Name:")
        self.outputText4 = tk.Text(self.outputEntry4, height=1, width=5)

        baseFrame.pack(fill="both", expand=True)

        self.logoLabel.pack(side=tk.TOP)
        self.settingFrame.pack(side=tk.TOP, fill="both", expand=True, padx=default_padx, pady=default_pady)
        self.convertButton.pack(side=tk.BOTTOM, padx=default_padx, pady=default_pady)

        self.outputSettingsFrame.pack(side=tk.LEFT, fill="both", expand=True, padx=default_padx, pady=default_pady)
        self.otherSettingsFrame.pack(side=tk.RIGHT, fill="both", expand=True, padx=default_padx, pady=default_pady)

        self.outputEntry1.pack(side=tk.TOP, fill="both", expand=True)
        self.outputLabel1.pack(side=tk.LEFT)
        self.outputText1.pack(side=tk.LEFT, fill="x", expand=True, padx=default_padx)

        self.outputEntry2.pack(side=tk.TOP, fill="both", expand=True)
        self.outputLabel2.pack(side=tk.LEFT)
        self.outputText2.pack(side=tk.LEFT, fill="x", expand=True, padx=default_padx)

        self.outputEntry3.pack(side=tk.TOP, fill="both", expand=True)
        self.outputLabel3.pack(side=tk.LEFT)
        self.outputText3.pack(side=tk.LEFT, fill="x", expand=True, padx=default_padx)

        self.outputEntry4.pack(side=tk.TOP, fill="both", expand=True)
        self.outputLabel4.pack(side=tk.LEFT)
        self.outputText4.pack(side=tk.LEFT, fill="x", expand=True, padx=default_padx)

# Function to start the program.
def main():
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()