import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from torrent import Ui_MainWindow
from PyQt5 import QtWidgets
from the_python_bay import tpb

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.buscar)

    def buscar(self):
        # Limpar a tabela antes de adicionar novos resultados
        self.ui.tableWidget.setRowCount(0)

        busca = self.ui.lineEdit.text()
        results = tpb.search(busca)

        # Adicionar linhas à tabela para cada resultado da busca
        for torrent in results:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(torrent.name))
            self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(torrent.magnet))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())