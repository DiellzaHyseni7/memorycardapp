from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QRadioButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Memory Card')
Question = QLabel('Which nationality does not exist?')
btn_answer1 = QRadioButton('Enets')
btn_answer2 = QRadioButton('Smurfs')
btn_answer3 = QRadioButton('Chulyms')
btn_answer4 = QRadioButton('Aleuts')


layout_main = QVBoxLayout()
layout_main.addWidget(Question, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer4, alignment = Qt.AlignCenter)
#function that generates and displays a number
my_win.setLayout(layout_main)
my_win.show()
app.exec_()







