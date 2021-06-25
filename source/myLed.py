import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqt_led import Led


class MyLed(QWidget):
    def __init__(self, parent=None, isVertical=0):
        QWidget.__init__(self, parent)
        self.isVertical = isVertical
        self._layout1 = QGridLayout(self)
        self._create_leds()
        self._arrange_leds()

        # self.resize(200, 200)

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Escape:
    #         self.close()

    def _create_leds(self):
        self.gLight1 = Led(self, on_color=Led.green, off_color=Led.black, shape=Led.circle, build="debug")
        # self.gLight1.setFixedSize(40, 40)
        self.gLight1.setFocusPolicy(Qt.NoFocus)
        self.gLight1.turn_off()

        self.rLight1 = Led(self, on_color=Led.red, off_color=Led.black, shape=Led.circle, build="debug")
        # self.rLight1.setFixedSize(40, 40)
        self.rLight1.setFocusPolicy(Qt.NoFocus)
        self.rLight1.turn_off()

        self.yLight1 = Led(self, on_color=Led.yellow, off_color=Led.black, shape=Led.circle, build="debug")
        # self.yLight1.setFixedSize(40, 40)
        self.yLight1.setFocusPolicy(Qt.NoFocus)
        self.yLight1.turn_off()

    def _arrange_leds(self):
        if self.isVertical == 0:
            self._layout1.addWidget(self.gLight1, 0, 0, 0, 2, Qt.AlignCenter)
            self._layout1.addWidget(self.rLight1, 0, 1, 0, 2, Qt.AlignCenter)
            self._layout1.addWidget(self.yLight1, 0, 2, 0, 2, Qt.AlignCenter)
        else:
            self._layout1.addWidget(self.gLight1, 0, 0, 2, 0, Qt.AlignCenter)
            self._layout1.addWidget(self.rLight1, 1, 0, 2, 0, Qt.AlignCenter)
            self._layout1.addWidget(self.yLight1, 2, 0, 2, 0, Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MyLed()
    demo.show()
    sys.exit(app.exec_())