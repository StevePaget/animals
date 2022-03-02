import tkinter as tk
import tkinter.font as tkFont


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.theCanvas = tk.Canvas(self, width=500, height=500, bg="#007744")
        self.theCanvas.grid(row=0, column=0)
               
main = App()
main.mainloop()
