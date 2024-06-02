import tkinter as tk
from png2asm import model, view, controller, utils
from sys import argv
from os import path

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.model = model.Model()
        self.view = view.View(self)
        self.controller = controller.Controller(self.model, self.view)

        self.view.setController(self.controller)

def main():
    # argv[1] - path to image
    # argv[2] - variable name
    # argv[3] - force rgb

    # TODO: Parse args with argparse (https://docs.python.org/3/library/argparse.html)
    if len(argv) > 1:
        imgPath = argv[1]
        imgName = utils.path_to_basename(imgPath)
        currentDir = path.dirname(imgPath)

        if len(argv) == 3:
            utils.img2bytes(imgPath, imgName, currentDir, argv[2])
        elif len(argv) == 4:
            utils.img2bytes(imgPath, imgName, currentDir, argv[2], argv[3])
        else:
            utils.img2bytes(imgPath, imgName, currentDir)
    else:
        app = App()
        app.mainloop()

if __name__ == "__main__":
    main()
