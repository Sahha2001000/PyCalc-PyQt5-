from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def add_label(i = 1):
    print('add')
    i+=1
    print(i)

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('First desktop app')
    window.setGeometry(0,0,350,350)

    mainText = QtWidgets.QLabel(window)
    mainText.setText('TEXT TEST 1 TEXT TEST TEXT TEST TEXT TEST TEXT TEST22 ')
    mainText.move(10,100)
    mainText.adjustSize()

    btn = QtWidgets.QPushButton(window)
    btn.move(150,170)
    btn.setText('btn')
    btn.setFixedSize(40,50)
    btn.clicked.connect(add_label)

    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    application()