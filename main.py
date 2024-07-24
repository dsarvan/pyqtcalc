#!/usr/bin/env python

""" Script to create PyQt application """


import sys

from PyQt6 import QtWidgets


def main():
    """pyqt application"""

    # create an instance of QApplication
    app = QtWidgets.QApplication(sys.argv)

    win = QtWidgets.QWidget()  # application's GUI
    win.setWindowTitle("PyQt Calculator!")
    win.setGeometry(100, 100, 280, 80)

    msg = QtWidgets.QLabel("<h4>PyQt Calculator!</h4>", parent=win)
    msg.move(60, 15)

    win.show()  # show application's GUI
    sys.exit(app.exec())  # application's event loop


if __name__ == "__main__":
    sys.exit(main())
