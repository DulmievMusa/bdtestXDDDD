import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
con = sqlite3.connect("coffee.sqlite")

# Создание курсора
cur = con.cursor()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.loadTable('main_table', self.tableWidget)

    def loadTable(self, table_name, table_widget):
        reader = cur.execute(f"""SELECT * FROM {table_name}""").fetchall()
        title = [tup[1] for tup in cur.execute(f"""pragma table_info({table_name})""").fetchall()]
        # title = next(reader)
        table_widget.setColumnCount(len(title))
        table_widget.setHorizontalHeaderLabels(title)
        table_widget.setRowCount(0)
        for i, row in enumerate(reader):
            table_widget.setRowCount(
                table_widget.rowCount() + 1)
            for j, elem in enumerate(row):
                table_widget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def item_changed(self, item):
        pass

    def save_results(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())