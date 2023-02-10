# getStudentInfoById
from mysql_functions import *

def addStudent(fname, lname, email):
    sql = f"INSERT INTO `school`.`students` (`first_name`, `last_name`, `email`) VALUES ('{fname}', '{lname}', '{email}');"
    return executeQueryAndCommit(sql)

def getAllStudents():
    sql = "SELECT * FROM school.students;"
    return executeQueryAndReturnResult(sql)
