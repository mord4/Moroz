from PyQt5.QtWidgets import *
from db_code import delete_data
import sqlite3, sys


class DBPushInfo(QWidget):
    def __init__(self):
        super().__init__()

        self.res = []
        self.table = QTableWidget(self)
        self.pbtn = QPushButton("Удалить", self)
        self.docy = QLabel("Чтобы удалить\nуведомление\nвыберете\nлюбой элемент таблтцы,\n"
                           "просто нажав\nна него,\nи нажмите\nкнопку\nудалить.", self)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 640, 300)
        self.setWindowTitle('DB_push_info')
        self.push_info()

    def push_info(self):
        connection = sqlite3.connect("notifications.db")
        query = """
                    select * from push_notif
                """
        res = connection.cursor().execute(query).fetchall()
        connection.close()

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.table.setColumnCount(4)
        self.table.setRowCount(len(res))

        self.table.setHorizontalHeaderLabels(["Дата", "Время", "Заголовок", "Текст"])

        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")

        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.table.horizontalHeaderItem(3).setToolTip("Column 4 ")

        for i in range(len(res)):
            self.table.setItem(i, 0, QTableWidgetItem(res[i][0]))
            self.table.setItem(i, 1, QTableWidgetItem(res[i][1]))
            self.table.setItem(i, 2, QTableWidgetItem(res[i][2]))
            self.table.setItem(i, 3, QTableWidgetItem(res[i][3]))

        self.table.resizeRowsToContents()

        grid_layout.addWidget(self.table)

        self.table.cellClicked.connect(self.cell_was_clicked)

        self.pbtn.resize(80, 30)
        self.pbtn.move(540, 20)
        self.pbtn.clicked.connect(self.deleter)

        self.docy.resize(80, 150)
        self.docy.move(540, 60)

    def cell_was_clicked(self, row):
        self.res = [self.table.item(row, i).text() for i in range(4)]
        print(self.res)

    def deleter(self):
        if self.res:
            delete_data("push_notif", self.res)
            self.res = []


class DBTgInfo(QWidget):
    def __init__(self):
        super().__init__()

        self.res = []
        self.table = QTableWidget(self)
        self.pbtn = QPushButton("Удалить", self)
        self.docy = QLabel("Чтобы удалить\nуведомление\nвыберете\nлюбой элемент таблтцы,\n"
                           "просто нажав\nна него,\nи нажмите\nкнопку\nудалить.", self)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 640, 300)
        self.setWindowTitle('DB_tg_info')
        self.tg_info()

    def tg_info(self):
        connection = sqlite3.connect("notifications.db")
        query = """
            select * from tg_message
        """
        res = connection.cursor().execute(query).fetchall()
        connection.close()

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.table.setColumnCount(5)
        self.table.setRowCount(len(res))

        self.table.setHorizontalHeaderLabels(["Дата", "Время", "Сообщение", "ID", "Путь к фото"])

        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.table.horizontalHeaderItem(3).setToolTip("Column 4 ")
        self.table.horizontalHeaderItem(4).setToolTip("Column 5 ")

        for i in range(len(res)):
            self.table.setItem(i, 0, QTableWidgetItem(res[i][0]))
            self.table.setItem(i, 1, QTableWidgetItem(res[i][1]))
            self.table.setItem(i, 2, QTableWidgetItem(res[i][2]))
            self.table.setItem(i, 3, QTableWidgetItem(res[i][3]))
            self.table.setItem(i, 4, QTableWidgetItem(res[i][4]))

        self.table.resizeRowsToContents()

        grid_layout.addWidget(self.table)

        self.table.cellClicked.connect(self.cell_was_clicked)

        self.pbtn.resize(80, 30)
        self.pbtn.move(540, 20)
        self.pbtn.clicked.connect(self.deleter)

        self.docy.resize(80, 150)
        self.docy.move(540, 60)

    def cell_was_clicked(self, row):
        self.res = [self.table.item(row, i).text() for i in range(5)]

    def deleter(self):
        if self.res:
            delete_data("tg_message", self.res)
            self.res = []
