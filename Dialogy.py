import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pylab as pl
"""
messagebox.showerror("Titulek","Soráč eroráč")

odpoved = messagebox.askquestion("titulek","message", icon = "icon")
print(odpoved)

soubor = filedialog.askopenfile(title = "vyber soubor", initialdir="/")
print(soubor)
"""
class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if "textvariable" not in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = "Foo"
    title_ = "dialogy"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.title_)
        self.bind("<Escape>", self.quit)

        self.lbl = tk.Label(self, text="...")
        self.lbl.pack()
        self.btn1 = tk.Button(self, text="načíst",width= 5)
        self.btn1.pack(side="top")
        self.btn1.bind("<ButtonRelease-1>",self.soubor)

        self.btn2 = tk.Button(self, text="spustit",width= 5)
        self.btn2.pack(side="top")
        self.btn2.bind("<ButtonRelease-1>",self.show)
   
    def show(self,event=None):
        axisx = []
        axisy = []

        t = pl.linspace(0,0.1,100000)

        with open(self.filename,"r") as f:
            while True:
                line = f.readline()
                if line == "":
                    break
                linesplit = line.split()
                if len(linesplit) == 2:
                    x, y = line.split()
                    axisx.append(float(x))
                    axisy.append(float(y))
            print(axisx)
            print(axisy)

            pl.plot(t,axisx,color ="#ff3311")
            pl.plot(t,axisy)

            pl.grid(True)
            pl.show()

    def soubor(self,event=None):
        self.filename = filedialog.askopenfilename()
        self.lbl.config(text=self.filename)
            
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()

