#!/usr/bin/env python

""" Script to create PyQt application """


import sys


from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets

WINDOW_SIZE = 235  # window size in pixels

DISPLAY_HEIGHT = 45  # display height in pixels


class MainWindow(QtWidgets.QMainWindow):
    """pyqtcalc main window (GUI or view)"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Calculator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)

        self.generalLayout = QtWidgets.QVBoxLayout()
        centralWidget = QtWidgets.QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createDisplay()

    def _createDisplay(self):
        """create application's display"""
        self.display = QtWidgets.QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)


def main():
    """pyqtcalc main function"""

    # create an instance of QApplication
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()  # application's GUI
    window.show()  # show application's GUI

    sys.exit(app.exec())  # application's event loop


if __name__ == "__main__":
    sys.exit(main())
