from PyQt5 import QtCore, QtWidgets, QtSql
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import sqlite3


class Moroz(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.wtf = 0

    def initUI(self):
        self.setGeometry(500, 200, 800, 600)
        self.setWindowTitle('Moroz')
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)

        layout = QGridLayout()
        self.setLayout(layout)
        tab = QTabWidget()
        layout.addWidget(tab, 0, 0)
        # ==============================================================================================================
        label = QLabel()
        tab.addTab(label, "Уведомление")

        self.date_1_1 = QDateEdit(label)
        self.date_1_1.setGeometry(QtCore.QRect(80, 20, 100, 20))
        self.date_1_1.setMinimumDate(QtCore.QDate.currentDate())

        self.time_1_2 = QTimeEdit(label)
        self.time_1_2.setGeometry(QtCore.QRect(80, 50, 100, 20))
        self.time_1_2.setTime(QtCore.QTime.currentTime())

        self.label_maker(label, "label_1_1", "Дата:", 20, 20, 60, 20)
        self.label_maker(label, "label_1_2", "Время:", 20, 50, 60, 20)
        self.label_maker(label, "label_1_3", "Заголовок:", 20, 80, 80, 20)
        self.label_maker(label, "label_1_4", "Текст уведомления:", 20, 140, 140, 30)

        self.text_edit_1_1 = QLineEdit(label)
        self.text_edit_1_1.setGeometry(QtCore.QRect(20, 110, 735, 30))
        self.text_edit_1_1.setText("Уведомление")

        self.text_edit_1_2 = QTextEdit(label)
        self.text_edit_1_2.setGeometry(QtCore.QRect(20, 170, 735, 170))
        self.text_edit_1_2.setText("...")

        self.pbtn_1_1 = QPushButton("Создать", label)
        self.pbtn_1_1.resize(80, 30)
        self.pbtn_1_1.move(675, 350)
        self.pbtn_1_1.clicked.connect(self.test_1)

        self.pbtn_1_2 = QPushButton("Посмотреть созданные уведомления", label)
        self.pbtn_1_2.resize(200, 30)
        self.pbtn_1_2.move(20, 400)
        self.pbtn_1_2.clicked.connect(self.open_push_db)
        # ==============================================================================================================
        label = QLabel()
        tab.addTab(label, "Сообщение TG")

        self.date_2_1 = QDateEdit(label)
        self.date_2_1.setGeometry(QtCore.QRect(80, 20, 100, 20))
        self.date_2_1.setMinimumDate(QtCore.QDate.currentDate())

        self.time_2_1 = QTimeEdit(label)
        self.time_2_1.setGeometry(QtCore.QRect(80, 50, 100, 20))
        self.time_2_1.setTime(QtCore.QTime.currentTime())

        self.label_maker(label, "label_2_1", "Дата:", 20, 20, 60, 20)
        self.label_maker(label, "label_2_2", "Время:", 20, 50, 60, 20)
        self.label_maker(label, "label_2_4", "Текст:", 20, 110, 60, 20)
        self.label_maker(label, "label_2_5", "Ник: Moroz", 200, 20, 200, 20)
        self.label_maker(label, "label_2_6", "Имя бота: @morozoribot", 200, 50, 200, 20)
        self.label_maker(label, "label_2_7", "Введите ID:", 20, 80, 200, 20)

        self.text_edit_2_1 = QTextEdit(label)
        self.text_edit_2_1.setGeometry(QtCore.QRect(20, 140, 735, 200))
        self.text_edit_2_1.setText("...")

        self.text_edit_2_2 = QLineEdit(label)
        self.text_edit_2_2.setGeometry(QtCore.QRect(105, 75, 75, 25))
        self.text_edit_2_2.setText("")

        self.pbtn_2_1 = QPushButton("Создать", label)
        self.pbtn_2_1.resize(80, 30)
        self.pbtn_2_1.move(675, 350)
        self.pbtn_2_1.clicked.connect(self.test_2)

        self.pbtn_2_2 = QPushButton("Выбор фото:", label)
        self.pbtn_2_2.resize(80, 30)
        self.pbtn_2_2.move(20, 350)
        self.pbtn_2_2.clicked.connect(self.overview)

        self.text_edit_2_3 = QLineEdit(label)
        self.text_edit_2_3.setGeometry(QtCore.QRect(120, 350, 100, 30))

        self.pbtn_2_3 = QPushButton("Посмотреть созданные уведомления", label)
        self.pbtn_2_3.resize(200, 30)
        self.pbtn_2_3.move(20, 400)
        self.pbtn_2_3.clicked.connect(self.open_tg_db)
        # ==============================================================================================================

    def overview(self):
        fileName = QFileDialog.getOpenFileName(self, "Single File", "C:\\", "Images (*.png *.jpg *.jpeg)")
        self.text_edit_2_3.setText(fileName[0])

    def label_maker(self, label, name, text, x, y, w, h):
        self.name = QLabel(text, label)
        self.name.resize(w, h)
        self.name.move(x, y)

    def test_1(self):
        self.wtf = 1
        self.test()

    def test_2(self):
        self.wtf = 2
        self.test()

    def test(self):
        print(self.wtf)
        message = 'Создать уведомление?'
        question = QtWidgets.QMessageBox.question(self,
                                                  'Moroz имеет вопрос',
                                                  message,
                                                  QtWidgets.QMessageBox.Yes,
                                                  QtWidgets.QMessageBox.No)

        if question == QtWidgets.QMessageBox.Yes:
            if self.wtf == 1:
                self.click_btn_1_1()
            elif self.wtf == 2:
                self.click_btn_2_1()

    def click_btn_1_1(self):
        dt = self.date_1_1.date().getDate()
        tm = self.time_1_2.time().toString()
        nm = self.text_edit_1_1.text()
        txt = self.text_edit_1_2.toPlainText()

        conn = sqlite3.connect('notifications.db')
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO push_notif (date, time, title, text) VALUES ('{dt}', '{tm}', '{nm}', '{txt}')")
        conn.commit()

    def click_btn_2_1(self):
        dt = self.date_2_1.date().getDate()
        tm = self.time_2_1.time().toString()
        txt = self.text_edit_2_1.toPlainText()
        id = self.text_edit_2_2.text()
        file = self.text_edit_2_3.text()

        conn = sqlite3.connect('notifications.db')
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO tg_message(date, time, message, chat_id, file) VALUES('{dt}', '{tm}', '{txt}', '{id}', '{file}')")
        conn.commit()

    def keyPressEvent(self, event):
        if int(event.modifiers()) == Qt.AltModifier:
            if event.key() == Qt.Key_D:
                self.open_doc()

    def open_doc(self):
        d = open("doc.txt")
        d = d.readlines()
        self.doci = Doc(self, "\n".join(d))
        self.doci.show()

    def open_push_db(self):
        self.d = DB_push_info()
        self.d.show()

    def open_tg_db(self):
        self.d = DB_tg_info()
        self.d.show()


class Doc(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 480, 310)
        self.setWindowTitle('Doc for Moroz')
        self.label = QLabel(args[-1], self)
        self.label.move(20, 20)


class DB_push_info(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 300)
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

        table = QTableWidget(self)
        table.setColumnCount(4)
        table.setRowCount(len(res))

        table.setHorizontalHeaderLabels(["Дата", "Время", "Заголовок", "Текст"])

        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        table.horizontalHeaderItem(3).setToolTip("Column 4 ")

        for i in range(len(res)):
            table.setItem(i, 0, QTableWidgetItem(res[i][0]))
            table.setItem(i, 1, QTableWidgetItem(res[i][1]))
            table.setItem(i, 2, QTableWidgetItem(res[i][2]))
            table.setItem(i, 3, QTableWidgetItem(res[i][3]))

        table.resizeColumnsToContents()

        grid_layout.addWidget(table, 0, 0)


class DB_tg_info(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 300)
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

        table = QTableWidget(self)
        table.setColumnCount(5)
        table.setRowCount(len(res))

        table.setHorizontalHeaderLabels(["Дата", "Время", "Сообщение", "ID", "Путь к фото"])

        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        table.horizontalHeaderItem(3).setToolTip("Column 4 ")
        table.horizontalHeaderItem(4).setToolTip("Column 5 ")

        for i in range(len(res)):
            table.setItem(i, 0, QTableWidgetItem(res[i][0]))
            table.setItem(i, 1, QTableWidgetItem(res[i][1]))
            table.setItem(i, 2, QTableWidgetItem(res[i][2]))
            table.setItem(i, 3, QTableWidgetItem(res[i][3]))
            table.setItem(i, 4, QTableWidgetItem(res[i][4]))

        table.resizeColumnsToContents()

        grid_layout.addWidget(table, 0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Moroz()
    ex.show()
    sys.exit(app.exec())