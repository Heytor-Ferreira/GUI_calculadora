import sys
from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow


def calculo():
    Quad1 = int(GUI_calculadora.lineEdit.text())
    Quad2 = int(GUI_calculadora.lineEdit_2.text())
    Resultado = Quad1+Quad2
    GUI_calculadora.textBrowser.setText(str(Resultado))
    
  

app=QtWidgets.QApplication([])
GUI_calculadora=uic.loadUi("GUI_calculadora.ui")
GUI_calculadora.pushButton.clicked.connect(calculo)
GUI_calculadora.show()
app.exec()