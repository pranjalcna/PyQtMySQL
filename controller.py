# getStudentInfoById
from mysql_functions import *

def addStudent(fname, lname, email):
    sql = f"INSERT INTO `school`.`students` (`first_name`, `last_name`, `email`) VALUES ('{fname}', '{lname}', '{email}');"
    return executeQueryAndCommit(sql)

def getAllStudents():
    sql = "SELECT * FROM school.students;"
    return executeQueryAndReturnResult(sql)

def getStudentIdsAndNames():
    sql =f"SELECT student_id, concat(first_name, ' ', last_name) as 'Student Name' FROM school.students;"
    return executeQueryAndReturnResult(sql)

def getStudentInfoById(stuId):
    sql = f"SELECT * FROM school.students where student_id = {stuId}; "
    stuInfo = executeQueryAndReturnResult(sql)[1][0]
    print('stuinfo',stuInfo)
    data = {'sid': stuInfo[0], 'fname': stuInfo[1], 'lname': stuInfo[2], 'email': stuInfo[3]}
    print(data)
    return data

def updateStudent(sid, fname, lname, email):
    sql = f"UPDATE `school`.`students` SET `first_name` = '{fname}', `last_name` = '{lname}', `email` = '{email}' WHERE (`student_id` = '{sid}');"
    return executeQueryAndCommit(sql)

def deleteStudentById(sid):
    sql = f"DELETE FROM `school`.`students` WHERE (`student_id` = '{sid}');"
    return executeQueryAndCommit(sql)
