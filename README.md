# Calculadora sencilla multiplataforma escrita en Python (v1.1)
Esta calculadora ha sido creada como un proyecto para aprender lo básico de la creación de programas con interfaz gráfica. En este caso he usando la librearía gráfica Tkinter porque ya viene instalado con Python. La mayor desventaja de usar esta librería es que las interfaces gráficas se ven bastante arcaicas pero sirve para aprender la lógica básica.

Es por esto que en la versión 1.1 he pasado la interfaz a Qt6 que es una librería gráfica mucho más moderna que se sincroniza con el tema del sistema operativo.

### Diferencia entre las calculadoras:

| Calculadora Tkinter | Calculadora Qt (PySide6) |
| :---: | :---: |
| <img src="https://i.ibb.co/CpsjCZkP/imagen.png" width="300"> | <img src="https://i.ibb.co/v4c0qmsZ/imagen.png" width="300"> |


## Creación de un ejecutable

**Importante tener instalado pyinstaller:** `pip install pyinstaller `

Ahora dependiendo del sistema operativo:

- Windows: 
  * `pyinstaller --onefile --windowed --add-data "icono.png;." calculadora_tkinter.py` (versión tkinter)
  * `pyinstaller --noconfirm --onefile --windowed calculadora_qt.py` (versión Qt)

- Linux: 
  * `pyinstaller --onefile --windowed --add-data "icono.png:." calculadora_tkinter.py` (versión tkinter)
  * `pyinstaller --noconfirm --onefile --windowed calculadora_qt.py` (versión Qt)