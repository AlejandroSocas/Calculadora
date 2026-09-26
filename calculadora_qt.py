from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QTimer, Qt
from ui_calculadora import Ui_MainWindow
import sys
from functools import partial

class InterfazCalculadora(QMainWindow):
  def __init__(self):
    super().__init__()

    # Instanciamos la clase del diseño y le pasamos nuestra ventana (self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.setWindowTitle("Calculadora")

    botones = self.findChildren(QPushButton)
    for boton in botones:
      simbolo = boton.text()
      if simbolo == "<-":
        boton.clicked.connect(partial(self.borrar_ultimo_pantalla))
      elif simbolo == "=":
        boton.clicked.connect(self.calcular)
      else:
        boton.clicked.connect(partial(self.escribir_pantalla, simbolo))

  def escribir_pantalla(self, simbolo):
    self.ui.pantalla.insert(simbolo)

  def borrar_ultimo_pantalla(self):
    texto_actual = self.ui.pantalla.text()
    self.ui.pantalla.setText(texto_actual[:-1])

  def borrar_pantalla(self):
    self.ui.pantalla.clear()

  def calcular(self):
    texto_actual = self.ui.pantalla.text()
    texto_actual = texto_actual.replace(",",".")
    resultado = None
    self.borrar_pantalla()
    try:
      resultado = eval(texto_actual)
    except Exception as e:
      self.escribir_pantalla(f"Error: {str(e)}")
      QTimer.singleShot(1000, self.borrar_pantalla)
    else:
      if resultado is None:
            return

      self.borrar_pantalla()
      if resultado.is_integer():
        self.escribir_pantalla(str(int(resultado)))
      else:
        if isinstance(resultado, float) and resultado.is_integer():
          resultado = int(resultado)

        resultado_str = str(resultado).replace('.', ',')
        self.escribir_pantalla(resultado_str)

  def keyPressEvent(self, event):
    caracter = event.text()
    if caracter in "0123456789+-*/()":
      self.escribir_pantalla(caracter)
    elif caracter == ".":
      self.escribir_pantalla(",")
    elif event.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
      self.calcular()
    elif event.key() == Qt.Key.Key_Backspace:
      self.borrar_ultimo_pantalla()
    else:
      super().keyPressEvent(event)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ventana = InterfazCalculadora()
  ventana.show()
  sys.exit(app.exec())