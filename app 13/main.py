from PyQt6.QtWidgets import QApplication ,QLabel,QWidget,QGridLayout,QLineEdit,QPushButton \
,QMainWindow,QTableWidget,QTableWidgetItem,QDialog,QVBoxLayout,QComboBox,QToolBar,QStatusBar \
,QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction,QIcon
import sys
import sqlite3
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(600,600)

        #menu bar
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")
        edit_menu = self.menuBar().addMenu("&Edit")

        #actions
        add_student = QAction(QIcon("icons/add.png"),"Add Student",self)
        add_student.triggered.connect(self.insert)
        file_menu.addAction(add_student)

        about_action = QAction("About",self)
        help_menu.addAction(about_action)
        about_action.triggered.connect(self.about)

        search_bar = QAction(QIcon("icons/search.png"),"Search",self)
        search_bar.triggered.connect(self.search)
        edit_menu.addAction(search_bar)


        #Table Creation
        self.table =QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id","Name","Course","Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        #ToolBar Creation
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

        toolbar.addAction(add_student)
        toolbar.addAction(search_bar)

        #status Bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)


        #Detect a Cell
        self.table.cellClicked.connect(self.cell_clicked)


    
    def load_data(self):
        conect =sqlite3.connect("database.db")
        result = conect.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for rownum, row_data in enumerate(result):
            self.table.insertRow(rownum)
            for col_num,item in enumerate(row_data):
                self.table.setItem(rownum,col_num,QTableWidgetItem(str(item)))
        
        conect.close()


    def insert(self):
        dialog = InsertDialogue()
        dialog.exec()

    def search(self):
        dialog = SearchBox()
        dialog.exec()

    def cell_clicked(self):
        edit_buton = QPushButton("Edit Records")
        edit_buton.clicked.connect(self.edit)

        delete_buton = QPushButton("Delete Records")
        delete_buton.clicked.connect(self.delete)

        self.statusbar.addWidget(edit_buton)
        self.statusbar.addWidget(delete_buton)

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialogue()
        dialog.exec()

class InsertDialogue(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        course = ["Biology","Chemistry","Maths","Science"]
        self.course_name.addItems(course)
        layout.addWidget(self.course_name)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        conect = sqlite3.connect("database.db")
        cursor = conect.cursor()
        cursor.execute("INSERT INTO students(name,course,mobile) VALUES (?,?,?)",(name,course,mobile))

        conect.commit()
        cursor.close()
        conect.close()

        main_window.load_data()


class SearchBox(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Search Student")
        self.setFixedHeight(300)
        self.setFixedWidth(300)


        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        button = QPushButton("Submit")
        button.clicked.connect(self.search)
        layout.addWidget(button)

        self.setLayout(layout)

    def search(self):
        name = self.student_name.text()
        conect = sqlite3.connect("database.db")
        cursor = conect.cursor()
        result = cursor.execute("SELECT * FROM STUDENTS WHERE name = ?",(name,))
        rows = list(result)
        print(rows)
        items = main_window.table.findItems(name,Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            main_window.table.item(item.row(),1).setSelected(True)

        cursor.close()
        conect.close()


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        #getting details of the student 
        index =main_window.table.currentRow()
        self.id_num = main_window.table.item(index,0).text()
        student_name = main_window.table.item(index,1).text()
        course_name = main_window.table.item(index,2).text()
        mobile = main_window.table.item(index,3).text()

        layout = QVBoxLayout()

        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        course = ["Biology","Chemistry","Maths","Science"]
        self.course_name.addItems(course)
        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)

        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = QPushButton("Update")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        id = self.id_num
        conect = sqlite3.connect("database.db")
        cursor = conect.cursor()
        cursor.execute("UPDATE students SET name = ? ,course = ? ,mobile = ? where id = ?",(name,course,mobile,id))

        conect.commit()
        cursor.close()
        conect.close()

        main_window.load_data()
    


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")


        layout = QGridLayout()
        confirm = QLabel("Are you sure u want to delete")
        yes = QPushButton("yes")
        no = QPushButton("No")

        layout.addWidget(confirm,0,0,1,2)
        layout.addWidget(yes,1,0)
        layout.addWidget(no,1,1)

        self.setLayout(layout)


        yes.clicked.connect(self.delete_student)

    def delete_student(self):
        index = main_window.table.currentRow()
        id_num = main_window.table.item(index,0).text()
        conect = sqlite3.connect("database.db")
        cursor = conect.cursor()
        cursor.execute("DELETE FROM students where id = ?",(id_num,))

        conect.commit()
        cursor.close()
        conect.close()
        main_window.load_data()
        self.close()


        confirm_message = QMessageBox()
        confirm_message.setWindowTitle("Sucess")
        confirm_message.setText("The records deleted")
        confirm_message.exec()
        
class AboutDialogue(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """This app is about student management system"""

        self.setText(content)




app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())