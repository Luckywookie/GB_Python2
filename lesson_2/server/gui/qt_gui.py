from PyQt5 import QtCore, QtGui, QtWidgets
from .gui_base_tabs import Ui_MainWindow
from models.partners import PartnerModel
from models.payments import PaymentModel
from models.terminals import TerminalModel


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
        current_tab = self.ui.tabWidgetAlls.currentIndex()
        if current_tab == 0:
            tab = self.ui.tableWidgetPartners
            model = PartnerModel.find_all()
        elif current_tab == 1:
            tab = self.ui.tableWidgetTerminals
            model = TerminalModel.find_all()
        elif current_tab == 2:
            tab = self.ui.tableWidgetTransactions
            model = PaymentModel.find_all()
        else:
            tab = None
            model = None
        if n > len(model):
            n = len(model) - 1
        tab.setRowCount(n)
        for i in range(n+1):
            for j in range(len(model[0])):
                row_item = QtWidgets.QTableWidgetItem(str(model[i][j]))
                tab.setItem(i, j, row_item)


