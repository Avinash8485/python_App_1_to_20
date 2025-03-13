from PyQt6.QtWidgets import QApplication ,QLabel,QWidget,QGridLayout,QLineEdit,QPushButton
import sys
from datetime import datetime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Age Calculator")

        grid = QGridLayout()

        name_lable = QLabel("Name : ")
        self.name_line_edit = QLineEdit()

        date_lable = QLabel("Date Of Birth MM/DD/YYYY : ")
        self.date_line_edit = QLineEdit() #by using self male it as instance variable to make it visible inside class from local variable

        cal_button = QPushButton("Calculate Age")
        cal_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")


        grid.addWidget(name_lable, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_lable, 1, 0)
        grid.addWidget(self.date_line_edit, 1, 1)
        grid.addWidget(cal_button,2,0,1,2)
        grid.addWidget(self.output_label,3,0,1,2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth,"%m/%d/%Y").date().year
        age = current_year - year_of_birth
        self.output_label.setText("{self.name_line_edit} is {age} years old")









app = QApplication(sys.argv)
age_cal = AgeCalculator()
age_cal.show()
sys.exit(app.exec())