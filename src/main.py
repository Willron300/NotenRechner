# -*- coding: iso-8859-1 -*-
from PySide.QtCore import *
from PySide.QtGui import *
import os
import sys
from src.gui.gui import MainWindow


def main():
    path = os.path.realpath('__file__')
    app = QApplication(sys.argv)
    try:
        gui = MainWindow(app)
        gui.win.show()
    except:
        pass
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()