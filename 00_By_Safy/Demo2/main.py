

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo2\UI\Demo2.ui" , self)
        self.setWindowIcon(QIcon(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo1\ai.ico"))
        self.setWindowTitle("الصفحـــة الرئيسية")
        
        
        # Selectors here>>
        self.btn = self.findChild(QPushButton , "pushButton")
        self.label = self.findChild(QLabel , "label")
        self.label.setText("<a href='https://www.google.com'> click here! </a>")

       
        self.btn.clicked.connect(self.handelButtonClicked)
        self.label.linkHovered.connect(self.handelLabelHoverSignal)
       
       #set icon for button :
        self.btn.setIcon(QIcon(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo2\Imgs\ai.ico"))
        self.btn.setIconSize(QSize(30,30))

        #make shortcut for button:
        self.btn.setShortcut("ctrl+A")

        #Enable and disabled btn:
        #self.btn.setEnabled(False)


        

    def handelButtonClicked(self):
        self.label.setText("Hello PyQt5")


    def handelLabelHoverSignal(self):
          print("Label Hovered Now!")
          self.btn.setEnabled(False)




       





       


#try except..to avoid error in exists to appear in customer side 
try:
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec_()
except Exception as error:
    print(error)

