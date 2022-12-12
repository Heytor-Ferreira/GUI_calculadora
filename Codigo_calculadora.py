from PyQt5 import  uic,QtWidgets
def Calculo():
    if GUI_calculadora.radioButton.isChecked():
        Valor_1 = int(GUI_calculadora.lineEdit.text())
        Valor_2 = int(GUI_calculadora.lineEdit_2.text())
        Resultado = Valor_1+Valor_2
        GUI_calculadora.textBrowser.setText(str(Resultado))       
    elif GUI_calculadora.radioButton_2.isChecked():
        Valor_1 = int(GUI_calculadora.lineEdit.text())
        Valor_2 = int(GUI_calculadora.lineEdit_2.text())
        Resultado = Valor_1-Valor_2
        GUI_calculadora.textBrowser.setText(str(Resultado)) 
    elif GUI_calculadora.radioButton_3.isChecked():
        Valor_1 = int(GUI_calculadora.lineEdit.text())
        Valor_2 = int(GUI_calculadora.lineEdit_2.text())
        Resultado = Valor_1/Valor_2
        GUI_calculadora.textBrowser.setText(str(Resultado))
    elif GUI_calculadora.radioButton_4.isChecked():
        Valor_1 = int(GUI_calculadora.lineEdit.text())
        Valor_2 = int(GUI_calculadora.lineEdit_2.text())
        Resultado = Valor_1*Valor_2
        GUI_calculadora.textBrowser.setText(str(Resultado))
    else :
        GUI_calculadora.textBrowser.setText("ERRO")
app=QtWidgets.QApplication([])
GUI_calculadora=uic.loadUi("GUI_calculadora.ui")
GUI_calculadora.pushButton.clicked.connect(Calculo)
GUI_calculadora.show()
app.exec()