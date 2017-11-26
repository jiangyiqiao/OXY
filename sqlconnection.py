#!/usr/bin/env python
from PyQt5 import QtWidgets, QtSql

def openConnection():

    conn.setDatabaseName('./db/database.db')

    if conn.open():
        print("打开数据库成功！")
        return True
    else:
        print("打开数据库失败！")
        return False

def createTable():
    query = QtSql.QSqlQuery()
    query.exec_("create table patient(Patient_ID int primary key auto_increment not null,Patient_name varchar(20) not null,"
                "Patient_sex varchar(2)not null,Patient_age int(4)not null,Patient_mainDoct varchar(20),"
                "Patient_fundDoct varchar(20),Patient_hosID varchar(10),Patient_phone varchar(20),"
                "mainDoct_time date,fundDoct_time date,mainDoct_sesion varchar(100),fundDoct_session varchar(100))")
    print("创建病人表成功！")

    query.exec_("create table doctor(doct_ID int primary key auto_increment not null,doct_name varchar(20)not null,"
                "Doct_sex varchar(2)not null,Patient_name varchar(20),Patient_sex varchar(2),Patient_age int(4),"
                "Patient_hosID varchar(10),Maindoct varchar(2),Funddoct varchar(2))")
    print("创建医生表成功！")


def insertTable():
    query = QtSql.QSqlQuery()

    query.exec_("insert into patient values(0,'王一','男',20,)")
    print("插入病人信息表成功！")

    query.exec_("insert into doctor values(1, '李一')")
    print("插入医生信息表成功！")



def queryTable():
    query = QtSql.QSqlQuery('select * from patient')
    if query.isActive():
        print("查询表成功！")
        query.first()
        while query.isValid():
            print(query.value(0), query.value(1),query.value(2))
            query.next()
    else:
        print("查询表失败！")
    queryDoct = QtSql.QSqlQuery('select * from doctor')
    if queryDoct.isActive():
        print("查询表成功！")
        queryDoct.first()
        while queryDoct.isValid():
            print(queryDoct.value(0), queryDoct.value(1))
            queryDoct.next()
    else:
        print("查询表失败！")

def closeConnection():
    conn.close()
    print("成功关闭数据库！")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    conn=QtSql.QSqlDatabase.addDatabase('QSQLITE')
    openConnection()
    createTable()
    insertTable()
    queryTable()
    closeConnection()
    sys.exit(app.exec_())
