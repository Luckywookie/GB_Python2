import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.qt_gui import MainWinMy


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWinMy()
    main_win.show()
    sys.exit(app.exec_())
