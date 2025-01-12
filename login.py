from PyQt5 import QtCore, QtGui, QtWidgets
from ui_ui_interface import Ui_MainWindow
from otp import Ui_Dialog
from testing import Ui_Testing
import sqlite3


class Ui_Form(object):
#############################To Connect Menu Window ###########################################    
    def openwin(self):
        self.ui_ui_interfaceWindow=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.ui_ui_interfaceWindow)
        self.ui_ui_interfaceWindow.show()

#############################To Connect Menu Window ###########################################    
    # def openWindow(self):
    #     self.window=QtWidgets.QMainWindow()
    #     self.ui=Ui_Testing()
    #     self.ui.setupUi(self.window)
    #     self.window.show()

#############################To open 3 Menu Window ###########################################
    # def view(self):
    #     user=self.usname.text()

    #     connection=sqlite3.connect("College_Details.db")
    #     c=connection.execute("SELECT Username FROM Login_info WHERE Username = ? ",(user,))
    #     if c.connection=="admin@mail.com":
    #         self.openwin()
        
    #     elif c.connection=='krish@mail.com':
    #         self.openWindow()
        
    #     else:
    #         print("Error!")    
    #     connection.close()     

########################################### To Connect Forgot password Window ##################         
    def openwin_forgot(self):
        self.otpWindow=QtWidgets.QMainWindow()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.otpWindow)
        self.otpWindow.show()
        print("Forgot Password Window Opened Successfully!")

########################################### Login Btn ##########################################
    def loginfunc(self):
        user=self.usname.text()
        password=self.passw.text()

        if len(user)==0 or len(password)==0:
            self.label_2.setText("Please input all fields!")
        
        else:
            connection=sqlite3.connect("College_Details.db")
            result=connection.execute("SELECT * FROM Login_info WHERE Username = ? AND Password = ?",(user,password))
            if(len(result.fetchall())>0):
                print("Successfully Login!")
                self.label_2.setText("")
                self.openwin()
                
            else:
                self.label_2.setText("Invalid username or password")
            connection.close()      

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(412, 546)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setStyleSheet("QPushButton#pushButton{\n"
"background-color:rgb(0,0,209);\n"
"color:rgb(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(0,0,209);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgb(0,0,240);\n"
"}\n"
"")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 390, 530))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 390, 530))
        self.label.setStyleSheet("background-color:rgb(0, 0, 117);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.usname = QtWidgets.QLineEdit(self.widget)
        self.usname.setGeometry(QtCore.QRect(20, 220, 351, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usname.setFont(font)
        self.usname.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"border:1px solid rgb(0,0,0,0);\n"
"border-bottom-color:rgb(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")
        self.usname.setObjectName("usname")
        self.passw = QtWidgets.QLineEdit(self.widget)
        self.passw.setGeometry(QtCore.QRect(20, 310, 351, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.passw.setFont(font)
        self.passw.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"border:1px solid rgb(0,0,0,0);\n"
"border-bottom-color:rgb(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")
        self.passw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passw.setObjectName("passw")
        self.img = QtWidgets.QLabel(self.widget)
        self.img.setGeometry(QtCore.QRect(110, 30, 161, 161))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("logimg2.png"))
        self.img.setScaledContents(True)
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setObjectName("img")
        self.forgotpassw = QtWidgets.QLabel(self.widget)
        self.forgotpassw.setGeometry(QtCore.QRect(30, 450, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.forgotpassw.setFont(font)
        self.forgotpassw.setStyleSheet("color:rgb(255,255,255,150);")
        self.forgotpassw.setObjectName("forgotpassw")
        ####################################################### Test #######,clicked=lambda: self.openWindow()
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(70, 387, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:15px;")
        self.pushButton.setObjectName("pushButton")

        #############################################################################################
        self.pushButton.clicked.connect(self.loginfunc)
        #self.pushButton.clicked.connect(Form.close)
        #############################################################################################

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 344, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 0, 4);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.forgotbtn = QtWidgets.QPushButton(self.widget)
        self.forgotbtn.setGeometry(QtCore.QRect(280, 460, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.forgotbtn.setFont(font)
        self.forgotbtn.setStyleSheet("QPushButton{\n"
"    background-color:rgb(0, 0, 117);\n"
"    color:rgb(255,255,255,150);\n"
"    border: 2px solid rgb(0, 0, 117);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color:rgb(255, 89, 92)\n"
"}\n"
"")
        self.forgotbtn.setObjectName("forgotbtn")
        #############################################################################################
        self.forgotbtn.clicked.connect(self.openwin_forgot)
        #############################################################################################

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.usname.setPlaceholderText(_translate("Form", "  User Name"))
        self.passw.setPlaceholderText(_translate("Form", "  Password"))
        self.forgotpassw.setText(_translate("Form", "Forgot your User Name or Password?"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.forgotbtn.setText(_translate("Form", "click here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

#connection=sqlite3.connect("College_Details.db")
#connection.execute("SELECT Username FROM Login_info WHERE Username = ? ",(user,))



####################################### Changes ####################################
#        self.tabWidget.setCurrentIndex(0)
#####################################################################################
