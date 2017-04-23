from db import Base, session
from PyQt5 import QtCore, QtGui, QtWidgets
from .base_tab import Ui_MainWindow
from models.partners import PartnerModel
from models.payments import PaymentModel
from models.terminals import TerminalModel


class MainWinMy(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.viewRowsButton.clicked.connect(lambda: self.fill_sql_table(self.count_rows()))
        self.ui.spinBoxPartners.valueChanged.connect(lambda: self.count_rows())
        self.ui.pushButtonAddPartner.clicked.connect(lambda: self.add_partner())
        self.ui.pushButtonAddTerminal.clicked.connect(lambda: self.add_terminal())
        self.ui.tableWidgetPartners.itemDoubleClicked.connect(lambda item: self.view_change(item))
        # self.ui.tableWidgetPartners.itemEntered.connect(lambda x, y: self.view_enter(x, y))

    def view_change(self, item):
        row = item.row()
        column = item.column()
        # model = PartnerModel.find_all()
        # print(model[row][column])
        # _id, title, comment = model[row]
        # PartnerModel.update_partner(_id, title, comment)
        # print(model[row])

    def add_partner(self):
        cell_title = self.ui.lineEditPartnerTitle
        cell_comment = self.ui.lineEditPartnerComment
        title = cell_title.displayText()
        comment = cell_comment.displayText()

        partner = PartnerModel(title=str(title), comment=str(comment))
        partner.save_to_db()
        print('Partner: {}, saved'.format(title))
        cell_title.clear()
        cell_comment.clear()

    def add_terminal(self):
        cell_title = self.ui.lineEditTerminalTitle
        cell_config = self.ui.lineEditTerminalConfig
        title = cell_title.displayText()
        config = cell_config.displayText()

        terminal = TerminalModel(title=str(title), configuration=str(config))
        terminal.save_to_db()
        print('Terminal: {}, saved'.format(title))
        cell_title.clear()
        cell_config.clear()

    def count_rows(self):
        return self.ui.spinBoxPartners.value()

    def fill_sql_table(self, n):
        # focus_cell = self.ui.tableWidgetPartners.currentRow()
        current_tab = self.ui.tabWidgetAlls.currentIndex()
        if current_tab == 0:
            tab = self.ui.tableWidgetPartners
            model = PartnerModel.find_all()
            # print(model)
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
            n = len(model)
        tab.setRowCount(n)
        for i in range(n):
            for j in range(len(model[0])):
                row_item = QtWidgets.QTableWidgetItem(str(model[i][j]))
                tab.setItem(i, j, row_item)


