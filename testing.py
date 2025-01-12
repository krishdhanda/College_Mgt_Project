from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Testing(object):
    def setupUi(self, Testing):
        Testing.setObjectName("Testing")
        Testing.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Testing)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 110, 211, 131))
        self.label.setObjectName("label")
        Testing.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Testing)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Testing.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Testing)
        self.statusbar.setObjectName("statusbar")
        Testing.setStatusBar(self.statusbar)

        self.retranslateUi(Testing)
        QtCore.QMetaObject.connectSlotsByName(Testing)

    def retranslateUi(self, Testing):
        _translate = QtCore.QCoreApplication.translate
        Testing.setWindowTitle(_translate("Testing", "MainWindow"))
        self.label.setText(_translate("Testing", "testing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Testing = QtWidgets.QMainWindow()
    ui = Ui_Testing()
    ui.setupUi(Testing)
    Testing.show()
    sys.exit(app.exec_())
