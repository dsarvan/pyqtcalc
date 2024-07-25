#!/usr/bin/env python

""" Script to create PyQt application """


import sys

from PyQt6 import QtWidgets

WINDOW_SIZE = 235  # window size in pixels


class MainWindow(QtWidgets.QMainWindow):
    """pyqtcalc main window (GUI or view)"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Calculator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(centralWidget)


def main():
    """pyqtcalc main function"""

    # create an instance of QApplication
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()  # application's GUI
    window.show()  # show application's GUI

    sys.exit(app.exec())  # application's event loop


if __name__ == "__main__":
    sys.exit(main())
