import tkinter as tk
import os
import sys

"""
Generar ejecutable:
 - Windows: pyinstaller --onefile --windowed --add-data "icono.png;." calculadora.py
 - Linux: pyinstaller --onefile --windowed --add-data "icono.png:." calculadora.py
"""

def resolver_ruta(ruta_relativa):
  """Obtiene la ruta absoluta al recurso, funciona para dev y para PyInstaller paar empaquetar el porgrama en un ejecutable"""
  if hasattr(sys, '_MEIPASS'):
    # PyInstaller crea una carpeta temporal y guarda la ruta en _MEIPASS
    return os.path.join(sys._MEIPASS, ruta_relativa)
  return os.path.join(os.path.abspath("."), ruta_relativa)

class UI(tk.Frame):

  def __init__(self, parent=None):
    """Constructor de la calculadora"""
    tk.Frame.__init__(self, parent)
    self.parent = parent
    self.teclas = [
      ["(", ")", "%", "<-"],
      ['7', '8', '9', '/'],
      ['4', '5', '6', '*'],
      ['1', '2', '3', '-'],
      ['0', ',', '=', '+']
    ]
    self.init_ui()

  def init_ui(self):
    """Aquí van los widgets"""
    self.parent.title("Calculadora")
    self.parent.minsize(200, 400) # Bloquea el tamaño mínimo

    # Establece el icono de la ventana
    icono = tk.PhotoImage(file=resolver_ruta("icono.png")) 
    self.parent.iconphoto(False, icono) 

    # Configuración de la pantalla
    self.pantalla = tk.Entry(self.parent, bd=1, font=("Arial", 34), relief="solid")
    self.pantalla.pack(padx=30, pady=30)
    self.pantalla.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=15, ipady=10)
    # Configuramos la pantalla para que sea solo lectura y que no se pueda escribir con el teclado letras. Cuando se quiera escribir hay que cambiar state a "normal"
    self.pantalla.config(state="readonly")

    #Asignamos las funciones que tienen los botones
    for i, fila in enumerate(self.teclas, start=1):
      for j, funcion in enumerate(fila):
        if funcion == '=':
          boton = tk.Button(self.parent, text=funcion, font=("Arial", 24), padx=10, pady=10, command=self.calcular)
        elif funcion == "<-":
          boton = tk.Button(self.parent, text=funcion, font=("Arial", 24), padx=10, pady=10, command=self.borrar_caracter)
        else:
          boton = tk.Button(self.parent, text=funcion, font=("Arial", 24), padx=10, pady=10, command=lambda f=funcion: self.imprimir_pantalla(f))
        boton.grid(row=i, column=j, sticky="nsew")

    # Con esto las columnas se ajustan al tamaño de la ventana
    for col in range(4):
      self.parent.columnconfigure(col, weight=1)

    # Con esto las filas se ajustan al tamaño de la ventana
    self.parent.rowconfigure(0, weight=2)
    for row in range(1, 6):
      self.parent.rowconfigure(row, weight=1)

    # Escucha las teclas que se pulsan
    self.parent.bind("<Key>", self.tecla_pulsada)
    

  def calcular(self):
    """Función que calcula el resultado de la operación que hay en pantalla y muestra el resultado en la misma"""
    contenido = self.pantalla.get()
    contenido = contenido.replace(",",".")
    resultado = None
    try:
      resultado = eval(contenido) # Hace el cálculo entero del string
    except ZeroDivisionError:
      self.borrar_pantalla()
      self.imprimir_pantalla("Error")
      self.parent.after(1000, self.borrar_pantalla)
      return
    except SyntaxError:
      self.borrar_pantalla()
      self.imprimir_pantalla("Error Sintaxis")
      self.parent.after(1000, self.borrar_pantalla)

    if resultado is None:
      return

    self.borrar_pantalla()
    if resultado.is_integer():
      self.imprimir_pantalla(int(resultado))
    else:
      resultado = str(resultado)
      self.imprimir_pantalla(resultado.replace('.',','))


  def imprimir_pantalla(self, boton):
    """Imprime un string en la pantalla"""
    self.pantalla.config(state="normal")
    self.pantalla.insert(tk.END, boton)
    self.pantalla.config(state="readonly")

  def borrar_pantalla(self):
    """Borra la pantalla completa"""
    self.pantalla.config(state="normal")
    self.pantalla.delete(0, tk.END)
    self.pantalla.config(state="readonly")

  def borrar_caracter(self):
    """Borra el último caracter de la pantalla"""
    longitud_borrado = len(self.pantalla.get()) - 1
    self.pantalla.config(state="normal")
    self.pantalla.delete(longitud_borrado, tk.END)
    self.pantalla.config(state="readonly")

  def tecla_pulsada(self, evento):
    """Asigna funciones cuando ciertas teclas son pulsadas"""
    # print(f"Has pulsado: {evento.char}, {evento.keysym}")
    if evento.char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', ',', '(', ')', '%']:
      self.imprimir_pantalla(evento.char)
    elif evento.keysym == "BackSpace":
      self.borrar_caracter()
    elif evento.keysym == "Return":
      self.calcular()
    


if __name__ == "__main__":
  ROOT = tk.Tk()
  ROOT.geometry("400x600")
  APP = UI(parent=ROOT)
  APP.mainloop()