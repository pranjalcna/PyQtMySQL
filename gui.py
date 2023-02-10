import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *
from controller import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('home.ui', self)

        # widgets for add student
        self.lblAddStudentFeedback = self.findChild(QLabel, 'lblAddStudentFeedback')
        self.txtAddStuFName = self.findChild(QLineEdit, 'txtAddStuFName')
        self.txtAddStuLName = self.findChild(QLineEdit, 'txtAddStuLName')
        self.txtAddStuEmail = self.findChild(QLineEdit, 'txtAddStuEmail')
        self.btnAddStudent = self.findChild(QPushButton, 'btnAddStudent')
        self.btnAddStudent.clicked.connect(self.btnAddStudentClickHandler)

    def btnAddStudentClickHandler(self):
        fname = self.txtAddStuFName.text()
        lname = self.txtAddStuLName.text()
        email = self.txtAddStuEmail.text()
        result = addStudent(fname, lname, email)
        if result == 1:
            # success
            pass
        else:
            # fail
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
