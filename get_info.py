from PyQt5.QtWidgets import *
import db_code


class InfoHub(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.res = []
        self.table = QTableWidget(self)
        self.pbtn = QPushButton("Удалить", self)
        self.docy = QLabel("Чтобы удалить\nуведомление\nвыберете\nлюбой элемент\nтаблицы,\n"
                           "просто нажав\nна него,\nи нажмите\nкнопку\nудалить.", self)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 300)
        self.setWindowTitle('infohub')
        self.info()

    def info(self):
        res = db_code.get_data()

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.table.setColumnCount(8)
        self.table.setRowCount(len(res))

        self.table.setHorizontalHeaderLabels(["Дата", "Время", "Заголовок",
                                              "Текст", "Telegram", "Push", "e-mail", "Фото"])

        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.table.horizontalHeaderItem(3).setToolTip("Column 4 ")
        self.table.horizontalHeaderItem(4).setToolTip("Column 5 ")
        self.table.horizontalHeaderItem(5).setToolTip("Column 6 ")
        self.table.horizontalHeaderItem(6).setToolTip("Column 7 ")
        self.table.horizontalHeaderItem(7).setToolTip("Column 8 ")

        for i in range(len(res)):
            self.table.setItem(i, 0, QTableWidgetItem(res[i][0]))
            self.table.setItem(i, 1, QTableWidgetItem(res[i][1]))
            self.table.setItem(i, 2, QTableWidgetItem(res[i][2]))
            self.table.setItem(i, 3, QTableWidgetItem(res[i][3]))
            self.table.setItem(i, 4, QTableWidgetItem(res[i][4]))
            self.table.setItem(i, 5, QTableWidgetItem(res[i][5]))
            self.table.setItem(i, 6, QTableWidgetItem(res[i][6]))
            self.table.setItem(i, 7, QTableWidgetItem(res[i][7]))

        self.table.resizeRowsToContents()

        grid_layout.addWidget(self.table)

        self.pbtn.resize(120, 100)
        self.pbtn.move(840, 180)

        self.docy.resize(100, 200)
        self.docy.move(840, -20)
