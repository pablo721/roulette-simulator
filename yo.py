
from PyQt6 import QtWidgets, QtCore, QtGui
from pandasmodel import PandasModel
import pandas as pd
from roulette_simulator import RouletteSimulator


class RouletteSimulatorGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.simulator = RouletteSimulator()
        self.setObjectName("self")
        self.resize(334, 560)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 191, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 311, 491))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setToolTip("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setToolTip("")
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_3.addWidget(self.lineEdit_7, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 5, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_2 = QtGui.QAction(self)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionManual = QtGui.QAction(self)
        self.actionManual.setObjectName("actionManual")
        self.menuHelp.addAction(self.actionAbout_2)
        self.menuHelp.addAction(self.actionManual)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi()
        self.pushButton.clicked.connect(self.run_simulation)
        self.pushButton_2.clicked.connect(self.save_config)

        QtCore.QMetaObject.connectSlotsByName(self)

    def run_simulation(self):
        cash = int(self.lineEdit.text())
        stake = int(self.lineEdit_2.text())
        exit_cash = int(self.lineEdit_5.text())
        numbers = self.comboBox_2.currentText()
        attempts = int(self.lineEdit_6.text())
        multiplier_after_win = float(self.lineEdit_4.text())
        multiplier_after_loss = float(self.lineEdit_7.text())

        summary, logs = self.simulator.run_simulation(cash, stake, exit_cash, numbers, attempts, multiplier_after_win,
                                                      multiplier_after_loss)
        window = QtWidgets.QWidget()
        window.setGeometry(QtCore.QRect(0, 0, 400, 800))
        table = QtWidgets.QTableView(window)
        table.setGeometry(QtCore.QRect(0, 0, 400, 800))
        table.setModel(PandasModel(logs))
        print(summary)

        window.show()

    def save_config(self):
        pass

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Martingale simulator"))
        self.groupBox.setTitle(_translate("MainWindow", "  Roulette martingale simulator"))
        self.label.setText(_translate("MainWindow", "cash"))
        self.lineEdit.setText(_translate("MainWindow", "10000"))
        self.label_2.setText(_translate("MainWindow", "stake"))
        self.lineEdit_2.setText(_translate("MainWindow", "1000"))
        self.label_10.setText(_translate("MainWindow", "exit with"))
        self.lineEdit_5.setText(_translate("MainWindow", "20000"))
        self.label_11.setText(_translate("MainWindow", "attempts"))
        self.lineEdit_6.setText(_translate("MainWindow", "1000"))
        self.groupBox_3.setToolTip(_translate("MainWindow", "Spoiler: It doesn\'t matter on what you bet as return rate is inveresely proportional to win chance and "))
        self.groupBox_3.setTitle(_translate("MainWindow", "bet on"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "red"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "black"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "even"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "odd"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "1-18"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "19-36"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "1-12"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "13-24"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "25-36"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "exact number"))
        self.label_6.setText(_translate("MainWindow", "win chance:"))
        self.label_8.setText(_translate("MainWindow", "%%"))
        self.label_7.setText(_translate("MainWindow", "return ratio:"))
        self.label_9.setText(_translate("MainWindow", "%%%"))
        self.groupBox_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Specify what to do with your bet size after winning and losing a bet.</p><p>Options are: addition, substratction, multiplication (default), division and reset to initial amount.</p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", " stake multipliers (0 = back to initial stake)"))
        self.lineEdit_4.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "after loss"))
        self.lineEdit_7.setText(_translate("MainWindow", "2"))
        self.label_12.setText(_translate("MainWindow", "after win"))
        self.pushButton_2.setText(_translate("MainWindow", "save"))
        self.pushButton.setText(_translate("MainWindow", "start"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = RouletteSimulatorGUI
    MainWindow.show()
    sys.exit(app.exec())
