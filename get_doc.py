from PyQt5.QtWidgets import QWidget, QLabel


class Doc(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.label = QLabel(args[-1], self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 480, 310)
        self.setWindowTitle('Doc for Moroz')
        self.label.move(20, 20)
