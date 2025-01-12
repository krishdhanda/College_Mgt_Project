from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    ####################################### Check() ####################################################
    def check(self):
        user=self.oldusname.text()
        
        connection=sqlite3.connect("College_Details.db")
        result=connection.execute("SELECT * FROM Login_info WHERE Username = ? ",(user,))
        if(len(result.fetchall())>0):
            self.cnlabel.setText("User Name Found!")
            print("User Found !")
            self.confirmpass()
        
        elif len(user)==0:
            self.wnlabel.setText("Input all fields!")
            
        else:
            self.wnlabel.setText("Invalid User Name!")
            print("User not Found !")
        connection.close()

    ####################################### Confirmpass() ####################################################
    def confirmpass(self):
        passw=self.conpass.text()
        newpassw=self.newpass.text()
        conpassw=self.conpass.text()

        if len(passw) == 0 :
            self.wplabel.setText("Please Confirm Password!")
        
        elif newpassw != conpassw :
            self.wplabel.setText("Wrong Password!")
        
        else:
            self.changepass()

    ####################################### Chnagepass() ####################################################
    def changepass(self):
        print("User can change password!")
        password=self.newpass.text()
        user=self.oldusname.text()

        connection=sqlite3.connect("College_Details.db")
        #result=connection.execute("UPDATE Login_info SET Password = ? WHERE Username = ? ;",(password,user))
        
        try:
            connection.execute("UPDATE Login_info SET Password = ? WHERE Username = ? ;",(password,user))
            connection.commit()
            print("Record Updated Succesfully!")
        except:
            print("error!")
            connection.rollback()
        connection.close()

               
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(408, 685)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 392, 671))
        self.label.setStyleSheet("background-color:rgb(0, 0, 117);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.img = QtWidgets.QLabel(Dialog)
        self.img.setGeometry(QtCore.QRect(140, 120, 131, 131))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("otp.png"))
        self.img.setScaledContents(False)
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setObjectName("img")
        self.heading = QtWidgets.QLabel(Dialog)
        self.heading.setGeometry(QtCore.QRect(80, 20, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setStyleSheet("color:rgb(255, 255, 255);")
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.oldusname = QtWidgets.QLineEdit(Dialog)
        self.oldusname.setGeometry(QtCore.QRect(50, 290, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.oldusname.setFont(font)
        self.oldusname.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"border:1px solid rgb(0,0,0,0);\n"
"border-bottom-color:rgb(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")
        self.oldusname.setText("")
        self.oldusname.setObjectName("oldusname")
        self.newpass = QtWidgets.QLineEdit(Dialog)
        self.newpass.setGeometry(QtCore.QRect(50, 390, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.newpass.setFont(font)
        self.newpass.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"border:1px solid rgb(0,0,0,0);\n"
"border-bottom-color:rgb(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")
        self.newpass.setText("")
        self.newpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpass.setObjectName("newpass")
        self.conpass = QtWidgets.QLineEdit(Dialog)
        self.conpass.setGeometry(QtCore.QRect(50, 480, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.conpass.setFont(font)
        self.conpass.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"border:1px solid rgb(0,0,0,0);\n"
"border-bottom-color:rgb(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")
        self.conpass.setText("")
        self.conpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conpass.setObjectName("conpass")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 580, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        #############################################################################################
        self.pushButton.clicked.connect(self.check)
        self.wnlabel = QtWidgets.QLabel(Dialog)
        self.wnlabel.setGeometry(QtCore.QRect(50, 350, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wnlabel.setFont(font)
        self.wnlabel.setStyleSheet("color:rgb(255, 0, 4);")
        self.wnlabel.setText("")
        self.wnlabel.setObjectName("wnlabel")
        self.cnlabel = QtWidgets.QLabel(Dialog)
        self.cnlabel.setGeometry(QtCore.QRect(50, 350, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cnlabel.setFont(font)
        self.cnlabel.setStyleSheet("color:rgb(0, 255, 0);")
        self.cnlabel.setText("")
        self.cnlabel.setObjectName("cnlabel")
        self.wplabel = QtWidgets.QLabel(Dialog)
        self.wplabel.setGeometry(QtCore.QRect(50, 530, 215, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wplabel.setFont(font)
        self.wplabel.setStyleSheet("color:rgb(255, 0, 4);")
        self.wplabel.setText("")
        self.wplabel.setObjectName("wplabel")
        self.cplabel = QtWidgets.QLabel(Dialog)
        self.cplabel.setGeometry(QtCore.QRect(50, 530, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cplabel.setFont(font)
        self.cplabel.setStyleSheet("color:rgb(0, 255, 0);")
        self.cplabel.setText("")
        self.cplabel.setObjectName("cplabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.heading.setText(_translate("Dialog", "Reset Password"))
        self.oldusname.setPlaceholderText(_translate("Dialog", "Old User Name!"))
        self.newpass.setPlaceholderText(_translate("Dialog", "New Password!"))
        self.conpass.setPlaceholderText(_translate("Dialog", "Confirm Password!"))
        self.pushButton.setText(_translate("Dialog", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
