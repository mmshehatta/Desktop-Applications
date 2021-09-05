

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo1\UI\test4.ui" , self)
        self.setWindowIcon(QIcon(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo1\ai.ico"))
        self.setWindowTitle("الصفحـــة الرئيسية")
        # Selectors >>
        self.lb1 = self.findChild(QLabel , "link")
        self.lb1.setText("<a href='https://www.google.com'>Visit Us</a>")
        print(self.lb1.openExternalLinks()) ## to check if enable to open external links defualt = False
        self.lb1.setOpenExternalLinks(True)
        self.lb2 = self.findChild(QLabel , "img")
        self.lb2.setPixmap(QPixmap(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo1\imgs\img2.jpg"))
        
        #Set .gif image for label
        gifImg = QMovie(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo1\imgs\loader.gif")
        self.lb2.setMovie(gifImg)
        gifImg.start()

        # to get label Text:
        print(self.lb1.text())   #<a href='https://www.google.com'>Visit Us</a>

        # to clear label  text but not delete label as widget:
        # self.lb1.clear()






       


#try except..to avoid error in exists to appear in customer side 
try:
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec_()
except:
    pass

