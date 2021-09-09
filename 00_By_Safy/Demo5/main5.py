from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5 import uic

from icecream import ic



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo5\UI\Demo5.ui" , self)
        self.setWindowIcon(QIcon(r"C:\Users\Mahmoud Shehata\Desktop\All-Desktop-Apps-Repo\00_By_Safy\Demo5\Imgs\ai.ico"))
        self.setWindowTitle("الصفحـــة الرئيسية")


        # Selectors here>>
        # info 1
        self.ent1 = self.findChild(QLineEdit ,  "lineEdit")
        self.ent1.setClearButtonEnabled(True)  #to Enable clear button in inputbox

        # info 2:
        # if you need to check if lineEdit set property that return T or F , you can use is+property name(isClearButtonEnabled())
        # but in you need to check prop that tack value as PlaceholderText("value") , you can use propName("it's value") that retun T if it has vaue
        ic(self.ent1.isClearButtonEnabled()) #ic| self.ent1.isClearButtonEnabled(): True
        ic(self.ent1.placeholderText()) #ic| self.ent1.placeholderText(): ''

        # info3:signals and slots of lineEdit
        # 1- returnPressed : it is event that fire when Enter btn is clicked
        self.ent1.returnPressed.connect(self.handelReturnPressedSignal)
        
        # 2-editingFinished: it is an event that fire when we finish editing textBox , i see that is similar to previous event 
        # we can use this feature if we do not need to put login put and after user enter his pass and click enter send data to database..nice
        self.ent1.editingFinished.connect(self.handelEditingFinishedSignal)


        # 3-inputRejected: Event fired or slot fired when we enter data in textBox not match prespecified data that determined in textbox Validator
        self.ent1.setValidator(QIntValidator())
        self.ent1.inputRejected.connect(self.handelIputRejectedSignal) 


        # 4- redo and undo slots that inplements on lineEdit widget:
        self.btn1 = self.findChild(QPushButton , "pushButton")
        self.btn2 = self.findChild(QPushButton , "pushButton_2")
        self.btn1.clicked.connect(self.makeRedoTask)
        self.btn2.clicked.connect(self.makeUndoTask)



        


        


    # Signals Here>>
    def handelReturnPressedSignal(self):
        ic("Enter Button is Clickd !")  #ic| 'Enter Button is Clickd !'
    
    def handelEditingFinishedSignal(self):
        ic(self.ent1.text()) #ic| self.ent1.text(): 'Mahmoud'
    
    def handelIputRejectedSignal(self):
        ic("Input not Valid Enter number only") #ic| 'Input not Valid Enter number only'


    def makeRedoTask(self):
        self.ent1.redo()
    
    
    def makeUndoTask(self):
        self.ent1.undo()
        
      


    # Slots Here:
   




#try except..to avoid error in exists to appear in customer side 
try:
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec_()
except Exception as error:
    print(error)

