from PySide6.QtGui import*
from PySide6.QtCore import *
import sys
import math
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QTextBrowser, QLineEdit, QVBoxLayout

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)
        self.resultsList=QTextBrowser()
        self.resultsInput=QLineEdit("Enter an expression you want to Evaluate and press return key")

        layout=QVBoxLayout()
        layout.addWidget(self.resultsList)
        layout.addWidget(self.resultsInput)
        self.setLayout(layout)
        self.resultsInput.selectAll()
        self.resultsInput.setFocus()
        self.resultsInput.returnPressed.connect(self.compute)
    def compute(self):
        try:
            text=self.resultsInput.text()
            self.resultsInput.append("(0)=<b>(1)</b>".format(text,eval(text)))
        except:
            self.resultsList.append("<font color=red><b> expression invalid</b></font>")


app=QApplication(sys.argv)
form= Form()
form.show()
app.exec_()

