import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)
        self.flag = False

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        self.drawCircule(p)
        p.end()

    def draw(self):
        self.flag = True
        if self.flag:
            self.repaint()

    def drawCircule(self, p):
        if self.flag:
            rand = random.randint(1, 200)
            p.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            p.drawEllipse(250, 200, rand, rand)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
