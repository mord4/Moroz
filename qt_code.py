from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from get_doc import Doc
from get_info import *
import sys


class Moroz(QWidget):
    def __init__(self):
        super().__init__()

        self.wtf = 0
        self.new_window = None

        layout = QGridLayout()
        self.setLayout(layout)
        self.tab = QTabWidget()
        layout.addWidget(self.tab)

        self.label_page_1 = QLabel()
        self.tab.addTab(self.label_page_1, "Уведомление")
        self.date_1_1 = QDateEdit(self.label_page_1)
        self.time_1_2 = QTimeEdit(self.label_page_1)
        self.text_edit_1_1 = QLineEdit(self.label_page_1)
        self.text_edit_1_2 = QTextEdit(self.label_page_1)
        if sys.platform == "win32":
            self.pbtn_1_1 = QPushButton("Создать", self.label_page_1)
            self.pbtn_1_2 = QPushButton("Посмотреть созданные уведомления", self.label_page_1)
        else:
            label_maker(self.label_page_1, "Ваша ОС не подходит для работы данной опции", 250, 350, 300, 20)
        label_maker(self.label_page_1, "Дата:", 20, 20, 60, 20)
        label_maker(self.label_page_1, "Время:", 20, 50, 60, 20)
        label_maker(self.label_page_1, "Заголовок:", 20, 80, 80, 20)
        label_maker(self.label_page_1, "Текст уведомления:", 20, 140, 140, 30)
        self.label_page_2 = QLabel()
        self.tab.addTab(self.label_page_2, "Сообщение TG")
        self.date_2_1 = QDateEdit(self.label_page_2)
        self.time_2_1 = QTimeEdit(self.label_page_2)
        self.text_edit_2_1 = QTextEdit(self.label_page_2)
        self.text_edit_2_2 = QTextEdit(self.label_page_2)
        self.pbtn_2_1 = QPushButton("Создать", self.label_page_2)
        self.pbtn_2_2 = QPushButton("Выбор фото:", self.label_page_2)
        self.text_edit_2_3 = QLineEdit(self.label_page_2)
        self.pbtn_2_3 = QPushButton("Посмотреть созданные уведомления", self.label_page_2)
        label_maker(self.label_page_2, "Дата:", 20, 20, 60, 20)
        label_maker(self.label_page_2, "Время:", 20, 50, 60, 20)
        label_maker(self.label_page_2, "Текст:", 20, 110, 60, 20)
        label_maker(self.label_page_2, "Ник: Moroz", 200, 20, 200, 20)
        label_maker(self.label_page_2, "Имя бота: @morozoribot", 200, 50, 200, 20)
        label_maker(self.label_page_2, "Введите ID:", 20, 80, 100, 20)

        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 800, 600)
        self.setWindowTitle('Moroz')
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        # ==============================================================================================================
        self.date_1_1.setGeometry(QtCore.QRect(80, 20, 100, 20))
        self.date_1_1.setMinimumDate(QtCore.QDate.currentDate())

        self.time_1_2.setGeometry(QtCore.QRect(80, 50, 100, 20))
        self.time_1_2.setTime(QtCore.QTime.currentTime())

        self.text_edit_1_1.setGeometry(QtCore.QRect(20, 110, 735, 30))
        self.text_edit_1_1.setText("Уведомление")

        self.text_edit_1_2.setGeometry(QtCore.QRect(20, 170, 735, 170))
        self.text_edit_1_2.setText("...")
        if sys.platform == "win32":
            self.pbtn_1_1.resize(80, 30)
            self.pbtn_1_1.move(675, 350)
            self.pbtn_1_1.clicked.connect(self.test_1)

            self.pbtn_1_2.resize(200, 30)
            self.pbtn_1_2.move(20, 400)
            self.pbtn_1_2.clicked.connect(self.open_push_db)
        else:
            label_maker(self.label_page_1, "Ваша ОС не подходит для работы данной опции", 250, 350, 300, 20)
        # ==============================================================================================================
        self.date_2_1.setGeometry(QtCore.QRect(80, 20, 100, 20))
        self.date_2_1.setMinimumDate(QtCore.QDate.currentDate())

        self.time_2_1.setGeometry(QtCore.QRect(80, 50, 100, 20))
        self.time_2_1.setTime(QtCore.QTime.currentTime())

        self.text_edit_2_1.setGeometry(QtCore.QRect(20, 140, 735, 200))
        self.text_edit_2_1.setText("...")

        self.text_edit_2_2.setGeometry(QtCore.QRect(105, 80, 70, 25))
        self.text_edit_2_2.setText("")

        self.pbtn_2_1.resize(80, 30)
        self.pbtn_2_1.move(675, 350)
        self.pbtn_2_1.clicked.connect(self.test_2)

        self.pbtn_2_2.resize(80, 30)
        self.pbtn_2_2.move(20, 350)
        self.pbtn_2_2.clicked.connect(self.overview)

        self.text_edit_2_3.setGeometry(QtCore.QRect(120, 350, 100, 30))
        self.text_edit_2_3.setReadOnly(True)

        self.pbtn_2_3.resize(200, 30)
        self.pbtn_2_3.move(20, 400)
        self.pbtn_2_3.clicked.connect(self.open_tg_db)
        # ==============================================================================================================

    def overview(self):
        file = QFileDialog.getOpenFileName(self, "Single File", "C:\\", "Images (*.png *.jpg *.jpeg)")
        self.text_edit_2_3.setText(file[0])

    def test_1(self):
        self.wtf = 1
        self.test()

    def test_2(self):
        self.wtf = 2
        self.test()

    def test(self):
        print(self.wtf)
        flag1 = True
        if self.wtf == 2:
            id_chat = str(self.text_edit_2_2.toPlainText())
            if not(len(id_chat) == 10 and id_chat.isdigit()):
                self.text_edit_2_2.setText("Плохой ID")
                flag1 = False
        if flag1:
            question = QtWidgets.QMessageBox.question(self, 'Moroz имеет вопрос',
                                                      "Создать уведомление?", QtWidgets.QMessageBox.Yes,
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
        id_chat = self.text_edit_2_2.toPlainText()
        txt = self.text_edit_2_1.toPlainText()
        file = self.text_edit_2_3.text()
        conn = sqlite3.connect('notifications.db')
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO tg_message(date, time, message, chat_id, file)"
                       f"VALUES('{dt}', '{tm}', '{txt}', '{id_chat}', '{file}')")
        conn.commit()

    def keyPressEvent(self, event):
        if int(event.modifiers()) == Qt.AltModifier:
            if event.key() == Qt.Key_D:
                self.open_doc()

    def open_doc(self):
        d = open("doc.txt")
        d = d.readlines()
        self.new_window = Doc(self, "\n".join(d))
        self.new_window.show()

    def open_push_db(self):
        self.new_window = DBPushInfo()
        self.new_window.show()

    def open_tg_db(self):
        self.new_window = DBTgInfo()
        self.new_window.show()


def label_maker(label, text, x, y, w, h):
    name = QLabel(text, label)
    name.resize(w, h)
    name.move(x, y)


def start():
    app = QApplication(sys.argv)
    ex = Moroz()
    ex.show()
    sys.exit(app.exec())


start()
