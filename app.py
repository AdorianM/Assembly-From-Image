import tkinter as tk
import model, view, controller

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.model = model.Model()
        self.view = view.View(self)
        self.controller = controller.Controller(self.model, self.view)

        self.view.setController(self.controller)

if __name__ == "__main__":
    app = App()
    app.mainloop()
