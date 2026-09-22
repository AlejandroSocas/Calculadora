# Calculadora sencilla multiplataforma escrita en Python (v1.0)
Esta calculadora ha sido creada como un proyecto para aprender lo básico de la creación de programas con interfaz gráfica. En este caso he usando la librearía gráfica Tkinter porque ya viene instalado con Python. La mayor desventaja de usar esta librería es que las interfaces gráficas se ven bastante arcaicas pero sirve para aprender la lógica básica.

Así se ve la calculadora actualmente:

<img src="https://i.ibb.co/k6kn5DfX/Captura.png" alt="Imagen del programa" width="30%">


## Creación de un ejecutable
Para generar un ejecutable hay que cambiar solo un ; por unos : en el comando de pyinstaller.

**Importante tener instalado pyinstaller:** `pip install pyinstaller `

Ahora dependiendo del sistema operativo:

- Windows: `pyinstaller --onefile --windowed --add-data "icono.png;." calculadora.py`

- Linux: `pyinstaller --onefile --windowed --add-data "icono.png:." calculadora.py`