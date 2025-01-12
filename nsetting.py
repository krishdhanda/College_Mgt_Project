from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_File(object):
    def setupUi(self, File):
        File.setObjectName("File")
        File.resize(438, 435)
        self.centralwidget = QtWidgets.QWidget(File)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QLabel(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(0, 0, 661, 601))
        self.back.setStyleSheet("background-color:rgb(55,233,200);")
        self.back.setText("")
        self.back.setObjectName("back")
        self.ltop = QtWidgets.QLabel(self.centralwidget)
        self.ltop.setGeometry(QtCore.QRect(50, 110, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ltop.setFont(font)
        self.ltop.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ltop.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"\n"
"\n"
"\n"
"")
        self.ltop.setAlignment(QtCore.Qt.AlignCenter)
        self.ltop.setObjectName("ltop")
        self.lhead = QtWidgets.QLabel(self.centralwidget)
        self.lhead.setGeometry(QtCore.QRect(50, 10, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lhead.setFont(font)
        self.lhead.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lhead.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"\n"
"\n"
"\n"
"")
        self.lhead.setAlignment(QtCore.Qt.AlignCenter)
        self.lhead.setObjectName("lhead")
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        self.frame_13.setGeometry(QtCore.QRect(20, 210, 311, 151))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.lp = QtWidgets.QLabel(self.frame_13)
        self.lp.setGeometry(QtCore.QRect(20, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lp.setFont(font)
        self.lp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lp.setStyleSheet("")
        self.lp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lp.setObjectName("lp")
        self.lu = QtWidgets.QLabel(self.frame_13)
        self.lu.setGeometry(QtCore.QRect(20, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lu.setFont(font)
        self.lu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lu.setStyleSheet("")
        self.lu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lu.setObjectName("lu")
        self.licon = QtWidgets.QLabel(self.centralwidget)
        self.licon.setGeometry(QtCore.QRect(30, 110, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.licon.setFont(font)
        self.licon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.licon.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"\n"
"\n"
"\n"
"")
        self.licon.setText("")
        self.licon.setPixmap(QtGui.QPixmap("sett_pic.png"))
        self.licon.setScaledContents(True)
        self.licon.setAlignment(QtCore.Qt.AlignCenter)
        self.licon.setObjectName("licon")
        File.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(File)
        self.statusbar.setObjectName("statusbar")
        File.setStatusBar(self.statusbar)

        self.retranslateUi(File)
        QtCore.QMetaObject.connectSlotsByName(File)

    def retranslateUi(self, File):
        _translate = QtCore.QCoreApplication.translate
        File.setWindowTitle(_translate("File", "MainWindow"))
        self.ltop.setText(_translate("File", "Your Credentials"))
        self.lhead.setText(_translate("File", "Settings Section"))
        self.lp.setText(_translate("File", "Password: 55555"))
        self.lu.setText(_translate("File", "Username: admin@mail.com"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    File = QtWidgets.QMainWindow()
    ui = Ui_File()
    ui.setupUi(File)
    File.show()
    sys.exit(app.exec_())
