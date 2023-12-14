import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt
import pyautogui
import time
import pyperclip


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      btn = QPushButton('Quit', self)
      btn.move(400, 20)
      btn.resize(btn.sizeHint())
      btn.clicked.connect(QCoreApplication.instance().quit)

      self.setWindowTitle('macro')
      self.setWindowIcon(QIcon('web.png'))
      self.setWindowTitle('macro program')
      self.setGeometry(600, 300, 500, 300)

      position = pyautogui.position()

      textLabel = QLabel("Message: ", self)
      textLabel.move(20, 20)

      label = QLabel("",self)
      label.move(80,20)
      label.resize(150,30)

      btn1 = QPushButton("Set", self)
      btn1.move(20, 60)
      btn1.clicked.connect(self.btn1_clicked)

      btn2 = QPushButton("Clear", self)
      btn2.move(140, 60)
      btn2.clicked.connect(self.btn2_clicked)
     
      self.center()
      # self.show()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def btn1_clicked(self):
      self.label.setText("버튼이 클릭되었습니다.")

  def btn2_clicked(self):
      self.label.clear()
     
  
if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  ex.show()
  app.exec_()
  # sys.exit(app.exec_())