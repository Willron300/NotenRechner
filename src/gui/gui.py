# -*- coding: iso-8859-1 -*-
from PySide.QtCore import *
from PySide.QtGui import *


class MainWindow:
    def __init__(self, app):
        self.app = app
        self.win = QWidget()
        self.window()
        self.win.setWindowTitle("Notentabelle")

    def window(self):
        """
        Generates all layouts
        :return:
        """
        vbox = QVBoxLayout()
        grid_top = self.frame_top()
        grid_one = self.frame_one()
        grid_two = self.frame_two()
        grid_three = self.frame_three()
        grid_four = self.frame_four()
        grid_five = self.frame_five()
        grid_six = self.frame_six()
        grid_start = self.frame_start()


        vbox.addLayout(grid_top)
        vbox.addSpacing(10)
        vbox.addLayout(grid_one)
        vbox.addSpacing(10)
        vbox.addLayout(grid_two)
        vbox.addSpacing(10)
        vbox.addLayout(grid_three)
        vbox.addSpacing(10)
        vbox.addLayout(grid_four)
        vbox.addSpacing(10)
        vbox.addLayout(grid_five)
        vbox.addSpacing(10)
        vbox.addLayout(grid_six)
        vbox.addSpacing(10)
        vbox.addLayout(grid_start)
        vbox.addStretch()
        self.win.setLayout(vbox)
    def frame_top(self):
        """
        Creates the frame to select the SOP date
        :return:
        """
        grid = QGridLayout()
        label_zensuren = QLabel('Zensuren:')
        label_zensuren.setMaximumWidth(60)
        label_pro = QLabel('Prozent:')
        label_von = QLabel('Von:')
        label_von.setMaximumWidth(60)
        label_bis = QLabel('Bis:')
        label_bis.setMaximumWidth(60)
        QIntValidator()        #dynamisch machen ??

        #self.line_sop_jj.setValidator(QIntValidator())
        #self.line_sop_kw.setValidator(QIntValidator(0, 52))

        grid.addWidget(label_zensuren, 0, 0)
        grid.addWidget(label_pro, 0, 1)
        grid.addWidget(label_von, 1, 1)
        grid.addWidget(label_bis, 1, 2)

        return grid
    def frame_one(self):
        grid = QGridLayout()
        label_one = QLabel('1')
        label_one.setMinimumWidth(60)
        line_one_max = QLineEdit('100')
        line_one_max.setMaximumWidth(60)
        line_one_min = QLineEdit('')
        line_one_min.setMaximumWidth(60)
        grid.addWidget(label_one, 0, 0)
        grid.addWidget(line_one_max, 0, 1)
        grid.addWidget(line_one_min, 0, 2)
        return grid
        # line_sop_jj.setMaxLength(2)
    def frame_two(self):
        grid = QGridLayout()
        label_two = QLabel('2')
        label_two.setMinimumWidth(60)
        line_two_max = QLineEdit('')
        line_two_max.setMaximumWidth(60)
        line_two_min = QLineEdit('')
        line_two_min.setMaximumWidth(60)
        grid.addWidget(label_two, 0, 0)
        grid.addWidget(line_two_max, 0, 1)
        grid.addWidget(line_two_min, 0, 2)
        return grid
        # line_sop_jj.setMaxLength(2)
    def frame_three(self):
        grid = QGridLayout()
        label_three = QLabel('3')
        label_three.setMinimumWidth(60)
        line_three_max = QLineEdit('')
        line_three_max.setMaximumWidth(60)
        line_three_min = QLineEdit('')
        line_three_min.setMaximumWidth(60)
        grid.addWidget(label_three, 0, 0)
        grid.addWidget(line_three_max, 0, 1)
        grid.addWidget(line_three_min, 0, 2)
        return grid
        # line_sop_jj.setMaxLength(2)
    def frame_four(self):
        grid = QGridLayout()
        label_four = QLabel('4')
        label_four.setMinimumWidth(60)
        line_four_max = QLineEdit('')
        line_four_max.setMaximumWidth(60)
        line_four_min = QLineEdit('')
        line_four_min.setMaximumWidth(60)
        grid.addWidget(label_four, 0, 0)
        grid.addWidget(line_four_max, 0, 1)
        grid.addWidget(line_four_min, 0, 2)
        return grid
        # line_sop_jj.setMaxLength(2)
    def frame_five(self):
        grid = QGridLayout()
        label_five = QLabel('5')
        label_five.setMinimumWidth(60)
        line_five_max = QLineEdit('49')
        line_five_max.setMaximumWidth(60)
        line_five_min = QLineEdit('25')
        line_five_min.setMaximumWidth(60)
        grid.addWidget(label_five, 0, 0)
        grid.addWidget(line_five_max, 0, 1)
        grid.addWidget(line_five_min, 0, 2)
        return grid
        # line_sop_jj.setMaxLength(2)
    def frame_six(self):
        grid = QGridLayout()
        label_six = QLabel('6')
        label_six.setMinimumWidth(60)
        line_six_max = QLineEdit('24')
        line_six_max.setMaximumWidth(60)
        line_six_min = QLineEdit('0')
        line_six_min.setMaximumWidth(60)
        grid.addWidget(label_six, 0, 0)
        grid.addWidget(line_six_max, 0, 1)
        grid.addWidget(line_six_min, 0, 2)
        return grid
        # line_sop_jj.setMaxLength(2)
    def frame_start(self):
        grid = QGridLayout()
        def start():
            pass
        button_start = QPushButton("Start:")
        button_start.setMaximumSize(120, 30)
        button_start.clicked.connect(lambda: start())

        grid.addWidget(button_start, 0, 0)
        return grid