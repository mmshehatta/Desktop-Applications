

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo3\UI\Demo3.ui" , self)
        self.setWindowIcon(QIcon(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo3\Imgs\ai.ico"))
        self.setWindowTitle("الصفحـــة الرئيسية")
        
        
        # Selectors here>>
        self.lable = self.findChild(QLabel  , "label")
        self.btn = self.findChild(QPushButton , "pushButton")
        self.btn.clicked.connect(self.handelBtnClick)
        self.ent = self.findChild(QLineEdit , "lineEdit")
        self.ent2 = self.findChild(QLineEdit,"lineEdit_2")

        # text alignment in lineEdit or textbox
        # self.ent.setAlignment(Qt.AlignCenter)
        self.ent.setAlignment(Qt.AlignLeft)

        # add action to the entry .. action as eye icon to show or hide password in textBox
        # self.ent.addAction(QIcon(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo3\Imgs\ai.ico"),QLineEdit.LeadingPosition)

        # to set placeholder to textBox
        self.ent.setPlaceholderText("User Name ")
        self.ent2.setPlaceholderText("Password")
        self.ent2.setEchoMode(QLineEdit.Password)


        # to set validator on lineEdit or textBox 
        # you have 3 validator:
        # 1- QIntValidator to accept only integer values with limit of int datatype.
        # 2- QDoubleValidator to accept only double vales with no limit of numbers before and after floating point sign
        # 3- QRegExpValidator to accept input that match specific pattern ... we will take about it later 

        # self.ent.setValidator(QIntValidator())
        # self.ent.setValidator(QDoubleValidator())







    # slots here:

    def handelBtnClick(self):
        # self.label.setText(self.ent.text())
        print(self.ent.text())
        print(self.ent2.text())

       
         





       


#try except..to avoid error in exists to appear in customer side 
try:
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec_()
except Exception as error:
    print(error)

