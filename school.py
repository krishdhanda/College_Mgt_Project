from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector as con
from datetime import date
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog

ui, _ = loadUiType('school.ui')

class MainApp(QMainWindow, ui):

    def __init__(self):

        QMainWindow.__init__(self)

        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0)

        self.tabWidget.tabBar().setVisible(False)

        self.menubar.setVisible(False)

        self.b01.clicked.connect(self.login)

        self.menu11.triggered.connect(self.show_add_new_student_tab)

        self.b12.clicked.connect(self.save_student_details)

        self.menu12.triggered.connect(self.show_edit_or_delete_student_tab)

        self.cb21.currentIndexChanged.connect(self.fill_details_when_combo_box_selected)

        self.b21.clicked.connect(self.edit_student_details)

        self.b22.clicked.connect(self.delete_student_details)

        self.menu21.triggered.connect(self.show_mark_tab)

        self.b31.clicked.connect(self.save_mark_details)

        self.cb32.currentIndexChanged.connect(self.fill_exam_names_in_combobox_for_registration_number_selected)

        self.b32.clicked.connect(self.fill_exam_details_in_textbox_for_examname_selected)

        self.b33.clicked.connect(self.update_mark_details)

        self.b34.clicked.connect(self.delete_mark_details)

        self.menu31.triggered.connect(self.show_attendance_tab)

        self.b41.clicked.connect(self.save_attendance_details)

        self.cb42.currentIndexChanged.connect(self.fill_date_in_combobox_for_reg_no_selected)

        self.b42.clicked.connect(self.fill_attendance_status_on_button_click)

        self.b43.clicked.connect(self.update_attendance_details)

        self.b44.clicked.connect(self.delete_attendance_details)

        self.menu42.triggered.connect(self.show_fees_tab)

        self.b51.clicked.connect(self.save_fees_details)

        self.b81.clicked.connect(self.print_file)

        self.b82.clicked.connect(self.cancel_print)

        self.cb52.currentIndexChanged.connect(self.fill_receipt_details_in_textboxes_for_receipt_combo_selected)

        self.b52.clicked.connect(self.update_fees_details)

        self.b53.clicked.connect(self.delete_fees_details)

        self.menu51.triggered.connect(self.show_report)

        self.menu52.triggered.connect(self.show_report)

        self.menu53.triggered.connect(self.show_report)

        self.menu54.triggered.connect(self.show_report)

        self.menu61.triggered.connect(self.logout)

####### Login form #####

    def login(self):

        un = self.tb01.text()

        pw = self.tb02.text()

        if(un=="admin" and pw=="admin"):

            self.menubar.setVisible(True)

            self.tabWidget.setCurrentIndex(1)

        else:

            QMessageBox.information(self,"School Management system", "Invalid admin login details, Try again !")

            self.l01.setText("Invalid admin login details, Try again !")



    #######  Add new student #########

    def show_add_new_student_tab(self):

        self.tabWidget.setCurrentIndex(2)
        self.fill_next_registration_number()



    def fill_next_registration_number(self):
        
        try:

            rn = 0

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from student")

            result = cursor.fetchall()

            if result:

                for stud in result:
                    rn += 1
                    self.tb11.setText(str(rn+1))

        except con.Error as e:

            print("Error occured in select studen reg number" + e)



    def save_student_details(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            registration_number = self.tb11.text()

            full_name = self.tb12.text()

            gender = self.cb11.currentText()

            date_of_birth = self.tb13.text()

            age = self.tb14.text()

            address = self.mtb11.toPlainText()

            phone = self.tb15.text()

            email = self.tb16.text()

            standard = self.cb12.currentText()

            qry = "insert into student (registration_number,full_name,gender,date_of_birth,age,address,phone,email,standard) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            value = (registration_number,full_name,gender,date_of_birth,age,address,phone,email,standard)

            cursor.execute(qry,value)

            mydb.commit()

            self.l11.setText("Student details saved successfully")

            QMessageBox.information(self, "School management system","Student details added successfully!")

            self.tb11.setText("")

            self.tb12.setText("")

            self.tb13.setText("")

            self.tb14.setText("")

            self.tb15.setText("")

            self.tb16.setText("")

            self.mtb11.setText("")

            self.tabWidget.setCurrentIndex(1)

        except con.Error as e:

            self.l11.setText("Error in save student form " + e)



#######  Edit / Delete student #########



    def show_edit_or_delete_student_tab(self):

        self.tabWidget.setCurrentIndex(3)

        self.fill_registration_number_in_combobox()



    def fill_registration_number_in_combobox(self):
        
        try:

            self.cb21.clear()

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from student")

            result = cursor.fetchall()

            if result:
                for stud in result:
                    self.cb21.addItem(str(stud[1]))

        except con.Error as e:
            
            print("Error occured in fill reg number in combo " + e)



    def fill_details_when_combo_box_selected(self):
        
        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from student where registration_number = '"+ self.cb21.currentText() +"'")

            result = cursor.fetchall()

            if result:

                for stud in result:

                    self.tb21.setText(str(stud[2]))

                    self.tb22.setText(str(stud[3]))

                    self.tb23.setText(str(stud[4]))

                    self.tb24.setText(str(stud[5]))

                    self.mtb21.setText(str(stud[6]))

                    self.tb25.setText(str(stud[7]))

                    self.tb26.setText(str(stud[8]))

                    self.tb27.setText(str(stud[9]))

        except con.Error as e:

            print("Error occured in fill defails when combo selected " + e)



    def edit_student_details(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            registration_number = self.cb21.currentText()

            full_name = self.tb21.text()

            gender = self.tb22.text()

            date_of_birth = self.tb23.text()

            age = self.tb24.text()

            address = self.mtb21.toPlainText()

            phone = self.tb25.text()

            email = self.tb26.text()

            standard = self.tb27.text()

            qry = "update student set full_name = '"+ full_name +"',gender = '"+ gender +"',date_of_birth = '"+ date_of_birth +"',age = '"+ age +"', address = '"+ address +"',phone = '"+ phone +"',email = '"+ email +"',standard = '"+ standard +"'  where registration_number = '"+ registration_number +"'"

            cursor.execute(qry)

            mydb.commit()

            self.l21.setText("Student details modified successfully")

            QMessageBox.information(self, "School management system","Student details modified successfully!")

            self.tb21.setText("")

            self.tb22.setText("")

            self.tb23.setText("")

            self.tb24.setText("")

            self.tb25.setText("")

            self.tb26.setText("")

            self.tb27.setText("")

            self.mtb21.setText("")

            self.tabWidget.setCurrentIndex(1)

        except con.Error as e:

            self.l21.setText("Error in edit student form " + e)



    def delete_student_details(self):
        
        m = QMessageBox.question(self,"Delete","Are you sure want to delete this students details", QMessageBox.Yes|QMessageBox.No)

        if m == QMessageBox.Yes:

            try:

                mydb = con.connect(host="localhost",user="root",password="",db="school")

                cursor = mydb.cursor()

                registration_number = self.cb21.currentText()

                qry = "delete from student where registration_number = '"+ registration_number +"'"

                cursor.execute(qry)

                mydb.commit()

                self.l21.setText("Student details delete_student_details successfully")

                QMessageBox.information(self, "School management system","Student details deleted successfully!")

                self.tabWidget.setCurrentIndex(1)

            except con.Error as e:

                self.l21.setText("Error in delete student form " + e)


##########  Mark Details #############



    def show_mark_tab(self):

        self.tabWidget.setCurrentIndex(4)

        self.fill_registration_number_in_combobox_for_mark_tab()



    def fill_registration_number_in_combobox_for_mark_tab(self):

        try:

            self.cb31.clear()

            self.cb32.clear()

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from student")

            result = cursor.fetchall()

            if result:

                for stud in result:

                    self.cb31.addItem(str(stud[1]))

                    self.cb32.addItem(str(stud[1]))

        except con.Error as e:

            print("Error occured in fill reg number in combo " + e)


    def save_mark_details(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            registration_number = self.cb31.currentText()

            exam_name = self.tb31.text()

            language = self.tb32.text()

            english = self.tb33.text()

            maths = self.tb34.text()

            science = self.tb35.text()

            social = self.tb36.text()

            qry = "insert into mark (registration_number,exam_name,language,english,maths,science,social) values(%s,%s,%s,%s,%s,%s,%s)"

            value = (registration_number,exam_name,language,english,maths,science,social)

            cursor.execute(qry,value)

            mydb.commit()

            self.l31.setText("Mark details saved successfully")

            QMessageBox.information(self, "School management system","Mark details added successfully!")

            self.tb31.setText("")

            self.tb32.setText("")

            self.tb33.setText("")

            self.tb34.setText("")

            self.tb35.setText("")

            self.tb36.setText("")

            self.tabWidget.setCurrentIndex(1)

        except con.Error as e:

            self.l11.setText("Error in save mark form " + e)


    def fill_exam_names_in_combobox_for_registration_number_selected(self):

        try:

            self.cb33.clear()

            registration_number = self.cb32.currentText()

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from mark where registration_number='"+ registration_number +"'")

            result = cursor.fetchall()

            if result:

                for stud in result:

                    self.cb33.addItem(str(stud[2]))

        except con.Error as e:

            print("Error occured in fill exam name in combo " + e)



    def fill_exam_details_in_textbox_for_examname_selected(self):

        try:

            registration_number = self.cb32.currentText()

            exam_name = self.cb33.currentText()

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from mark where registration_number='"+ registration_number +"' and exam_name='"+ exam_name  +"'")

            result = cursor.fetchall()

            if result:

                for stud in result:

                    self.tb37.setText(str(stud[3]))

                    self.tb38.setText(str(stud[4]))

                    self.tb39.setText(str(stud[5]))

                    self.tb310.setText(str(stud[6]))

                    self.tb311.setText(str(stud[7]))

        except con.Error as e:

            print("Error occured in fill mark details in textbox " + e)



    def update_mark_details(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            registration_number = self.cb32.currentText()

            exam_name = self.cb33.currentText()

            language = self.tb37.text()

            english = self.tb38.text()

            maths = self.tb39.text()

            science = self.tb310.text()

            social = self.tb311.text()

            qry = "update mark set language = '"+ language +"',english = '"+ english +"',maths = '"+ maths +"',science = '"+ science +"', social = '"+ social +"'  where registration_number = '"+ registration_number +"' and exam_name = '"+ exam_name +"'"

            cursor.execute(qry)

            mydb.commit()

            self.l32.setText("Mark details modified successfully")

            QMessageBox.information(self, "School management system","Mark details modified successfully!")

            self.tb37.setText("")

            self.tb38.setText("")

            self.tb39.setText("")

            self.tb310.setText("")

            self.tb311.setText("")

            self.tabWidget.setCurrentIndex(1)

        except con.Error as e:

            self.l32.setText("Error in edit student form " + e)




    def delete_mark_details(self):

        m = QMessageBox.question(self,"Delete","Are you sure want to delete this mark details", QMessageBox.Yes|QMessageBox.No)

        if m == QMessageBox.Yes:

            try:

                mydb = con.connect(host="localhost",user="root",password="",db="school")

                cursor = mydb.cursor()

                registration_number = self.cb32.currentText()

                exam_name = self.cb33.currentText()

                qry = "delete from mark where registration_number = '"+ registration_number +"' and exam_name = '"+ exam_name +"'"

                cursor.execute(qry)

                mydb.commit()

                self.l32.setText("Mark details delete_student_details successfully")

                QMessageBox.information(self, "School management system","Mark details deleted successfully!")

                self.tb37.setText("")

                self.tb38.setText("")

                self.tb39.setText("")

                self.tb310.setText("")

                self.tb311.setText("")

                self.tabWidget.setCurrentIndex(1)

            except con.Error as e:

                self.l32.setText("Error in delete mark details form " + e)



####### ATTENDANCE CODING ##########

    def show_attendance_tab(self):

        self.tabWidget.setCurrentIndex(5)

        self.fill_registration_number_in_combobox_for_attendance_tab()

        self.tb41.setText(str(date.today()))



    def fill_registration_number_in_combobox_for_attendance_tab(self):

        try:

            self.cb41.clear()

            self.cb42.clear()

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from student")

            result = cursor.fetchall()

            if result:

                for stud in result:

                    self.cb41.addItem(str(stud[1]))

                    self.cb42.addItem(str(stud[1]))

        except con.Error as e:

            print("Error occured in fill reg number in combo " + e)





    def save_attendance_details(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            registration_number = self.cb41.currentText()

            attendance_date = self.tb41.text()

            morning = self.tb42.text()

            evening = self.tb43.text()

            qry = "insert into attendance (registration_number,attendance_date,morning,evening) values(%s,%s,%s,%s)"

            value = (registration_number,attendance_date,morning,evening)

            cursor.execute(qry,value)

            mydb.commit()

            self.l41.setText("Attendance details saved successfully")

            QMessageBox.information(self, "School management system","Attendance details added successfully!")

            self.tb42.setText("")

            self.tb43.setText("")

        except con.Error as e:

            self.l41.setText("Error in save attendance form " + e)




    def fill_date_in_combobox_for_reg_no_selected(self):

        try:

            self.cb43.clear()

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from attendance where registration_number='"+ self.cb42.currentText() +"'")

            result = cursor.fetchall()

            if result:

                for att in result:

                    self.cb43.addItem(str(att[2]))

        except con.Error as e:

            print("Error occured in fill date in combo " + e)




    def fill_attendance_status_on_button_click(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from attendance where registration_number='"+ self.cb42.currentText() +"' and attendance_date = '"+ self.cb43.currentText() +"'")

            result = cursor.fetchall()

            if result:

                for att in result:

                    self.tb44.setText(str(att[3]))

                    self.tb45.setText(str(att[4]))

        except con.Error as e:

            print("Error occured in fill atteneance status " + e)




    def update_attendance_details(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            registration_number = self.cb42.currentText()

            attendance_date = self.cb43.currentText()

            morning = self.tb44.text()

            evening = self.tb45.text()

            qry = "update attendance set morning = '"+ morning +"',evening = '"+ evening +"' where registration_number = '"+ registration_number +"' and attendance_date = '"+ attendance_date +"'"

            print(qry)

            cursor.execute(qry)

            mydb.commit()

            self.tb44.setText("")

            self.tb45.setText("")

            self.l42.setText("Attendance details modified successfully")

            QMessageBox.information(self, "School management system","Attendance details modified successfully!")

        except con.Error as e:

            self.l42.setText("Error in edit attendance form " + e)





    def delete_attendance_details(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            registration_number = self.cb42.currentText()

            attendance_date = self.cb43.currentText()

            qry = "delete from attendance where registration_number = '"+ registration_number +"' and attendance_date = '"+ attendance_date +"'"

            cursor.execute(qry)

            mydb.commit()

            self.tb44.setText("")

            self.tb45.setText("")

            self.l42.setText("Attendance details deleted successfully")

            QMessageBox.information(self, "School management system","Attendance details deleted successfully!")

            self.tabWidget.setCurrentIndex(1)

        except con.Error as e:

            self.l42.setText("Error in edit attendance form " + e)



####### FEES CODING ##########

    def show_fees_tab(self):

        self.tabWidget.setCurrentIndex(6)

        self.fill_registration_number_in_combobox_for_attendance_tab()

        self.tb41.setText(str(date.today()))

        self.fill_registration_number_in_combobox_for_fees_tab()

        self.fill_next_receipt_number()

        self.tb54.setText(str(date.today()))

        self.fill_receipt_number_in_combobox_for_edit_fees_tab()



    def fill_registration_number_in_combobox_for_fees_tab(self):
        
        try:

            self.cb51.clear()

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from student")

            result = cursor.fetchall()

            if result:

                for stud in result:

                    self.cb51.addItem(str(stud[1]))

        except con.Error as e:

            print("Error occured in fill reg number in combo " + e)




    def fill_next_receipt_number(self):

        try:

            rn=0

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from fees")

            result = cursor.fetchall()

            if result:

                for rec in result:

                    rn += 1

                    self.tb51.setText(str(rn+1))

        except con.Error as e:

            print("Error occured in fill reg number in combo " + e)



    def save_fees_details(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            receipt_number = self.tb51.text()

            registration_number = self.cb51.currentText()

            reason = self.tb52.text()

            amount = self.tb53.text()

            fees_date = self.tb54.text()

            qry = "insert into fees (receipt_number,registration_number,reason,amount,fees_date) values(%s,%s,%s,%s,%s)"

            value = (receipt_number, registration_number,reason,amount,fees_date)

            cursor.execute(qry,value)

            mydb.commit()

            self.l51.setText("Fees details saved successfully")

            QMessageBox.information(self, "School management system","Fees details added successfully!")

            self.fill_receipt_number_in_combobox_for_edit_fees_tab()

            self.l81.setText(self.tb51.text())

            self.l82.setText(self.tb54.text())

            self.l86.setText(self.tb54.text())

            self.l84.setText(self.tb53.text())

            self.l85.setText(self.tb52.text())

            cursor.execute("select * from student where registration_number='"+ registration_number +"'")

            result = cursor.fetchone()

            if result:

                self.l83.setText(str(result[2]))

                self.tabWidget.setCurrentIndex(8)

                self.tb52.setText("")

                self.tb53.setText("")

                self.fill_next_receipt_number()

        except con.Error as e:

            self.l51.setText("Error in save fees form " + e)



    def fill_receipt_number_in_combobox_for_edit_fees_tab(self):

        try:

            self.cb52.clear()

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from fees")

            result = cursor.fetchall()

            if result:

                for rec in result:

                    self.cb52.addItem(str(rec[1]))

        except con.Error as e:

            print("Error occured in fill receipt number in combo " + e)





    def fill_receipt_details_in_textboxes_for_receipt_combo_selected(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            cursor.execute("select * from fees where receipt_number='"+ self.cb52.currentText() +"'")

            result = cursor.fetchall()

            if result:

                for rec in result:

                    self.tb55.setText(str(rec[2]))

                    self.tb56.setText(str(rec[3]))

                    self.tb57.setText(str(rec[4]))

                    self.tb58.setText(str(rec[5]))

        except con.Error as e:

            print("Error occured in fill receipt details in textboxes " + e)




    def update_fees_details(self):

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            receipt_number = self.cb52.currentText()

            registration_number = self.tb55.text()

            reason = self.tb56.text()

            amount = self.tb57.text()

            fees_date = self.tb58.text()

            qry = "update fees set registration_number = '"+ registration_number +"',reason = '"+ reason +"' ,amount = '"+ amount +"',fees_date = '"+ fees_date +"' where receipt_number = '"+ receipt_number +"' "

            print(qry)

            cursor.execute(qry)

            mydb.commit()

            self.l52.setText("Fees details modified successfully")

            QMessageBox.information(self, "School management system","Fees details modified successfully!")



            self.l81.setText(self.cb52.currentText())

            self.l82.setText(self.tb58.text())

            self.l86.setText(self.tb58.text())

            self.l84.setText(self.tb57.text())

            self.l85.setText(self.tb56.text())

            cursor.execute("select * from student where registration_number='"+ registration_number +"'")

            result = cursor.fetchone()

            if result:

                self.l83.setText(str(result[2]))

                self.tabWidget.setCurrentIndex(8)

                self.tb55.setText("")

                self.tb56.setText("")

                self.tb57.setText("")

                self.tb58.setText("")

        except con.Error as e:

            self.l42.setText("Error in edit fees form " + e)




    def delete_fees_details(self):  

        try:

            mydb = con.connect(host="localhost",user="root",password="",db="school")

            cursor = mydb.cursor()

            receipt_number = self.cb52.currentText()

            qry = "delete from fees where receipt_number = '"+ receipt_number +"' "

            print(qry)

            cursor.execute(qry)

            mydb.commit()

            self.l52.setText("Fees details deleted successfully")

            QMessageBox.information(self, "School management system","Fees details deleted successfully!")

            self.tb55.setText("")

            self.tb56.setText("")

            self.tb57.setText("")

            self.tb58.setText("")

            self.tabWidget.setCurrentIndex(1)

        except con.Error as e:

            self.l42.setText("Error in delete fees form " + e)



######### REPORT FORM ###########

    def show_report(self):

        table_name = self.sender()

        self.l61.setText(table_name.text())

        self.tabWidget.setCurrentIndex(7)

        try:

            self.tableReport.setRowCount(0)

            print(table_name.text())

            if(table_name.text()=="Student Reports"):

                mydb = con.connect(host="localhost",user="root",password="",db="school")

                cursor = mydb.cursor()

                qry = "select registration_number,full_name,gender,date_of_birth,age,address,phone,email,standard from student"

                cursor.execute(qry)

                result = cursor.fetchall()

                r = 0

                c = 0

                for row_number, row_data in enumerate(result):

                    r += 1
                    c = 0

                    for row_number, data in enumerate(row_data):

                        c += 1

                        self.tableReport.clear()

                        self.tableReport.setColumnCount(c)

                        for row_number, row_data in enumerate(result):

                            self.tableReport.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.tableReport.setItem(row_number, column_number,QTableWidgetItem(str(data)))
                                self.tableReport.setHorizontalHeaderLabels(['Register Number','Name','Gender','Date of birth','Age','Address','Phone','Email','Standard'])
                            if(table_name.text()=="Mark Reports"):
                                mydb = con.connect(host="localhost",user="root",password="",db="school")
                                cursor = mydb.cursor()
                                qry = "select registration_number,exam_name,language,english,maths,science,social from mark"
                                cursor.execute(qry)
                                result = cursor.fetchall()
                                r = 0

                                c = 0

                                for row_number, row_data in enumerate(result):

                                    r += 1

                                    c = 0

                                for row_number, data in enumerate(row_data):

                                    c += 1

                                    self.tableReport.clear()

                                    self.tableReport.setColumnCount(c)

                                    for row_number, row_data in enumerate(result):

                                        self.tableReport.insertRow(row_number)

                                        for column_number, data in enumerate(row_data):

                                            self.tableReport.setItem(row_number, column_number,QTableWidgetItem(str(data)))

                                            self.tableReport.setHorizontalHeaderLabels(['Register Number','Exam Name','Language','English','Maths','Science','Social'])

                                            if(table_name.text()=="Attendance Reports"):

                                                mydb = con.connect(host="localhost",user="root",password="",db="school")

                                                cursor = mydb.cursor()

                                                qry = "select registration_number,attendance_date,morning,evening from attendance"

                                                cursor.execute(qry)

                                                result = cursor.fetchall()

                                                r = 0

                                                c = 0

                                                for row_number, row_data in enumerate(result):

                                                    r += 1

                                                    c = 0

                                                    for row_number, data in enumerate(row_data):

                                                        c += 1

                                                        self.tableReport.clear()

                                                        self.tableReport.setColumnCount(c)

                                                        for row_number, row_data in enumerate(result):

                                                            self.tableReport.insertRow(row_number)

                                                            for column_number, data in enumerate(row_data):

                                                                self.tableReport.setItem(row_number, column_number,QTableWidgetItem(str(data)))

                                                                self.tableReport.setHorizontalHeaderLabels(['Register Number','Attendance Date','Morning','Evening'])

                                                            if(table_name.text()=="Fees Reports"):

                                                                mydb = con.connect(host="localhost",user="root",password="",db="school")

                                                                cursor = mydb.cursor()

                                                                qry = "select receipt_number,registration_number,reason,amount,fees_date from fees"

                                                                cursor.execute(qry)

                                                                result = cursor.fetchall()

                                                                r = 0

                                                                c = 0

                                                            for row_number, row_data in enumerate(result):

                                                                r += 1

                                                                c = 0

                                                                for row_number, data in enumerate(row_data):

                                                                    c += 1

                                                                    self.tableReport.clear()

                                                                    self.tableReport.setColumnCount(c)

                                                                    for row_number, row_data in enumerate(result):

                                                                        self.tableReport.insertRow(row_number)

                                                                        for column_number, data in enumerate(row_data):

                                                                            self.tableReport.setItem(row_number, column_number,QTableWidgetItem(str(data)))

                                                                            self.tableReport.setHorizontalHeaderLabels(['Receipt Number','Register Number','Reason','Amount','Fees Date'])


        except con.Error as e:

            print("Error in report form " + e)



######### PRINT FUNCTION ###########

    def print_file(self):

        printer = QPrinter(QPrinter.HighResolution)

        dialog = QPrintDialog(printer,self)

        if dialog.exec_() == QPrintDialog.Accepted:

            self.tabWidget.print_(printer)



    def cancel_print(self):

        self.tabWidget.setCurrentIndex(1)




######### LOGOUT FUNCTION ###########

    def logout(self):
        self.menubar.setVisible(False)
        self.tb01.setText("")
        self.tb02.setText("")
        self.tabWidget.setCurrentIndex(0)
        QMessageBox.information(self, "School management system","You are logged out successfully!")



def main():

    app = QApplication(sys.argv)

    window = MainApp()

    window.show()

    app.exec_()
    if __name__ == '__main__':
            
        main()


################################################# My Backups #######################################
    # def show_report_tab(self):
    #     self.tabWidget.setCurrentIndex(4)
    #     table_name = "Student Report"
    #     try:
    #         self.tableReport.setRowCount(0)
    #         print(table_name.text())
    #         if(table_name.text()=="Student Reports"):
    #             connection=sqlite3.connect("College_Details.db")
    #             cursor=connection.cursor()
    #             cursor.execute("Select registration_number,full_name,gender,date_of_birth,age ,address,phone,email,course,semester from Student_info")
    #             result=cursor.fetchall()
    #             r=0
    #             c=0
    #             for row_number,row_data in enumerate(result):
    #                 r+=1
    #                 c=0
    #                 for row_number,data in enumerate(row_data):
    #                     c+=1
    #             self.tableReport.clear()
    #             self.tableReport.setColumnCount(c)
    #             for row_number,row_data in enumerate(result):
    #                 self.tableReport.insertRow(row_number)
    #                 for column_number, data in enumerate(row_data):
    #                     self.tableReport.setItem(row_number, column_number,QTableWidgetItem(str(data)))
    #                     self.tableReport.setHorizontalHeaderLabels(['Register Number','Name','Gender','Date of birth','Address','Phone_No','Email','Course','Semester','Age'])
    #     except sqlite3.Error as e:
    #         print("Error occured in show student report!"+e)
