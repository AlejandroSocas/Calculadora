import tkinter as tk

def saludar():
  print("Botón pulsado")

class UI(tk.Frame):

  def __init__(self, parent=None):
    tk.Frame.__init__(self, parent)
    self.parent = parent
    self.init_ui()

  def init_ui(self):
    """Aquí van los widgets"""
    self.parent.title("Calculadora")
    self.pantalla = tk.Entry(self.parent, width=13)
    botonok = tk.Button(self.parent, text="ok", command=self.leer_pantalla)
    boton7 = tk.Button(self.parent, text="7", command=self.pantalla.insert(0, "7"))
    boton8 = tk.Button(self.parent, text="8", command=saludar)
    boton9 = tk.Button(self.parent, text="9", command=saludar)
    boton4 = tk.Button(self.parent, text="4", command=saludar)
    boton5 = tk.Button(self.parent, text="5", command=saludar)
    boton6 = tk.Button(self.parent, text="6", command=saludar)
    boton1 = tk.Button(self.parent, text="1", command=saludar)
    boton2 = tk.Button(self.parent, text="2", command=saludar)
    boton3 = tk.Button(self.parent, text="3", command=saludar)
    boton0 = tk.Button(self.parent, text="0", command=saludar)
    botoncoma = tk.Button(self.parent, text=",", command=saludar)
    botondiv = tk.Button(self.parent, text="/", command=saludar)
    botonmult = tk.Button(self.parent, text="x", command=saludar)
    botonrest = tk.Button(self.parent, text="-", command=saludar)
    botonsum = tk.Button(self.parent, text="+", command=saludar)
    botonigual = tk.Button(self.parent, text="=", command=saludar)

    self.pantalla.grid(row=0, column=0, columnspan=4)
    botonok.grid(row=0, column=5)
    boton7.grid(row=1, column=0)
    boton8.grid(row=1, column=1)
    boton9.grid(row=1, column=2)
    botondiv.grid(row=1, column=3)
    boton4.grid(row=2, column=0)
    boton5.grid(row=2, column=1)
    boton6.grid(row=2, column=2)
    botonmult.grid(row=2, column=3)
    boton1.grid(row=3, column=0)
    boton2.grid(row=3, column=1)
    boton3.grid(row=3, column=2)
    botonrest.grid(row=3, column=3)
    boton0.grid(row=4, column=0)
    botoncoma.grid(row=4, column=1)
    botonigual.grid(row=4, column=2)
    botonsum.grid(row=4, column=3)

  def leer_pantalla(self):
    contenido = self.pantalla.get()
    print(contenido) 

if __name__ == "__main__":
  ROOT = tk.Tk()
  ROOT.geometry("800x600")
  APP = UI(parent=ROOT)
  APP.mainloop()
  ROOT.destroy()