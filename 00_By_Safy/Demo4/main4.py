from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5 import uic



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo4\UI\Demo4.ui" , self)
        self.setWindowIcon(QIcon(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo4\Imgs\ai.ico"))
        self.setWindowTitle("الصفحـــة الرئيسية")


        # Selectors here>>
        self.ent1 = self.findChild(QLineEdit , "lineEdit")
        self.ent1.setMaxLength(10) #to set maxlength for line edit
        # self.ent1.setInputMask("0000-000-000-00") #to set mask to your input as phone number or anything like this
        self.ent1.setDragEnabled(True) #to make line edit content dragable and drobed

        completer = QCompleter(["Mahmoud","Muhammed","Moaz","Mourad"])
        self.ent1.setCompleter(completer)
         
        self.ent2 = self.findChild(QLineEdit , "lineEdit_2")
        self.selectbtn = self.findChild(QPushButton , "pushButton_6")
        self.unSelectbtn = self.findChild(QPushButton , "pushButton_5")
        self.copyBtn = self.findChild(QPushButton , "pushButton_4")
        self.pasteBtn = self.findChild(QPushButton , "pushButton_3")
        self.cutBtn = self.findChild(QPushButton , "pushButton_2")
        self.clearBtn = self.findChild(QPushButton , "pushButton")


        # Signals Here >>
        self.selectbtn.clicked.connect(self.handelSelectSignal)
        self.unSelectbtn.clicked.connect(self.handelUnslectSignal)
        self.copyBtn.clicked.connect(self.handelCopySignal)
        self.pasteBtn.clicked.connect(self.handelPasteSignal)
        self.cutBtn.clicked.connect(self.handelCutSignal)
        self.clearBtn.clicked.connect(self.handelClearSignal)


    # Slots Here:
    def handelSelectSignal(self):
      self.ent1.selectAll()
    
    def handelUnslectSignal(self):
        self.ent1.deselect()

    def handelCopySignal(self):
        self.ent1.copy()

    def handelPasteSignal(self):
       self.ent2.paste()
       self.ent2.setReadOnly(True) #to make lineEdit ReadOnly
    
    def handelCutSignal(self):
        self.ent1.cut()

    def handelClearSignal(self):
        self.ent1.clear()
        self.ent2.clear()





#try except..to avoid error in exists to appear in customer side 
try:
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec_()
except Exception as error:
    print(error)

