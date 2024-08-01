#!/usr/bin/env python

""" Script to create PyQt application """


import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt

WINDOW_SIZE = 235  # window size in pixels
DISPLAY_HEIGHT = 45  # display height in pixels
BUTTON_SIZE = 40  # button size in pixels
ERROR_MSG = "ERROR"  # error message


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
        self._createButtons()

    def _createDisplay(self):
        """create application's display"""
        self.display = QtWidgets.QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """create application's keyboard buttons"""
        self.buttonMap = {}
        buttonLayout = QtWidgets.QGridLayout()
        keyboard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", ".", "%", "+", "="],
        ]

        for row, keys in enumerate(keyboard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QtWidgets.QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonLayout)

    def setDisplayText(self, text):
        """sets and updates display's text"""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """gets current display's text"""
        return self.display.text()

    def clearDisplay(self):
        """clears display's text"""
        self.setDisplayText("")


def evaluateExpression(expression):
    """evaluate math expressions (model)"""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result


def main():
    """pyqtcalc main function"""

    # create an instance of QApplication
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()  # application's GUI
    window.show()  # show application's GUI

    sys.exit(app.exec())  # application's event loop


if __name__ == "__main__":
    sys.exit(main())
