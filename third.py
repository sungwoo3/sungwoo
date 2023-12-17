import sys
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyautogui
import time
import pyperclip

class Worker(QThread):
    timeout = pyqtSignal(str) 

    def __init__(self):
        super().__init__()
        self.position = 0


    def run(self):
        while True:
            self.position = pyautogui.position()
            self.timeout.emit(str(self.position))     # 방출
            # self.timeout.emit(self.num)  
            # self.num+=1 
            self.sleep(1)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.macro()
        self.worker = Worker()
        self.worker.start()
        self.worker.timeout.connect(self.timeout)   # 시그널 슬롯 등록
       

    def macro(self):
        self.setGeometry(800, 400, 300, 200)
        self.setWindowTitle('macro program')
        self.position = pyautogui.position()
        
        XLabel = QLabel("Position X:   ", self)
        XLabel.move(20, 20)
        YLabel = QLabel("Position Y:   ", self)
        YLabel.move(20, 40)

        self.label = QLabel(self)
        self.label.move(20,90)
        self.label.resize(300,30)

        self.label2 = QLabel(self)
        self.label2.move(20,60)
        self.label2.resize(300,30)

        self.label3 = QLabel("x값과 y값을 입력하세요.",self)
        self.label3.move(20,120)
        self.label3.resize(300,30)

        

        self.linex = QLineEdit(self)
        self.linex.move(100, 20)
        self.linex.resize(200, 25)
        self.liney = QLineEdit(self)
        self.liney.move(100, 40)
        self.liney.resize(200, 25)

        btn1 = QPushButton("Start", self)
        btn1.move(20, 150)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton("Clear", self)
        btn2.move(140, 150)
        btn2.clicked.connect(self.btn2_clicked)

 
        self.center()

    @pyqtSlot(str)
    def timeout(self, pos):
        
        self.label2.setText(pos)

    def btn1_clicked(self):
        self.x = self.linex.text()
        self.y = self.liney.text()
        self.label.setText("X point: " + self.x + " Y point: "+ self.y)
        pyautogui.moveTo(int(self.x), int(self.y))    
        pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다
        # pyautogui.rightClick()   

    def btn2_clicked(self):
        self.label.clear()
        self.linex.clear()
        self.liney.clear()

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