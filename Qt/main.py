from os import error
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog 
from PyQt5.QtWidgets import QMessageBox
import csv
import clientui

def set_list(mylist):
    new_list = []
    for item in mylist:
        index = item.find("|")
        log = item[:index]
        log = log.replace('"','')
        new_list.append(log)
    return list(set(new_list))

def read_file(path):
    list_cvf = []
    with open(path,mode = "r+", encoding = "utf-8" ) as f:
        filter_list = set_list(f)
        for log_list in filter_list:
            log = log_list[:24]+chr(29)+log_list[31:36]
            list_cvf.append([log])
    return list_cvf

def write_csv(logs,names):
    csvfile = open(names, mode = 'w', encoding = "utf-8", newline= '')
    writer = csv.writer(csvfile, dialect='excel')
    for item in logs:
        print(item)
        #item = item.split()       
        writer.writerow(item)

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


    def mybutton4_clicked(self):
        path = self.lineEdit.text()
        if (len(path) > 5):
            logs = read_file(path)
            write_csv(logs,'convert1.csv')            
        else:
            QMessageBox.about(self, "Error", "Пожалуста выберите путь к лог файле 1 строке!")
        path2 = self.lineEdit_2.text()
        if (len(path2) > 5):
            logs2 = read_file(path2)
            write_csv(logs2,'convert2.csv')
        else:
            QMessageBox.about(self, "Error", "Пожалуста выберите путь к лог файле 2 строке!")
        path3 = self.lineEdit_3.text()
        if(len(path3)> 5):
            logs3 = read_file(path3)
            write_csv(logs3,'convert3.csv')
        else:
            QMessageBox.about(self, "Error", "Пожалуста выберите путь к лог файле 3 строке!")
        QMessageBox.about(self, "О успешной завершении", "Конвертация успешно равершено!")

        



app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec_()


