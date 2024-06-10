#!/usr/bin/env python

""" Script to create PyQt application """


import sys

from PyQt6 import QtWidgets


def main():
    """PyQt application"""

    app = QtWidgets.QApplication(sys.argv)

    win = QtWidgets.QWidget()
    win.setWindowTitle("PyQt Calculator!")
    win.setGeometry(100, 100, 280, 80)

    msg = QtWidgets.QLabel("<h1>PyQt Calculator!</h1>", parent=win)
    msg.move(60, 15)

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
