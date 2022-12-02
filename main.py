#!/usr/bin/env python3
# coding=utf-8

import math
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore


class Main(QDialog):


    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Сложные табличные вычисления в Python')

        self.setWindowIcon(QtGui.QIcon('uis/logo.png'))


        pixmap = QtGui.QPixmap('uis/task8.png')

        rez = QtCore.QSize(597, 75)
        pixmap = pixmap.scaled(rez)

        self.label_img.setPixmap(pixmap)

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.exit)


    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return: pass
        """
        i = 0

        while i < self.tableWidget.rowCount():
            random_num = randint(0, 101)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(random_num)))
            i += 1

    def solve(self):

        if validation_of_data(self.tableWidget):
            i = 0
            j = 1
            multiplication_of_k_i = 1
            factorial = 1

            while i < self.tableWidget.rowCount():
                item = self.tableWidget.item(i, 0).text()
                ki = int(item)
                try:
                    multiplication_of_k_i *= ki
                    a = int(self.TextEditA.toPlainText())
                    b = int(self.TextEditB.toPlainText())
                    first = (math.cos(ki)**2)
                    second = ((a * a) + (b * b)) - math.sin(multiplication_of_k_i)
                    answer = (first/second) ** (1/3)
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(format(answer, ".5f"))))
                    self.label_error.setText('')
                except Exception:
                    self.tableWidget.setItem(i, j, QTableWidgetItem('???'))
                i += 1
        else:
            self.label_error.setText('Введены некорректные данные!')

    def clear(self):
        self.tableWidget.clearContents()

    def exit(self):
        self.close()


def validation_of_data(table_widget):
    """
    проверяем данные на валидность
    :param table_widget: таблица с числами
    :return: True - данные корректны, False - есть некорректные данные
    """
    i = 0
    while i < table_widget.rowCount():
        try:
            float(table_widget.item(i, 0).text())
            i += 1
        except Exception:
            return False

    return True


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
