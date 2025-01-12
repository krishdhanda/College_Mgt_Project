from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"color:000;\n"
"border: none;\n"
"}\n"
"#leftmenu{\n"
"    background-color: rgb(53, 255, 242);\n"
"}\n"
"#mainbody{\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"QPushButton{\n"
"\n"
"padding:10px 5px;\n"
"text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color:#fefeff;\n"
" padding:10px 5px;\n"
" text-align: left;\n"
" border-top-left-radius:20px;\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.mainbody = QtWidgets.QWidget(self.centralwidget)
        self.mainbody.setGeometry(QtCore.QRect(316, 10, 884, 765))
        self.mainbody.setStyleSheet("\n"
"#pushButton_6:hover{\n"
"    background-color: rgb(255, 255, 0);\n"
"}")
        self.mainbody.setObjectName("mainbody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainbody)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.mainbody)
        self.tabWidget.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.tabWidget.setObjectName("tabWidget")
        self.profiletab = QtWidgets.QWidget()
        self.profiletab.setObjectName("profiletab")
        self.frame_8 = QtWidgets.QFrame(self.profiletab)
        self.frame_8.setGeometry(QtCore.QRect(20, 10, 841, 371))
        self.frame_8.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.image = QtWidgets.QFrame(self.frame_8)
        self.image.setGeometry(QtCore.QRect(20, 20, 201, 251))
        self.image.setStyleSheet("position: relative;\n"
"  \n"
"border:1px solid rgb(175, 175, 175);\n"
"\n"
"  border-radius: 20px;\n"
"  box-sizing: border-box;\n"
"  background: #ecf0f3;\n"
"  box-shadow: 14px 14px 20px #cbced1, -14px -14px 20px white;")
        self.image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image.setObjectName("image")
        self.update = QtWidgets.QPushButton(self.frame_8)
        self.update.setGeometry(QtCore.QRect(60, 280, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.update.setFont(font)
        self.update.setStyleSheet("color: rgb(0, 85, 255);")
        self.update.setObjectName("update")
        self.l4 = QtWidgets.QLabel(self.frame_8)
        self.l4.setGeometry(QtCore.QRect(270, 128, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l4.setFont(font)
        self.l4.setObjectName("l4")
        self.l1 = QtWidgets.QLabel(self.frame_8)
        self.l1.setGeometry(QtCore.QRect(270, 16, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.l6 = QtWidgets.QLabel(self.frame_8)
        self.l6.setGeometry(QtCore.QRect(270, 202, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l6.setFont(font)
        self.l6.setObjectName("l6")
        self.l7 = QtWidgets.QLabel(self.frame_8)
        self.l7.setGeometry(QtCore.QRect(270, 242, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l7.setFont(font)
        self.l7.setObjectName("l7")
        self.l2 = QtWidgets.QLabel(self.frame_8)
        self.l2.setGeometry(QtCore.QRect(270, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.l9 = QtWidgets.QLabel(self.frame_8)
        self.l9.setGeometry(QtCore.QRect(270, 320, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l9.setFont(font)
        self.l9.setObjectName("l9")
        self.l5 = QtWidgets.QLabel(self.frame_8)
        self.l5.setGeometry(QtCore.QRect(270, 163, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l5.setFont(font)
        self.l5.setObjectName("l5")
        self.l3 = QtWidgets.QLabel(self.frame_8)
        self.l3.setGeometry(QtCore.QRect(270, 91, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.l8 = QtWidgets.QLabel(self.frame_8)
        self.l8.setGeometry(QtCore.QRect(270, 285, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l8.setFont(font)
        self.l8.setObjectName("l8")
        self.p1 = QtWidgets.QLineEdit(self.frame_8)
        self.p1.setGeometry(QtCore.QRect(530, 50, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p1.setFont(font)
        self.p1.setStyleSheet("")
        self.p1.setText("")
        self.p1.setObjectName("p1")
        self.p3 = QtWidgets.QLineEdit(self.frame_8)
        self.p3.setGeometry(QtCore.QRect(530, 84, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p3.setFont(font)
        self.p3.setStyleSheet("")
        self.p3.setText("")
        self.p3.setObjectName("p3")
        self.p5 = QtWidgets.QLineEdit(self.frame_8)
        self.p5.setGeometry(QtCore.QRect(530, 160, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p5.setFont(font)
        self.p5.setStyleSheet("")
        self.p5.setText("")
        self.p5.setObjectName("p5")
        self.p6 = QtWidgets.QLineEdit(self.frame_8)
        self.p6.setGeometry(QtCore.QRect(530, 200, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p6.setFont(font)
        self.p6.setStyleSheet("")
        self.p6.setText("")
        self.p6.setObjectName("p6")
        self.p4 = QtWidgets.QLineEdit(self.frame_8)
        self.p4.setGeometry(QtCore.QRect(530, 123, 251, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p4.setFont(font)
        self.p4.setStyleSheet("")
        self.p4.setText("")
        self.p4.setObjectName("p4")
        self.p7 = QtWidgets.QLineEdit(self.frame_8)
        self.p7.setGeometry(QtCore.QRect(530, 238, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p7.setFont(font)
        self.p7.setStyleSheet("")
        self.p7.setText("")
        self.p7.setObjectName("p7")
        self.p8 = QtWidgets.QLineEdit(self.frame_8)
        self.p8.setGeometry(QtCore.QRect(530, 277, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p8.setFont(font)
        self.p8.setStyleSheet("")
        self.p8.setText("")
        self.p8.setObjectName("p8")
        self.p9 = QtWidgets.QLineEdit(self.frame_8)
        self.p9.setGeometry(QtCore.QRect(530, 315, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p9.setFont(font)
        self.p9.setStyleSheet("")
        self.p9.setText("")
        self.p9.setObjectName("p9")
        self.p2 = QtWidgets.QLineEdit(self.frame_8)
        self.p2.setGeometry(QtCore.QRect(530, 15, 251, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.p2.setFont(font)
        self.p2.setStyleSheet("")
        self.p2.setText("")
        self.p2.setObjectName("p2")
        self.upcominglecture = QtWidgets.QFrame(self.profiletab)
        self.upcominglecture.setGeometry(QtCore.QRect(10, 420, 261, 181))
        self.upcominglecture.setStyleSheet("position: relative;\n"
"  \n"
"border:1px solid rgb(175, 175, 175);\n"
"\n"
"  border-radius: 20px;\n"
"  box-sizing: border-box;\n"
"  \n"
"background-color: rgb(229, 51, 63);")
        self.upcominglecture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upcominglecture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upcominglecture.setObjectName("upcominglecture")
        self.label_54 = QtWidgets.QLabel(self.upcominglecture)
        self.label_54.setGeometry(QtCore.QRect(10, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("border:none;\n"
"color: rgb(71, 71, 71);")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.upcominglecture)
        self.lineEdit_22.setGeometry(QtCore.QRect(20, 70, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setStyleSheet("border:none;")
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.topic = QtWidgets.QFrame(self.profiletab)
        self.topic.setGeometry(QtCore.QRect(300, 420, 261, 181))
        self.topic.setStyleSheet("position: relative;\n"
"  \n"
"border:1px solid rgb(175, 175, 175);\n"
"\n"
"  border-radius: 20px;\n"
"  box-sizing: border-box;\n"
"  background: #ecf0f3;\n"
"background-color: rgb(35, 134, 255);\n"
"\n"
"")
        self.topic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topic.setObjectName("topic")
        self.label_55 = QtWidgets.QLabel(self.topic)
        self.label_55.setGeometry(QtCore.QRect(20, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("border:none;\n"
"color: rgb(71, 71, 71);")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.topic)
        self.lineEdit_23.setGeometry(QtCore.QRect(20, 70, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setStyleSheet("border:none;")
        self.lineEdit_23.setText("")
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.syllabus = QtWidgets.QFrame(self.profiletab)
        self.syllabus.setGeometry(QtCore.QRect(590, 420, 261, 181))
        self.syllabus.setStyleSheet("position: relative;\n"
"  \n"
"border:1px solid rgb(175, 175, 175);\n"
"\n"
"  border-radius: 20px;\n"
"  box-sizing: border-box;\n"
"  background: #ecf0f3;\n"
"background-color: rgb(252, 255, 79);")
        self.syllabus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.syllabus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.syllabus.setObjectName("syllabus")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.syllabus)
        self.lineEdit_24.setGeometry(QtCore.QRect(20, 70, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setStyleSheet("border:none;")
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_56 = QtWidgets.QLabel(self.syllabus)
        self.label_56.setGeometry(QtCore.QRect(20, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("border:none;\n"
"color: rgb(71, 71, 71);")
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.tabWidget.addTab(self.profiletab, "")
        self.umarkstab = QtWidgets.QWidget()
        self.umarkstab.setObjectName("umarkstab")
        self.frame_2 = QtWidgets.QFrame(self.umarkstab)
        self.frame_2.setGeometry(QtCore.QRect(0, 10, 861, 701))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 411, 681))
        self.groupBox.setStyleSheet("border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 25, 401, 53))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;")
        self.label.setObjectName("label")
        self.l2_2 = QtWidgets.QLabel(self.groupBox)
        self.l2_2.setGeometry(QtCore.QRect(8, 160, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l2_2.setFont(font)
        self.l2_2.setStyleSheet("border:none;")
        self.l2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_2.setObjectName("l2_2")
        self.usection_2 = QtWidgets.QComboBox(self.groupBox)
        self.usection_2.setGeometry(QtCore.QRect(198, 153, 191, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usection_2.setFont(font)
        self.usection_2.setStatusTip("")
        self.usection_2.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.usection_2.setObjectName("usection_2")
        self.usection_2.addItem("")
        self.usection_2.setItemText(0, "")
        self.usection_2.addItem("")
        self.usection_2.setItemText(1, "")
        self.l3_2 = QtWidgets.QLabel(self.groupBox)
        self.l3_2.setGeometry(QtCore.QRect(8, 220, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3_2.setFont(font)
        self.l3_2.setStyleSheet("border:none;")
        self.l3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_2.setObjectName("l3_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(168, 216, 221, 35))
        self.lineEdit.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.l3_3 = QtWidgets.QLabel(self.groupBox)
        self.l3_3.setGeometry(QtCore.QRect(8, 290, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3_3.setFont(font)
        self.l3_3.setStyleSheet("border:none;")
        self.l3_3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_3.setObjectName("l3_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(168, 279, 221, 35))
        self.lineEdit_2.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.l3_4 = QtWidgets.QLabel(self.groupBox)
        self.l3_4.setGeometry(QtCore.QRect(8, 352, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3_4.setFont(font)
        self.l3_4.setStyleSheet("border:none;")
        self.l3_4.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_4.setObjectName("l3_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(168, 344, 221, 35))
        self.lineEdit_3.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.l3_5 = QtWidgets.QLabel(self.groupBox)
        self.l3_5.setGeometry(QtCore.QRect(8, 418, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3_5.setFont(font)
        self.l3_5.setStyleSheet("border:none;")
        self.l3_5.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_5.setObjectName("l3_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(168, 410, 221, 35))
        self.lineEdit_4.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.l3_6 = QtWidgets.QLabel(self.groupBox)
        self.l3_6.setGeometry(QtCore.QRect(8, 484, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3_6.setFont(font)
        self.l3_6.setStyleSheet("border:none;")
        self.l3_6.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_6.setObjectName("l3_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(168, 480, 221, 35))
        self.lineEdit_5.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.usearch_2 = QtWidgets.QPushButton(self.groupBox)
        self.usearch_2.setGeometry(QtCore.QRect(90, 570, 201, 74))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(99)
        self.usearch_2.setFont(font)
        self.usearch_2.setStyleSheet("color: white;\n"
"  margin-top: 20px;\n"
"  background: #1DA1F2;\n"
"  height: 40px;\n"
"  border-radius: 20px;\n"
"  cursor: pointer;\n"
"  font-weight: 900;\n"
"  box-shadow: 6px 6px 6px #cbced1, -6px -6px 6px white;\n"
"  transition: 0.5s;\n"
"text-align:center;\n"
"")
        self.usearch_2.setObjectName("usearch_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 10, 411, 681))
        self.groupBox_2.setStyleSheet("border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(0, 25, 401, 53))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:none;")
        self.label_5.setObjectName("label_5")
        self.l2_6 = QtWidgets.QLabel(self.groupBox_2)
        self.l2_6.setGeometry(QtCore.QRect(8, 160, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l2_6.setFont(font)
        self.l2_6.setStyleSheet("border:none;")
        self.l2_6.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_6.setObjectName("l2_6")
        self.usection_4 = QtWidgets.QComboBox(self.groupBox_2)
        self.usection_4.setGeometry(QtCore.QRect(198, 153, 191, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usection_4.setFont(font)
        self.usection_4.setStatusTip("")
        self.usection_4.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.usection_4.setObjectName("usection_4")
        self.usection_4.addItem("")
        self.usection_4.setItemText(0, "")
        self.usection_4.addItem("")
        self.usection_4.setItemText(1, "")
        self.l3_22 = QtWidgets.QLabel(self.groupBox_2)
        self.l3_22.setGeometry(QtCore.QRect(8, 230, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3_22.setFont(font)
        self.l3_22.setStyleSheet("border:none;")
        self.l3_22.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_22.setObjectName("l3_22")
        self.l3_23 = QtWidgets.QLabel(self.groupBox_2)
        self.l3_23.setGeometry(QtCore.QRect(8, 291, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3_23.setFont(font)
        self.l3_23.setStyleSheet("border:none;")
        self.l3_23.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_23.setObjectName("l3_23")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(168, 279, 221, 35))
        self.lineEdit_19.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.l3_24 = QtWidgets.QLabel(self.groupBox_2)
        self.l3_24.setGeometry(QtCore.QRect(8, 352, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3_24.setFont(font)
        self.l3_24.setStyleSheet("border:none;")
        self.l3_24.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_24.setObjectName("l3_24")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(168, 344, 221, 35))
        self.lineEdit_20.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.l3_25 = QtWidgets.QLabel(self.groupBox_2)
        self.l3_25.setGeometry(QtCore.QRect(8, 418, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3_25.setFont(font)
        self.l3_25.setStyleSheet("border:none;")
        self.l3_25.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_25.setObjectName("l3_25")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_21.setGeometry(QtCore.QRect(168, 410, 221, 35))
        self.lineEdit_21.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.l3_26 = QtWidgets.QLabel(self.groupBox_2)
        self.l3_26.setGeometry(QtCore.QRect(8, 484, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l3_26.setFont(font)
        self.l3_26.setStyleSheet("border:none;")
        self.l3_26.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_26.setObjectName("l3_26")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_25.setGeometry(QtCore.QRect(168, 480, 221, 35))
        self.lineEdit_25.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.usearch_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.usearch_4.setGeometry(QtCore.QRect(10, 580, 171, 74))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(99)
        self.usearch_4.setFont(font)
        self.usearch_4.setStyleSheet("color: white;\n"
"  margin-top: 20px;\n"
"  background: #1DA1F2;\n"
"  height: 40px;\n"
"  border-radius: 20px;\n"
"  cursor: pointer;\n"
"  font-weight: 900;\n"
"  box-shadow: 6px 6px 6px #cbced1, -6px -6px 6px white;\n"
"  transition: 0.5s;\n"
"text-align:center;\n"
"")
        self.usearch_4.setObjectName("usearch_4")
        self.usection_8 = QtWidgets.QComboBox(self.groupBox_2)
        self.usection_8.setGeometry(QtCore.QRect(170, 216, 104, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usection_8.setFont(font)
        self.usection_8.setStatusTip("")
        self.usection_8.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"border:1px solid rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.usection_8.setObjectName("usection_8")
        self.usection_8.addItem("")
        self.usection_8.setItemText(0, "")
        self.usection_8.addItem("")
        self.usection_8.setItemText(1, "")
        self.usearch_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.usearch_5.setGeometry(QtCore.QRect(290, 193, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(99)
        self.usearch_5.setFont(font)
        self.usearch_5.setStyleSheet("color: white;\n"
"  margin-top: 20px;\n"
"  background: #1DA1F2;\n"
"  height: 40px;\n"
"  border-radius: 20px;\n"
"  cursor: pointer;\n"
"  font-weight: 900;\n"
"  box-shadow: 6px 6px 6px #cbced1, -6px -6px 6px white;\n"
"  transition: 0.5s;\n"
"text-align:center;\n"
"")
        self.usearch_5.setObjectName("usearch_5")
        self.usearch_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.usearch_10.setGeometry(QtCore.QRect(200, 580, 201, 74))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(99)
        self.usearch_10.setFont(font)
        self.usearch_10.setStyleSheet("color: white;\n"
"  margin-top: 20px;\n"
"  background: #1DA1F2;\n"
"  height: 40px;\n"
"  border-radius: 20px;\n"
"  cursor: pointer;\n"
"  font-weight: 900;\n"
"  box-shadow: 6px 6px 6px #cbced1, -6px -6px 6px white;\n"
"  transition: 0.5s;\n"
"text-align:center;\n"
"")
        self.usearch_10.setObjectName("usearch_10")
        self.tabWidget.addTab(self.umarkstab, "")
        self.attendancetab = QtWidgets.QWidget()
        self.attendancetab.setMaximumSize(QtCore.QSize(867, 736))
        self.attendancetab.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.attendancetab.setObjectName("attendancetab")
        self.frame_10 = QtWidgets.QFrame(self.attendancetab)
        self.frame_10.setGeometry(QtCore.QRect(190, 20, 441, 681))
        self.frame_10.setStyleSheet("border:1px solid rgb(175, 175, 175);\n"
"  border-radius: 20px;\n"
"   background: #ecf0f3;\n"
"position: relative; \n"
"  border-radius: 20px;\n"
"  box-sizing: border-box;\n"
"  background: #ecf0f3;\n"
"  box-shadow: 14px 14px 20px #cbced1, -14px -14px 20px white;\n"
" ")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_34 = QtWidgets.QLabel(self.frame_10)
        self.label_34.setGeometry(QtCore.QRect(110, 20, 221, 141))
        self.label_34.setStyleSheet(" border-radius: 50%;\n"
"border:none;\n"
" ")
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap("jims_logo.webp"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_10)
        self.label_35.setGeometry(QtCore.QRect(30, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("display: block;\n"
"  width: 100%;\n"
"  padding: 0;\n"
"  border: none;\n"
"  outline: none;\n"
"  box-sizing: border-box;")
        self.label_35.setObjectName("label_35")
        self.subatt_2 = QtWidgets.QPushButton(self.frame_10)
        self.subatt_2.setGeometry(QtCore.QRect(150, 600, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(99)
        self.subatt_2.setFont(font)
        self.subatt_2.setStyleSheet("color: white;\n"
"  \n"
"  background: #1DA1F2;\n"
"  height: 40px;\n"
"  border-radius: 20px;\n"
"  cursor: pointer;\n"
"  font-weight: 900;\n"
"  box-shadow: 6px 6px 6px #cbced1, -6px -6px 6px white;\n"
"  transition: 0.5s;\n"
"text-align:center;\n"
"")
        self.subatt_2.setObjectName("subatt_2")
        self.line_9 = QtWidgets.QFrame(self.frame_10)
        self.line_9.setGeometry(QtCore.QRect(21, 280, 400, 1))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_36 = QtWidgets.QLabel(self.frame_10)
        self.label_36.setGeometry(QtCore.QRect(20, 289, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("border:none;")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame_10)
        self.label_37.setGeometry(QtCore.QRect(165, 289, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("border:none;")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.line_17 = QtWidgets.QFrame(self.frame_10)
        self.line_17.setGeometry(QtCore.QRect(21, 320, 400, 1))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.frame_10)
        self.line_18.setGeometry(QtCore.QRect(21, 360, 400, 1))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.frame_10)
        self.line_19.setGeometry(QtCore.QRect(21, 400, 400, 1))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.frame_10)
        self.line_20.setGeometry(QtCore.QRect(21, 440, 400, 1))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.frame_10)
        self.line_21.setGeometry(QtCore.QRect(21, 480, 400, 1))
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(self.frame_10)
        self.line_22.setGeometry(QtCore.QRect(21, 520, 400, 1))
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(self.frame_10)
        self.line_23.setGeometry(QtCore.QRect(21, 560, 400, 1))
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.label_57 = QtWidgets.QLabel(self.frame_10)
        self.label_57.setGeometry(QtCore.QRect(300, 290, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("border:none;")
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.c2 = QtWidgets.QCheckBox(self.frame_10)
        self.c2.setGeometry(QtCore.QRect(346, 370, 16, 17))
        self.c2.setStyleSheet("border:none;")
        self.c2.setText("")
        self.c2.setObjectName("c2")
        self.c3 = QtWidgets.QCheckBox(self.frame_10)
        self.c3.setGeometry(QtCore.QRect(346, 410, 16, 17))
        self.c3.setStyleSheet("border:none;")
        self.c3.setText("")
        self.c3.setObjectName("c3")
        self.c4 = QtWidgets.QCheckBox(self.frame_10)
        self.c4.setGeometry(QtCore.QRect(346, 450, 16, 17))
        self.c4.setStyleSheet("border:none;")
        self.c4.setText("")
        self.c4.setObjectName("c4")
        self.c5 = QtWidgets.QCheckBox(self.frame_10)
        self.c5.setGeometry(QtCore.QRect(346, 490, 16, 17))
        self.c5.setStyleSheet("border:none;")
        self.c5.setText("")
        self.c5.setObjectName("c5")
        self.c6 = QtWidgets.QCheckBox(self.frame_10)
        self.c6.setGeometry(QtCore.QRect(346, 530, 16, 17))
        self.c6.setStyleSheet("border:none;")
        self.c6.setText("")
        self.c6.setObjectName("c6")
        self.c1 = QtWidgets.QCheckBox(self.frame_10)
        self.c1.setGeometry(QtCore.QRect(346, 330, 16, 17))
        self.c1.setStyleSheet("border:none;")
        self.c1.setText("")
        self.c1.setObjectName("c1")
        self.date = QtWidgets.QLineEdit(self.frame_10)
        self.date.setGeometry(QtCore.QRect(20, 230, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.date.setFont(font)
        self.date.setStyleSheet("  border-radius: 20px;\n"
"  ")
        self.date.setObjectName("date")
        self.l1_2 = QtWidgets.QLineEdit(self.frame_10)
        self.l1_2.setGeometry(QtCore.QRect(32, 330, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l1_2.setFont(font)
        self.l1_2.setStyleSheet("border:none;\n"
"")
        self.l1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_2.setObjectName("l1_2")
        self.l2_3 = QtWidgets.QLineEdit(self.frame_10)
        self.l2_3.setGeometry(QtCore.QRect(32, 370, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l2_3.setFont(font)
        self.l2_3.setStyleSheet("border:none;\n"
"")
        self.l2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_3.setObjectName("l2_3")
        self.l3_7 = QtWidgets.QLineEdit(self.frame_10)
        self.l3_7.setGeometry(QtCore.QRect(32, 410, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l3_7.setFont(font)
        self.l3_7.setStyleSheet("border:none;\n"
"")
        self.l3_7.setAlignment(QtCore.Qt.AlignCenter)
        self.l3_7.setObjectName("l3_7")
        self.l4_2 = QtWidgets.QLineEdit(self.frame_10)
        self.l4_2.setGeometry(QtCore.QRect(32, 450, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l4_2.setFont(font)
        self.l4_2.setStyleSheet("border:none;\n"
"")
        self.l4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l4_2.setObjectName("l4_2")
        self.l5_2 = QtWidgets.QLineEdit(self.frame_10)
        self.l5_2.setGeometry(QtCore.QRect(32, 490, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l5_2.setFont(font)
        self.l5_2.setStyleSheet("border:none;\n"
"")
        self.l5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l5_2.setObjectName("l5_2")
        self.l6_2 = QtWidgets.QLineEdit(self.frame_10)
        self.l6_2.setGeometry(QtCore.QRect(32, 530, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.l6_2.setFont(font)
        self.l6_2.setStyleSheet("border:none;\n"
"")
        self.l6_2.setAlignment(QtCore.Qt.AlignCenter)
        self.l6_2.setObjectName("l6_2")
        self.n3 = QtWidgets.QLineEdit(self.frame_10)
        self.n3.setGeometry(QtCore.QRect(170, 410, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.n3.setFont(font)
        self.n3.setStyleSheet("border:none;\n"
"")
        self.n3.setAlignment(QtCore.Qt.AlignCenter)
        self.n3.setObjectName("n3")
        self.n6 = QtWidgets.QLineEdit(self.frame_10)
        self.n6.setGeometry(QtCore.QRect(170, 530, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.n6.setFont(font)
        self.n6.setStyleSheet("border:none;\n"
"")
        self.n6.setAlignment(QtCore.Qt.AlignCenter)
        self.n6.setObjectName("n6")
        self.n1 = QtWidgets.QLineEdit(self.frame_10)
        self.n1.setGeometry(QtCore.QRect(170, 330, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.n1.setFont(font)
        self.n1.setStyleSheet("border:none;\n"
"")
        self.n1.setAlignment(QtCore.Qt.AlignCenter)
        self.n1.setObjectName("n1")
        self.n2 = QtWidgets.QLineEdit(self.frame_10)
        self.n2.setGeometry(QtCore.QRect(170, 370, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.n2.setFont(font)
        self.n2.setStyleSheet("border:none;\n"
"")
        self.n2.setAlignment(QtCore.Qt.AlignCenter)
        self.n2.setObjectName("n2")
        self.n4 = QtWidgets.QLineEdit(self.frame_10)
        self.n4.setGeometry(QtCore.QRect(170, 450, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.n4.setFont(font)
        self.n4.setStyleSheet("border:none;\n"
"")
        self.n4.setAlignment(QtCore.Qt.AlignCenter)
        self.n4.setObjectName("n4")
        self.n5 = QtWidgets.QLineEdit(self.frame_10)
        self.n5.setGeometry(QtCore.QRect(170, 490, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.n5.setFont(font)
        self.n5.setStyleSheet("border:none;\n"
"")
        self.n5.setAlignment(QtCore.Qt.AlignCenter)
        self.n5.setObjectName("n5")
        self.pushButton = QtWidgets.QPushButton(self.frame_10)
        self.pushButton.setGeometry(QtCore.QRect(270, 230, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(99)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" color: white;\n"
" background: #1DA1F2;\n"
"  height: 40px;\n"
"  cursor: pointer;\n"
"  font-weight: 900;\n"
"  box-shadow: 6px 6px 6px #cbced1, -6px -6px 6px white;\n"
"  transition: 0.5s;\n"
" text-align:center;\n"
"  border-radius: 20px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.attendancetab, "")
        self.resourcetab = QtWidgets.QWidget()
        self.resourcetab.setObjectName("resourcetab")
        self.label_33 = QtWidgets.QLabel(self.resourcetab)
        self.label_33.setGeometry(QtCore.QRect(90, 10, 621, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("position: relative;\n"
"\n"
"border:1px solid rgb(175, 175, 175);\n"
"\n"
"  border-radius: 20px;\n"
"  box-sizing: border-box;\n"
"  background: #ecf0f3;\n"
"  box-shadow: 14px 14px 20px #cbced1, -14px -14px 20px white;")
        self.label_33.setScaledContents(False)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.frame_7 = QtWidgets.QFrame(self.resourcetab)
        self.frame_7.setGeometry(QtCore.QRect(140, 150, 191, 171))
        self.frame_7.setStyleSheet("position: relative;\n"
"  width: 350px;\n"
"  height: 500px;\n"
"border:1px solid rgb(175, 175, 175);\n"
"\n"
"  border-radius: 20px;\n"
"  box-sizing: border-box;\n"
"background-color: rgb(180, 180, 180);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.notes = QtWidgets.QPushButton(self.frame_7)
        self.notes.setGeometry(QtCore.QRect(50, 80, 81, 41))
        self.notes.setStyleSheet("text-align:center;\n"
"color: rgb(255, 0, 0);")
        self.notes.setObjectName("notes")
        self.frame_9 = QtWidgets.QFrame(self.resourcetab)
        self.frame_9.setGeometry(QtCore.QRect(500, 150, 191, 171))
        self.frame_9.setStyleSheet("position: relative;\n"
"  width: 350px;\n"
"  height: 500px;\n"
"border:1px solid rgb(175, 175, 175);\n"
"\n"
"  border-radius: 20px;\n"
"  box-sizing: border-box;\n"
"background-color: rgb(180, 180, 180);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.links = QtWidgets.QPushButton(self.frame_9)
        self.links.setGeometry(QtCore.QRect(60, 80, 81, 41))
        self.links.setStyleSheet("text-align:center;\n"
"color: rgb(255, 0, 0);")
        self.links.setObjectName("links")
        self.tabWidget.addTab(self.resourcetab, "")
        self.feedbacktab = QtWidgets.QWidget()
        self.feedbacktab.setObjectName("feedbacktab")
        self.frame_6 = QtWidgets.QFrame(self.feedbacktab)
        self.frame_6.setGeometry(QtCore.QRect(230, 20, 441, 681))
        self.frame_6.setStyleSheet("\n"
"position: relative;\n"
"  width: 350px;\n"
"  height: 500px;\n"
"border:1px solid rgb(175, 175, 175);\n"
"\n"
"  border-radius: 20px;\n"
"  box-sizing: border-box;\n"
"  background: #ecf0f3;\n"
"  box-shadow: 14px 14px 20px #cbced1, -14px -14px 20px white;\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_39 = QtWidgets.QLabel(self.frame_6)
        self.label_39.setGeometry(QtCore.QRect(110, 20, 221, 141))
        self.label_39.setStyleSheet(" border-radius: 50%;\n"
"border:none;\n"
" ")
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap("jims_logo.webp"))
        self.label_39.setScaledContents(True)
        self.label_39.setObjectName("label_39")
        self.label_41 = QtWidgets.QLabel(self.frame_6)
        self.label_41.setGeometry(QtCore.QRect(30, 260, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("border:none;")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame_6)
        self.label_42.setGeometry(QtCore.QRect(30, 330, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("border:none;")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_6)
        self.label_43.setGeometry(QtCore.QRect(30, 400, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("border:none;")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.frame_6)
        self.label_44.setGeometry(QtCore.QRect(30, 470, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("border:none;")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.frame_6)
        self.label_45.setGeometry(QtCore.QRect(30, 540, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("border:none;")
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.f1 = QtWidgets.QLineEdit(self.frame_6)
        self.f1.setGeometry(QtCore.QRect(244, 260, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.f1.setFont(font)
        self.f1.setAlignment(QtCore.Qt.AlignCenter)
        self.f1.setObjectName("f1")
        self.f2 = QtWidgets.QLineEdit(self.frame_6)
        self.f2.setGeometry(QtCore.QRect(244, 330, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.f2.setFont(font)
        self.f2.setAlignment(QtCore.Qt.AlignCenter)
        self.f2.setObjectName("f2")
        self.f3 = QtWidgets.QLineEdit(self.frame_6)
        self.f3.setGeometry(QtCore.QRect(244, 400, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.f3.setFont(font)
        self.f3.setAlignment(QtCore.Qt.AlignCenter)
        self.f3.setObjectName("f3")
        self.f4 = QtWidgets.QLineEdit(self.frame_6)
        self.f4.setGeometry(QtCore.QRect(244, 469, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.f4.setFont(font)
        self.f4.setAlignment(QtCore.Qt.AlignCenter)
        self.f4.setObjectName("f4")
        self.f5 = QtWidgets.QLineEdit(self.frame_6)
        self.f5.setGeometry(QtCore.QRect(244, 536, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.f5.setFont(font)
        self.f5.setAlignment(QtCore.Qt.AlignCenter)
        self.f5.setObjectName("f5")
        self.tabWidget.addTab(self.feedbacktab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.ltop = QtWidgets.QLabel(self.tab)
        self.ltop.setGeometry(QtCore.QRect(40, 110, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ltop.setFont(font)
        self.ltop.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ltop.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:17px;")
        self.ltop.setAlignment(QtCore.Qt.AlignCenter)
        self.ltop.setObjectName("ltop")
        self.frame_13 = QtWidgets.QFrame(self.tab)
        self.frame_13.setGeometry(QtCore.QRect(10, 180, 341, 121))
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
        self.lhead = QtWidgets.QLabel(self.tab)
        self.lhead.setGeometry(QtCore.QRect(0, 10, 841, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lhead.setFont(font)
        self.lhead.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lhead.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:17px;")
        self.lhead.setAlignment(QtCore.Qt.AlignCenter)
        self.lhead.setObjectName("lhead")
        self.licon = QtWidgets.QLabel(self.tab)
        self.licon.setGeometry(QtCore.QRect(10, 110, 51, 51))
        self.licon.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:17px;")
        self.licon.setText("")
        self.licon.setPixmap(QtGui.QPixmap(":/blueIcon/iconsblue/codepen.svg"))
        self.licon.setScaledContents(False)
        self.licon.setObjectName("licon")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.leftmenu = QtWidgets.QWidget(self.centralwidget)
        self.leftmenu.setGeometry(QtCore.QRect(10, 10, 300, 765))
        self.leftmenu.setMinimumSize(QtCore.QSize(300, 0))
        self.leftmenu.setMaximumSize(QtCore.QSize(300, 16777215))
        self.leftmenu.setObjectName("leftmenu")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.leftmenu)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.leftmenu)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.teachername = QtWidgets.QLabel(self.frame)
        self.teachername.setGeometry(QtCore.QRect(50, 10, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.teachername.setFont(font)
        self.teachername.setObjectName("teachername")
        self.tfeedback = QtWidgets.QPushButton(self.frame)
        self.tfeedback.setGeometry(QtCore.QRect(20, 298, 241, 38))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tfeedback.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/blueIcon/iconsblue/meh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tfeedback.setIcon(icon)
        self.tfeedback.setIconSize(QtCore.QSize(30, 30))
        self.tfeedback.setObjectName("tfeedback")
        self.tumarks = QtWidgets.QPushButton(self.frame)
        self.tumarks.setGeometry(QtCore.QRect(20, 239, 241, 38))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tumarks.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/blueIcon/iconsblue/file-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tumarks.setIcon(icon1)
        self.tumarks.setIconSize(QtCore.QSize(30, 30))
        self.tumarks.setObjectName("tumarks")
        self.thome = QtWidgets.QPushButton(self.frame)
        self.thome.setGeometry(QtCore.QRect(20, 121, 241, 38))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.thome.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/blueIcon/iconsblue/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thome.setIcon(icon2)
        self.thome.setIconSize(QtCore.QSize(30, 30))
        self.thome.setObjectName("thome")
        self.tattendance = QtWidgets.QPushButton(self.frame)
        self.tattendance.setGeometry(QtCore.QRect(20, 180, 241, 38))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tattendance.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/blueIcon/iconsblue/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tattendance.setIcon(icon3)
        self.tattendance.setIconSize(QtCore.QSize(30, 30))
        self.tattendance.setObjectName("tattendance")
        self.tlogout = QtWidgets.QPushButton(self.frame)
        self.tlogout.setGeometry(QtCore.QRect(20, 697, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tlogout.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/blueIcon/iconsblue/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tlogout.setIcon(icon4)
        self.tlogout.setIconSize(QtCore.QSize(30, 30))
        self.tlogout.setObjectName("tlogout")
        self.tresource = QtWidgets.QPushButton(self.frame)
        self.tresource.setGeometry(QtCore.QRect(20, 354, 241, 38))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tresource.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/blueIcon/iconsblue/plus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tresource.setIcon(icon5)
        self.tresource.setIconSize(QtCore.QSize(30, 30))
        self.tresource.setObjectName("tresource")
        self.setting_btn = QtWidgets.QPushButton(self.frame)
        self.setting_btn.setGeometry(QtCore.QRect(20, 410, 241, 38))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.setting_btn.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/blueIcon/iconsblue/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_btn.setIcon(icon6)
        self.setting_btn.setIconSize(QtCore.QSize(30, 30))
        self.setting_btn.setObjectName("setting_btn")
        self.horizontalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ########################################## All Changes #########################################
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.thome.clicked.connect(self.show_home_tab)
        self.tattendance.clicked.connect(self.show_attendancetab_tab)
        self.tumarks.clicked.connect(self.show_umarkstab_tab)
        self.tfeedback.clicked.connect(self.show_feedbacktab_tab)
        self.tresource.clicked.connect(self.show_resourcetab_tab)
        # self.search_2.clicked.connect(self.show_adepartment_tab)
        self.usearch_2.clicked.connect(self.save_marks_details)
        self.tlogout.clicked.connect(self.exit_app)
        self.usection_4.currentIndexChanged.connect(self.fill_name_in_combobox_for_mark_tab)
        self.usearch_5.clicked.connect(self.fill_exam_details_in_textbox_for_examname_selected)
        self.usearch_4.clicked.connect(self.update_marks_details)
        self.usearch_10.clicked.connect(self.delete_marks_details)
        self.date.setText(str(datetime.now()))
        self.subatt_2.clicked.connect(self.mark_attendance)
        self.pushButton.clicked.connect(self.get_details_from_student)
        self.setting_btn.clicked.connect(self.show_setting_tab)
        ####################################################################################

####################################### QMessage-1 ####################################   


    def showMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()  
    
    def showMessageBox(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def show_home_tab (self):
        self.tabWidget.setCurrentIndex(0)
        self.profile()

    def show_attendancetab_tab (self):
        self.tabWidget.setCurrentIndex(2) 
        

    def show_umarkstab_tab (self):
        self.tabWidget.setCurrentIndex(1) 
        self.fill_registration_number_in_combobox_for_mark_tab()
         

    def show_feedbacktab_tab (self):
        self.tabWidget.setCurrentIndex(4)      

    def show_resourcetab_tab (self):
        self.tabWidget.setCurrentIndex(3)   

        ##################################Attendence#########################################
    
    def show_adepartment_tab (self):
        self.astackedWidget.setCurrentIndex(1)
        ####################################################################################

        ##################################Upload Marks#########################################
     
    def show_udepartment_tab (self):
        self.mstackedWidget.setCurrentIndex(1) 

    def show_setting_tab(self):
        self.tabWidget.setCurrentIndex(5)
        ####################################################################################
 
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################

    def get_details_from_student(self):
        try:
                dt=self.date.currentText()
                connection=sqlite3.connect("College_Details.db")
                cursor=connection.cursor()
                cursor.execute("Select * from attendance ORDER BY registration_number ASC ")
                result=cursor.fetchall()
                if result:
                        for stud in result:
                                self.l6_2.setText(str(stud[1]))
                                # self.l5_2.setText(str(stud[1]))
                                # self.l4_2.setText(str(stud[1]))
                                # self.l3_7.setText(str(stud[1]))
                                # self.l2_3.setText(str(stud[1]))
                                # self.l1_2.setText(str(stud[1]))
                                self.n6.setText(str(stud[2]))
                                # self.n2.setText(str(stud[2]))
                                # self.n3.setText(str(stud[2]))
                                # self.n4.setText(str(stud[2]))
                                # self.n5.setText(str(stud[2]))
                                # self.n6.setText(str(stud[2]))
        except sqlite3.Error as e:
                print("Error occured in pofile!"+e)
                self.l86.setText(self.tb34.text())



    def mark_attendance(self):

                
                connection=sqlite3.connect("College_Details.db")
                cursor=connection.cursor()
                # registration_number = self.l1.text()
                # name = self.n1.text()
                # datetime = self.date.text()
                
                # qry="insert into attendance(registration_number,name,date) values(?,?,?)"
                # value=(registration_number,name,datetime)
                # cursor.execute(qry,value)
                # connection.commit()
                
                
                if self.c1.isChecked()==True:
                        qry=" UPDATE attendance SET status = 'Present' WHERE ID = 1"
                        cursor.execute(qry)
                        connection.commit()
                        print("Attendence mark  Successfully!")
                        self.showMessageBox('College Management System','Student attendence Marks Successfully!') 
                else:
                        qry="UPDATE attendance SET status = 'Absent' WHERE ID = 1 "
                        cursor.execute(qry)
                        connection.commit()


    

                if self.c2.isChecked()==True:
                        qry=" UPDATE attendance SET status = 'Present' WHERE ID = 2"
                        cursor.execute(qry)
                        connection.commit()
                        print("Attendence mark  Successfully!")
                        self.showMessageBox('College Management System','Student attendence Marks Successfully!') 
                else:
                        qry="UPDATE attendance SET status = 'Absent' WHERE ID = 2 "
                        cursor.execute(qry)
                        connection.commit()        
                         
                

         
                if self.c3.isChecked()==True:
                        qry=" UPDATE attendance SET status = 'Present' WHERE ID = 3"
                        cursor.execute(qry)
                        connection.commit()
                        print("Attendence mark  Successfully!")
                        self.showMessageBox('College Management System','Student attendence Marks Successfully!') 
                else:
                        qry="UPDATE attendance SET status = 'Absent' WHERE ID = 3 "
                        cursor.execute(qry)
                        connection.commit()



                if self.c4.isChecked()==True:
                        qry=" UPDATE attendance SET status = 'Present' WHERE ID = 4"
                        cursor.execute(qry)
                        connection.commit()
                        print("Attendence mark  Successfully!")
                        self.showMessageBox('College Management System','Student attendence Marks Successfully!') 
                else:
                        qry="UPDATE attendance SET status = 'Absent' WHERE ID = 4 "
                        cursor.execute(qry)
                        connection.commit()


                if self.c5.isChecked()==True:
                        qry=" UPDATE attendance SET status = 'Present' WHERE ID = 5"
                        cursor.execute(qry)
                        connection.commit()
                        print("Attendence mark  Successfully!")
                        self.showMessageBox('College Management System','Student attendence Marks Successfully!') 
                else:
                        qry="UPDATE attendance SET status = 'Absent' WHERE ID = 5 "
                        cursor.execute(qry)
                        connection.commit()



                if self.c6.isChecked()==True:
                        qry=" UPDATE attendance SET status = 'Present' WHERE ID = 6"
                        cursor.execute(qry)
                        connection.commit()
                        print("Attendence mark  Successfully!")
                        self.showMessageBox('College Management System','Student attendence Marks Successfully!') 
                else:
                        qry="UPDATE attendance SET status = 'Absent' WHERE ID = 6 "
                        cursor.execute(qry)
                        connection.commit()





###########################################################################################
###########################################################################################
###########################################################################################
###########################################################################################



    def profile (self):
        try:
                details=self.p1.text()
                connection=sqlite3.connect("College_Details.db")
                cursor=connection.cursor()
                cursor.execute("Select * from teacher_info ")
                result=cursor.fetchall()
                if result:
                        for stud in result:
                                self.p2.setText(str(stud[0]))
                                self.p1.setText(str(stud[1]))
                                self.p3.setText(str(stud[2]))
                                self.p4.setText(str(stud[3]))
                                self.p5.setText(str(stud[4]))
                                self.p6.setText(str(stud[5]))
                                self.p7.setText(str(stud[6]))
                                self.p8.setText(str(stud[7]))
                                self.p9.setText(str(stud[8]))
        except sqlite3.Error as e:
                print("Error occured in pofile!"+e)  




################################Enter Marks#################################
    def fill_registration_number_in_combobox_for_mark_tab (self):
        try:
                self.usection_2.clear()
                self.usection_4.clear()
                connection=sqlite3.connect("College_Details.db")
                cursor=connection.cursor()
                cursor.execute("Select * from Student_info ")
                result=cursor.fetchall()
                if result:
                        for stud in result:
                                self.usection_2.addItem(str(stud[1]))
                                self.usection_4.addItem(str(stud[1]))


        except sqlite3.Error as e:
                print("Error occured in fill_reg_no_in_combo!"+e)

       
    def save_marks_details (self):
        try:

                connection=sqlite3.connect("College_Details.db")
                cursor=connection.cursor()
                registration_number = self.usection_2.currentText()
                name = self.lineEdit.text()
                mid_term = self.lineEdit_2.text()
                assingment_1 = self.lineEdit_3.text()
                assingment_2 = self.lineEdit_4.text()
                mack_up = self.lineEdit_5.text() 
                qry="insert into Marks(registration_number,name,mid_term,assingment_1,assingment_2,mack_up) values(?,?,?,?,?,?)"
                value=(registration_number,name,mid_term,assingment_1,assingment_2,mack_up)
                cursor.execute(qry,value)
                connection.commit()
                self.label.setText("Marks saved successfully")
                print("Student Details Added Successfully!")
                self.showMessageBox('College Management System','Student Marks Added Successfully!')                
       
        except sqlite3.Error as e:
                self.label.setText("Error in Save Mark form" + e)



    def fill_name_in_combobox_for_mark_tab (self):
        try:
                self.usection_8.clear()
                registration_number=self.usection_4.currentText()
                connection=sqlite3.connect("College_Details.db")
                cursor=connection.cursor()
                cursor.execute("Select * from Marks where registration_number='"+registration_number+"'")
                result=cursor.fetchall()
                if result:
                        for stud in result:
                                self.usection_8.addItem(str(stud[2]))

        except sqlite3.Error as e:
                print("Error occured in fill_name_in_combo!"+e)         



    def fill_exam_details_in_textbox_for_examname_selected (self):
        try:
                registration_number=self.usection_4.currentText()
                name=self.usection_8.currentText()
                connection=sqlite3.connect("College_Details.db")
                cursor=connection.cursor()
                cursor.execute("Select * from Marks where registration_number='"+registration_number+"'and name='"+name+"'")
                result=cursor.fetchall()
                if result:
                        for stud in result:
                                self.lineEdit_19.setText(str(stud[3]))
                                self.lineEdit_20.setText(str(stud[4]))
                                self.lineEdit_21.setText(str(stud[5]))
                                self.lineEdit_25.setText(str(stud[6]))

        except sqlite3.Error as e:
                print("Error occured in fill_marks_in_textbox!"+e)    


    def update_marks_details (self):
        try:

                connection=sqlite3.connect("College_Details.db")
                cursor=connection.cursor()
                registration_number = self.usection_4.currentText()
                name=self.usection_8.currentText()
                mid_term = self.lineEdit_19.text()
                assingment_1 = self.lineEdit_20.text()
                assingment_2 = self.lineEdit_21.text()
                mack_up = self.lineEdit_25.text() 
                qry="update Marks set mid_term='"+mid_term +"',assingment_1='"+assingment_1+"',assingment_2='"+assingment_2+"',mack_up='"+mack_up+"' where registration_number='"+registration_number+"'and name='"+name+"'"
                cursor.execute(qry)
                connection.commit()
                self.label_5.setText("Marks details modified successfully")
                print("Student Details Added Successfully!")
                self.showMessageBox('College Management System','Student Marks modified Successfully!')                
       
        except sqlite3.Error as e:
                self.label_5.setText("Error in Save Mark form" + e)   

    def delete_marks_details (self):        
        try:
                connection=sqlite3.connect("College_Details.db")
                cursor=connection.cursor()
                registration_number = self.usection_4.currentText()
                name=self.usection_8.currentText() 
                qry="delete from Marks where registration_number='"+registration_number+"'and name='"+name+"'"
                cursor.execute(qry)
                connection.commit()
                self.label_5.setText("Marks delete successfully")
                print("Marks delete Successfully!")
                self.showMessageBox("Delete","Are you sure want to delete this mark details")
                self.showMessageBox('College Management System','Student Marks deleted Successfully!') 
                

        except sqlite3.Error as e:
                self.label_5.setText("Error in delrting Mark details" + e)              
                 

######################### LogOut #################################################
    def exit_app(self):        
        print("You logout") #verification of shortcut press
        self.showMessageBox('College Management System','You have Logged Out Successfully!')
        sys.exit()

######
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.update.setText(_translate("MainWindow", "Update Profile"))
        self.l4.setText(_translate("MainWindow", "D.O.B"))
        self.l1.setText(_translate("MainWindow", "Name"))
        self.l6.setText(_translate("MainWindow", "Joining Year"))
        self.l7.setText(_translate("MainWindow", "Department"))
        self.l2.setText(_translate("MainWindow", "Registration Number"))
        self.l9.setText(_translate("MainWindow", "Contact  Number"))
        self.l5.setText(_translate("MainWindow", "Designation"))
        self.l3.setText(_translate("MainWindow", "Email"))
        self.l8.setText(_translate("MainWindow", "Gender"))
        self.label_54.setText(_translate("MainWindow", "UPCOMING LECTURE"))
        self.lineEdit_22.setText(_translate("MainWindow", "5"))
        self.label_55.setText(_translate("MainWindow", "Topic"))
        self.lineEdit_24.setText(_translate("MainWindow", "2023"))
        self.label_56.setText(_translate("MainWindow", "Year"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profiletab), _translate("MainWindow", "Profile"))
        self.groupBox.setTitle(_translate("MainWindow", "Add Marks Details"))
        self.label.setText(_translate("MainWindow", "Enter Marks"))
        self.l2_2.setText(_translate("MainWindow", "Registration Number"))
        self.l3_2.setText(_translate("MainWindow", "Exam"))
        self.l3_3.setText(_translate("MainWindow", "Mid-Term"))
        self.l3_4.setText(_translate("MainWindow", "Assingment-I"))
        self.l3_5.setText(_translate("MainWindow", "Assingment-II"))
        self.l3_6.setText(_translate("MainWindow", "Mackup Exam"))
        self.usearch_2.setText(_translate("MainWindow", "Save Marks Details"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Edit Marks Details"))
        self.label_5.setText(_translate("MainWindow", "Edit/Delete Marks"))
        self.l2_6.setText(_translate("MainWindow", "Registration Number"))
        self.l3_22.setText(_translate("MainWindow", "Exam"))
        self.l3_23.setText(_translate("MainWindow", "Mid-Term"))
        self.l3_24.setText(_translate("MainWindow", "Assingment-I"))
        self.l3_25.setText(_translate("MainWindow", "Assingment-II"))
        self.l3_26.setText(_translate("MainWindow", "Mackup Exam"))
        self.usearch_4.setText(_translate("MainWindow", "Edit Marks Details"))
        self.usearch_5.setText(_translate("MainWindow", "Get Marks"))
        self.usearch_10.setText(_translate("MainWindow", "Delete Marks Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.umarkstab), _translate("MainWindow", "Upload Marks"))
        self.label_35.setText(_translate("MainWindow", "Date_Time"))
        self.subatt_2.setText(_translate("MainWindow", "Mark"))
        self.label_36.setText(_translate("MainWindow", "Registration No"))
        self.label_37.setText(_translate("MainWindow", "Student Name"))
        self.label_57.setText(_translate("MainWindow", "Attendance"))
        self.l1_2.setText(_translate("MainWindow", "001"))
        self.l2_3.setText(_translate("MainWindow", "002"))
        self.l3_7.setText(_translate("MainWindow", "003"))
        self.l4_2.setText(_translate("MainWindow", "004"))
        self.l5_2.setText(_translate("MainWindow", "005"))
        self.l6_2.setText(_translate("MainWindow", "006"))
        self.n3.setText(_translate("MainWindow", "Aja"))
        self.n6.setText(_translate("MainWindow", "Daman"))
        self.n1.setText(_translate("MainWindow", "Aashutosh"))
        self.n2.setText(_translate("MainWindow", "Abhijeet"))
        self.n4.setText(_translate("MainWindow", "chetna"))
        self.n5.setText(_translate("MainWindow", "Bhumika"))
        self.pushButton.setText(_translate("MainWindow", "Get Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.attendancetab), _translate("MainWindow", "Attendance"))
        self.label_33.setText(_translate("MainWindow", "UPLOAD RESOURCES"))
        self.notes.setText(_translate("MainWindow", "NOTES"))
        self.links.setText(_translate("MainWindow", "LINKS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resourcetab), _translate("MainWindow", "Resource"))
        self.label_41.setText(_translate("MainWindow", "Communication Skills"))
        self.label_42.setText(_translate("MainWindow", "Control on Class"))
        self.label_43.setText(_translate("MainWindow", " Subject Knowledge"))
        self.label_44.setText(_translate("MainWindow", "Dought Clearing"))
        self.label_45.setText(_translate("MainWindow", "Communication Skills"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.feedbacktab), _translate("MainWindow", "Feedback"))
        self.ltop.setText(_translate("MainWindow", "Your Credentials"))
        self.lp.setText(_translate("MainWindow", "Password: manoj"))
        self.lu.setText(_translate("MainWindow", "Username: manoj@mail.com"))
        self.lhead.setText(_translate("MainWindow", "Settings Section"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "settings"))
        self.teachername.setText(_translate("MainWindow", "Learn Clean"))
        self.tfeedback.setText(_translate("MainWindow", "Feedback"))
        self.tumarks.setText(_translate("MainWindow", "Upload Marks"))
        self.thome.setText(_translate("MainWindow", "Home"))
        self.tattendance.setText(_translate("MainWindow", "Attendance"))
        self.tlogout.setText(_translate("MainWindow", "Logout"))
        self.tresource.setText(_translate("MainWindow", "Resource"))
        self.setting_btn.setText(_translate("MainWindow", "Settings"))

import resource3_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
