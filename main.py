import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
            p.setBrush(QColor(255, 255, 0))
            temp = random.randint(1, 200)
            p.drawEllipse(250, 200, temp, temp)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
