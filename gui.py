import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('home.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
