from facebase import Ui_MainWindow
from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":
    App = QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(App.exec_())