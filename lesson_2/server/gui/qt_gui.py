from PyQt5 import QtCore, QtGui, QtWidgets
from .gui_test import Ui_MainWindow
from models.partners import PartnerModel


class MainWinMy(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.viewPartnersBtn.clicked.connect(lambda: self.fill_sql_table(self.count_rows()))
        self.ui.spinBoxPartners.valueChanged.connect(lambda: self.count_rows())

    def count_rows(self):
        return self.ui.spinBoxPartners.value()

    def fill_sql_table(self, n):
        all_partners = PartnerModel.find_all()
        if n > len(all_partners):
            n = len(all_partners) - 1
        self.ui.tableWidget.setRowCount(n)
        for i in range(n+1):
            for j in range(2):
                row_item = QtWidgets.QTableWidgetItem(str(all_partners[i][j]))
                self.ui.tableWidget.setItem(i, j, row_item)


