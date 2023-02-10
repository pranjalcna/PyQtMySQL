import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *
from controller import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('home.ui', self)

        self.addStudentWidgetsSetup()

        self.initializeAllStudentsTable()

        self.initializeUpdateStudentWidgets()

    def initializeAllStudentsTable(self):
        self.tblAllStudents = self.findChild(QTableWidget, 'tblAllStudents')
        colNames, data = getAllStudents()
        self.displayDataInTable(colNames, data, self.tblAllStudents)

    def initializeUpdateStudentWidgets(self):
        self.cboStudentInfo = self.findChild(QComboBox, 'cboStudentInfo')
        self.txtUpdateStuId = self.findChild(QLineEdit, 'txtUpdateStuId')
        self.txtUpdateStuFname = self.findChild(QLineEdit, 'txtUpdateStuFname')
        self.txtUpdateStuLName = self.findChild(QLineEdit, 'txtUpdateStuLName')
        self.txtUpdateStuEmail = self.findChild(QLineEdit, 'txtUpdateStuEmail')
        self.lblModifyStuFeedback = self.findChild(QLabel, 'lblModifyStuFeedback')
        self.btnUpdateStu = self.findChild(QPushButton, 'btnUpdateStu')
        self.btnDeleteStu = self.findChild(QPushButton, 'btnDeleteStu')

        colNames, rows = getStudentIdsAndNames()
        print(colNames, rows)
        for row in rows:
            self.cboStudentInfo.addItem(row[1], userData=row[0])
        self.cboStudentInfo.currentIndexChanged.connect(self.cboStudentInfoCurrentIndexChangedHandler)

    def cboStudentInfoCurrentIndexChangedHandler(self):
        try:
            stuId = self.cboStudentInfo.currentData()
            info = getStudentInfoById(stuId)
            print("info",info)
            self.txtUpdateStuId.setText(str(info['sid']))
            self.txtUpdateStuFname.setText(info['fname'])
            self.txtUpdateStuLName.setText(info['lname'])
            self.txtUpdateStuEmail.setText(info['email'])
        except Exception as e:
            print(e)



    def displayDataInTable(self, columns, rows, table:QTableWidget):
        """
        Displays the data in the rows in the table provided
        """
        table.setRowCount(len(rows))
        table.setColumnCount(len(columns))
        for i in range(len(rows)): # once for each row
            row = rows[i]
            for j in range(len(row)): # once for each cell in a given row
                table.setItem(i, j, QTableWidgetItem(str(row[j])))
        columns = ['ID', 'First Name', 'Last Name', 'Email']
        for i in range(table.columnCount()):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(f'{columns[i]}'))



    def addStudentWidgetsSetup(self):
        # widgets for add student
        self.lblAddStudentFeedback = self.findChild(QLabel, 'lblAddStudentFeedback')
        self.txtAddStuFName = self.findChild(QLineEdit, 'txtAddStuFName')
        self.txtAddStuLName = self.findChild(QLineEdit, 'txtAddStuLName')
        self.txtAddStuEmail = self.findChild(QLineEdit, 'txtAddStuEmail')
        self.btnAddStudent = self.findChild(QPushButton, 'btnAddStudent')
        self.btnAddStudent.clicked.connect(self.btnAddStudentClickHandler)

    def btnAddStudentClickHandler(self):
        try:
            fname = self.txtAddStuFName.text()
            assert fname != '', "First Name is mandatory"
            lname = self.txtAddStuLName.text()
            email = self.txtAddStuEmail.text()
            result = addStudent(fname, lname, email)
        except Exception as e:
            self.lblAddStudentFeedback.setText(str(e))
        else:
            if result == 1:
                self.lblAddStudentFeedback.setText("Student Added")
            else:
                self.lblAddStudentFeedback.setText("Student could not be added")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
