import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.my_input = 0
        self.operand_1 = 0 #первое число
        self.operand_2 = 0 #второе число
    def initUI(self):
        self.setGeometry(300, 300, 350, 370)
        self.setWindowTitle('Calculator')
        self.label = QLabel(self)
        self.label.resize(325, 50)
        self.label.move(0,0)
        self.label.setText('0')
        #Кнопки цифры
        self.num_1 = QPushButton('1', self)
        self.num_1.resize(50, 50)
        self.num_1.move(0, 50)

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(50, 50)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(100, 50)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(0, 100)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(50, 100)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(100, 100)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(0, 150)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(50, 150)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(100, 150)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(0, 200)

        #Кнопки операции
        self.plus = QPushButton('+', self)
        self.plus.resize(100, 50)
        self.plus.move(150, 50)

        self.minus = QPushButton('-', self)
        self.minus.resize(100, 50)
        self.minus.move(150, 100)

        self.mul = QPushButton('*', self)
        self.mul.resize(100, 50)
        self.mul.move(150, 150)

        self.div = QPushButton('/', self)
        self.div.resize(100, 50)
        self.div.move(150, 200)

        self.degree = QPushButton('^', self)
        self.degree.resize(100, 50)
        self.degree.move(250, 50)

        self.sqrt = QPushButton('√', self)
        self.sqrt.resize(100, 50)
        self.sqrt.move(250, 100)

        self.divx2 = QPushButton('//', self)
        self.divx2.resize(100, 50)
        self.divx2.move(250, 150)

        self.remains = QPushButton('%', self)
        self.remains.resize(100, 50)
        self.remains.move(250, 200)

        #Кнопки равно и очистить
        self.ravno = QPushButton('=', self)
        self.ravno.resize(50, 50)
        self.ravno.move(50, 200)

        self.clear = QPushButton('C', self)
        self.clear.resize(50, 50)
        self.clear.move(100, 200)
        #Привязка кнопок к функциям
        self.num_0.clicked.connect(self.zero)
        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.plus.clicked.connect(self.plus_f)
        self.minus.clicked.connect(self.minus_f)
        self.mul.clicked.connect(self.mul_f)
        self.div.clicked.connect(self.div_f)
        self.degree.clicked.connect(self.degree_f)
        self.sqrt.clicked.connect(self.sqrt_f)
        self.divx2.clicked.connect(self.divx2_f)
        self.remains.clicked.connect(self.remains_f)
        self.ravno.clicked.connect(self.ravno_f)
        self.clear.clicked.connect(self.clean_f)
        # Функции кнопок
    def enter_value(self):
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enter_value()

    def two(self):
        self.my_input = '2'
        self.enter_value()

    def three(self):
        self.my_input = '3'
        self.enter_value()

    def four(self):
        self.my_input = '4'
        self.enter_value()

    def five(self):
        self.my_input = '5'
        self.enter_value()

    def six(self):
        self.my_input = '6'
        self.enter_value()

    def seven(self):
        self.my_input = '7'
        self.enter_value()

    def eight(self):
        self.my_input = '8'
        self.enter_value()

    def nine(self):
        self.my_input = '9'
        self.enter_value()

    def zero(self):
        self.my_input = '0'
        self.enter_value()

    def plus_f(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def minus_f(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mul_f(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_f(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def degree_f(self):
        self.operation = '^'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def sqrt_f(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def divx2_f(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def remains_f(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def ravno_f(self):
        self.operand_2 = float(self.label.text())
        if self.operation == '+': self.label.setText(str(self.operand_1 + self.operand_2))
        elif self.operation == '-': self.label.setText(str(self.operand_1 - self.operand_2))
        elif self.operation == '*': self.label.setText(str(self.operand_1 * self.operand_2))
        elif self.operation == '^': self.label.setText(str(self.operand_1 ** self.operand_2))
        elif self.operation == '√': self.label.setText(str(self.operand_1 ** 0.5))
        elif self.operation == '//': self.label.setText(str(self.operand_1 // self.operand_2))
        elif self.operation == '%': self.label.setText(str(self.operand_1 % self.operand_2))
        elif self.operation == '/':
            if self.operand_2 == 0: self.label.setText('Деление на ноль!')
            else: self.label.setText(str(self.operand_1 / self.operand_2))

    def clean_f(self):
        self.label.setText('Введите какие-то значения:')



app = QApplication(sys.argv)

my_Calculator = Calculator()
my_Calculator.show()
sys.exit(app.exec())