# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(366, 510)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pantalla = QLineEdit(self.centralwidget)
        self.pantalla.setObjectName(u"pantalla")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pantalla.sizePolicy().hasHeightForWidth())
        self.pantalla.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.pantalla.setFont(font)
        self.pantalla.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pantalla.setReadOnly(True)

        self.gridLayout.addWidget(self.pantalla, 0, 0, 1, 4)

        self.abre_parentesis = QPushButton(self.centralwidget)
        self.abre_parentesis.setObjectName(u"abre_parentesis")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.abre_parentesis.sizePolicy().hasHeightForWidth())
        self.abre_parentesis.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(14)
        self.abre_parentesis.setFont(font1)

        self.gridLayout.addWidget(self.abre_parentesis, 1, 0, 1, 1)

        self.cierra_parentesis = QPushButton(self.centralwidget)
        self.cierra_parentesis.setObjectName(u"cierra_parentesis")
        sizePolicy1.setHeightForWidth(self.cierra_parentesis.sizePolicy().hasHeightForWidth())
        self.cierra_parentesis.setSizePolicy(sizePolicy1)
        self.cierra_parentesis.setFont(font1)

        self.gridLayout.addWidget(self.cierra_parentesis, 1, 1, 1, 1)

        self.modulo = QPushButton(self.centralwidget)
        self.modulo.setObjectName(u"modulo")
        sizePolicy1.setHeightForWidth(self.modulo.sizePolicy().hasHeightForWidth())
        self.modulo.setSizePolicy(sizePolicy1)
        self.modulo.setFont(font1)

        self.gridLayout.addWidget(self.modulo, 1, 2, 1, 1)

        self.borrar = QPushButton(self.centralwidget)
        self.borrar.setObjectName(u"borrar")
        sizePolicy1.setHeightForWidth(self.borrar.sizePolicy().hasHeightForWidth())
        self.borrar.setSizePolicy(sizePolicy1)
        self.borrar.setFont(font1)

        self.gridLayout.addWidget(self.borrar, 1, 3, 1, 1)

        self.siete = QPushButton(self.centralwidget)
        self.siete.setObjectName(u"siete")
        sizePolicy1.setHeightForWidth(self.siete.sizePolicy().hasHeightForWidth())
        self.siete.setSizePolicy(sizePolicy1)
        self.siete.setFont(font1)

        self.gridLayout.addWidget(self.siete, 2, 0, 1, 1)

        self.ocho = QPushButton(self.centralwidget)
        self.ocho.setObjectName(u"ocho")
        sizePolicy1.setHeightForWidth(self.ocho.sizePolicy().hasHeightForWidth())
        self.ocho.setSizePolicy(sizePolicy1)
        self.ocho.setFont(font1)

        self.gridLayout.addWidget(self.ocho, 2, 1, 1, 1)

        self.nueve = QPushButton(self.centralwidget)
        self.nueve.setObjectName(u"nueve")
        sizePolicy1.setHeightForWidth(self.nueve.sizePolicy().hasHeightForWidth())
        self.nueve.setSizePolicy(sizePolicy1)
        self.nueve.setFont(font1)

        self.gridLayout.addWidget(self.nueve, 2, 2, 1, 1)

        self.division = QPushButton(self.centralwidget)
        self.division.setObjectName(u"division")
        sizePolicy1.setHeightForWidth(self.division.sizePolicy().hasHeightForWidth())
        self.division.setSizePolicy(sizePolicy1)
        self.division.setFont(font1)

        self.gridLayout.addWidget(self.division, 2, 3, 1, 1)

        self.cuatro = QPushButton(self.centralwidget)
        self.cuatro.setObjectName(u"cuatro")
        sizePolicy1.setHeightForWidth(self.cuatro.sizePolicy().hasHeightForWidth())
        self.cuatro.setSizePolicy(sizePolicy1)
        self.cuatro.setFont(font1)

        self.gridLayout.addWidget(self.cuatro, 3, 0, 1, 1)

        self.cinco = QPushButton(self.centralwidget)
        self.cinco.setObjectName(u"cinco")
        sizePolicy1.setHeightForWidth(self.cinco.sizePolicy().hasHeightForWidth())
        self.cinco.setSizePolicy(sizePolicy1)
        self.cinco.setFont(font1)

        self.gridLayout.addWidget(self.cinco, 3, 1, 1, 1)

        self.seis = QPushButton(self.centralwidget)
        self.seis.setObjectName(u"seis")
        sizePolicy1.setHeightForWidth(self.seis.sizePolicy().hasHeightForWidth())
        self.seis.setSizePolicy(sizePolicy1)
        self.seis.setFont(font1)

        self.gridLayout.addWidget(self.seis, 3, 2, 1, 1)

        self.multiplicacion = QPushButton(self.centralwidget)
        self.multiplicacion.setObjectName(u"multiplicacion")
        sizePolicy1.setHeightForWidth(self.multiplicacion.sizePolicy().hasHeightForWidth())
        self.multiplicacion.setSizePolicy(sizePolicy1)
        self.multiplicacion.setFont(font1)

        self.gridLayout.addWidget(self.multiplicacion, 3, 3, 1, 1)

        self.uno = QPushButton(self.centralwidget)
        self.uno.setObjectName(u"uno")
        sizePolicy1.setHeightForWidth(self.uno.sizePolicy().hasHeightForWidth())
        self.uno.setSizePolicy(sizePolicy1)
        self.uno.setFont(font1)

        self.gridLayout.addWidget(self.uno, 4, 0, 1, 1)

        self.dos = QPushButton(self.centralwidget)
        self.dos.setObjectName(u"dos")
        sizePolicy1.setHeightForWidth(self.dos.sizePolicy().hasHeightForWidth())
        self.dos.setSizePolicy(sizePolicy1)
        self.dos.setFont(font1)

        self.gridLayout.addWidget(self.dos, 4, 1, 1, 1)

        self.tres = QPushButton(self.centralwidget)
        self.tres.setObjectName(u"tres")
        sizePolicy1.setHeightForWidth(self.tres.sizePolicy().hasHeightForWidth())
        self.tres.setSizePolicy(sizePolicy1)
        self.tres.setFont(font1)

        self.gridLayout.addWidget(self.tres, 4, 2, 1, 1)

        self.resta = QPushButton(self.centralwidget)
        self.resta.setObjectName(u"resta")
        sizePolicy1.setHeightForWidth(self.resta.sizePolicy().hasHeightForWidth())
        self.resta.setSizePolicy(sizePolicy1)
        self.resta.setFont(font1)

        self.gridLayout.addWidget(self.resta, 4, 3, 1, 1)

        self.cero = QPushButton(self.centralwidget)
        self.cero.setObjectName(u"cero")
        sizePolicy1.setHeightForWidth(self.cero.sizePolicy().hasHeightForWidth())
        self.cero.setSizePolicy(sizePolicy1)
        self.cero.setFont(font1)

        self.gridLayout.addWidget(self.cero, 5, 0, 1, 1)

        self.coma = QPushButton(self.centralwidget)
        self.coma.setObjectName(u"coma")
        sizePolicy1.setHeightForWidth(self.coma.sizePolicy().hasHeightForWidth())
        self.coma.setSizePolicy(sizePolicy1)
        self.coma.setFont(font1)

        self.gridLayout.addWidget(self.coma, 5, 1, 1, 1)

        self.igual = QPushButton(self.centralwidget)
        self.igual.setObjectName(u"igual")
        sizePolicy1.setHeightForWidth(self.igual.sizePolicy().hasHeightForWidth())
        self.igual.setSizePolicy(sizePolicy1)
        self.igual.setFont(font1)

        self.gridLayout.addWidget(self.igual, 5, 2, 1, 1)

        self.suma = QPushButton(self.centralwidget)
        self.suma.setObjectName(u"suma")
        sizePolicy1.setHeightForWidth(self.suma.sizePolicy().hasHeightForWidth())
        self.suma.setSizePolicy(sizePolicy1)
        self.suma.setFont(font1)

        self.gridLayout.addWidget(self.suma, 5, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 366, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.abre_parentesis.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.cierra_parentesis.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.modulo.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.borrar.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.siete.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.ocho.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.nueve.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.cuatro.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.cinco.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.seis.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.multiplicacion.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.uno.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.dos.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.tres.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.resta.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.cero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.coma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.suma.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

