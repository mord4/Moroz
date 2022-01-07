from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from get_info import InfoHub
from get_doc import Doc
from db_code import add_data, get_id
import sys


class Moroz(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.window = None
        self.send_tg = False
        self.send_tg_1 = True
        self.send_push = False
        self.send_email = False

        if sys.platform == "win32":
            self.create_push = True
        else:
            self.create_push = False

        label_maker(self, "Дата:", 20, 20, 60, 20)
        label_maker(self, "Время:", 20, 50, 60, 20)
        label_maker(self, "Заголовок:", 20, 180, 80, 20)
        label_maker(self, "Текст уведомления:", 20, 260, 140, 30)

        self.tg = QCheckBox("Сообщение в Telegram", self)
        self.push = QCheckBox("push-уведомление Windows", self)
        self.email = QCheckBox("Письмо на электронную почту", self)

        self.date = QDateEdit(self)
        self.time = QTimeEdit(self)

        self.text_edit_1 = QTextEdit(self)  # Заголовок
        self.text_edit_2 = QTextEdit(self)  # Текст уведомления

        self.text_edit_3 = QLineEdit(self)  # ID
        self.text_edit_3.close()

        self.attention = QLabel("Ваша ОС не подходит для данной задачи", self)
        self.attention.close()

        self.text_edit_5 = QLineEdit(self)  # e-mail
        self.text_edit_5.close()

        self.text_edit_6 = QLineEdit(self)

        self.pbtn_1 = QPushButton("Создать", self)
        self.pbtn_2 = QPushButton("Посмотреть созданные уведомления", self)
        self.pbtn_3 = QPushButton("Выбор фото:", self)

        self.initUI()

    def initUI(self):

        self.setGeometry(500, 200, 800, 600)
        self.setWindowTitle('Moroz')
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)

        self.date.setGeometry(QtCore.QRect(80, 20, 100, 20))
        self.date.setMinimumDate(QtCore.QDate.currentDate())

        self.tg.move(20, 90)
        self.tg.clicked.connect(self.tg_box_click)
        self.push.move(20, 120)
        self.push.clicked.connect(self.push_box_click)
        self.email.move(20, 150)
        self.email.clicked.connect(self.email_box_click)

        self.time.setGeometry(QtCore.QRect(80, 50, 100, 20))
        self.time.setTime(QtCore.QTime.currentTime())

        self.text_edit_1.setGeometry(QtCore.QRect(20, 220, 735, 30))
        self.text_edit_1.setText("Уведомление")

        self.text_edit_2.setGeometry(QtCore.QRect(20, 300, 735, 170))
        self.text_edit_2.setText("...")

        self.text_edit_3.setGeometry(QtCore.QRect(220, 90, 300, 20))

        self.text_edit_6.setGeometry(QtCore.QRect(420, 480, 100, 30))
        self.text_edit_6.setReadOnly(True)

        self.attention.move(220, 120)
        self.attention.resize(300, 20)

        self.text_edit_5.setGeometry(QtCore.QRect(220, 150, 300, 20))

        self.pbtn_1.move(675, 480)
        self.pbtn_1.resize(80, 30)
        self.pbtn_1.clicked.connect(self.create_reminder)

        self.pbtn_2.move(20, 480)
        self.pbtn_2.resize(200, 30)
        self.pbtn_2.clicked.connect(self.open_info)

        self.pbtn_3.move(300, 480)
        self.pbtn_3.resize(100, 30)
        self.pbtn_3.clicked.connect(self.overview)

    def tg_box_click(self):
        if self.tg.isChecked():
            self.text_edit_3.show()
            self.send_tg = True
        else:
            self.text_edit_3.close()
            self.send_tg = False

    def push_box_click(self):
        if not self.create_push:
            if self.push.isChecked():
                self.attention.show()
            else:
                self.attention.close()
        else:
            if self.push.isChecked():
                self.send_push = True
            else:
                self.send_push = False

    def email_box_click(self):
        if self.email.isChecked():
            self.text_edit_5.show()
            self.send_email = True
        else:
            self.text_edit_5.close()
            self.send_email = False

    def keyPressEvent(self, event):
        if int(event.modifiers()) == Qt.AltModifier:
            if event.key() == Qt.Key_D:
                d = open("doc.txt")
                d = d.readlines()
                self.window = Doc(self, "\n".join(d))
                self.window.show()

    def overview(self):
        file = QFileDialog.getOpenFileName(self, "Single File", "C:\\", "Images (*.png *.jpg *.jpeg)")
        self.text_edit_6.setText(file[0])

    def open_info(self):
        self.window = InfoHub()
        self.window.show()

    def create_reminder(self):
        if self.tg.isChecked() or self.push.isChecked() or self.email.isChecked():
            date = self.date.date().getDate()
            time = self.time.time().toString()
            title = self.text_edit_1.toPlainText()
            text = self.text_edit_2.toPlainText()

            if self.send_tg and len(self.text_edit_3.text()) != 0:
                self.send_tg_1 = True
                tg = self.text_edit_3.text()
                if get_id(tg):
                    QMessageBox.critical(QWidget(), 'Ошибка!', "Такого ID нет в базе")
                    self.send_tg_1 = False
            else:
                tg = "no"

            if self.create_push and self.send_push:
                push = "yes"
            else:
                push = "no"

            if len(self.text_edit_5.text()) != 0 and self.send_email:
                email = self.text_edit_5.text()
            else:
                email = "no"

            photo = "no"

            if self.send_tg_1 or self.send_push or self.send_email:
                print([date, time, title, text, tg, push, email, photo])
                add_data(date, time, title, text, tg, push, email, photo)

        else:
            QMessageBox.critical(QWidget(), 'Ошибка!', "Вы ничего не выбрали")


def label_maker(label, text, x, y, w, h):
    name = QLabel(text, label)
    name.resize(w, h)
    name.move(x, y)
    name.setFont(QtGui.QFont("Impact", 10))


def start():
    app = QApplication(sys.argv)
    ex = Moroz()
    ex.show()
    sys.exit(app.exec())


start()
