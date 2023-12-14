import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyautogui
import time
import pyperclip

class Worker(QThread):
    timeout = pyqtSignal(int) 

    def __init__(self):
        super().__init__()
        self.num =0


    def run(self):
        while True:
            self.position = pyautogui.position()
            # self.timeout.emit(self.position)     # 방출
            self.timeout.emit(self.num)  
            self.num+=1
            
            
            self.sleep(1)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.worker = Worker()
        self.worker.start()
        self.worker.timeout.connect(self.timeout)   # 시그널 슬롯 등록

    def setupUI(self):
        self.setGeometry(800, 400, 300, 150)
        self.setWindowTitle('macro program')
        # self.position = pyautogui.position()
        
        textLabel = QLabel("Message:   ", self)
        textLabel.move(20, 20)

        self.label = QLabel("", self)
        self.label.move(80, 20)
        self.label.resize(300, 30)

        btn1 = QPushButton("Click", self)
        btn1.move(20, 60)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton("Clear", self)
        btn2.move(140, 60)
        btn2.clicked.connect(self.btn2_clicked)

        self.edit = QLineEdit(self)
        self.edit.move(100, 20)

        self.center()

    @pyqtSlot(int)
    def timeout(self, num):
        self.edit.setText(str(num))

    def btn1_clicked(self):
        self.label.setText(str(self.position))

    def btn2_clicked(self):
        self.label.clear()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()