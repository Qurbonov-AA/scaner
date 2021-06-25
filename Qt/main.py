from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog 

import clientui


class ExampleApp(QtWidgets.QMainWindow,clientui.Ui_Dialog):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def mybutton_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            self.lineEdit.setText(fileName) 


    def mybutton2_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            self.lineEdit_2.setText(fileName) 

    def mybutton3_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:            
            self.lineEdit_3.setText(fileName) 


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec_()


