from calc import *
import sys


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.equal = ''
        self.res = ''
        self.operation = {'+': self.add, '-': self.minus, '/': self.div, '*': self.multy, '^': self.grade}
        self.action = {'%': self.percent, '!': self.factorial}
        # кнопки
        self.pushButton_0.clicked.connect(self.click_num)  # 0
        self.pushButton_1.clicked.connect(self.click_num)  # 1
        self.pushButton_2.clicked.connect(self.click_num)  # 2
        self.pushButton_3.clicked.connect(self.click_num)  # 3
        self.pushButton_4.clicked.connect(self.click_num)  # 4
        self.pushButton_5.clicked.connect(self.click_num)  # 5
        self.pushButton_6.clicked.connect(self.click_num)  # 6
        self.pushButton_7.clicked.connect(self.click_num)  # 7
        self.pushButton_8.clicked.connect(self.click_num)  # 8
        self.pushButton_9.clicked.connect(self.click_num)  # 9

        # действие с числом
        self.pushButton.clicked.connect(self.click_num)  # .
        self.pushButton_percent.clicked.connect(self.click_num)  # %
        self.pushButton_factorial.clicked.connect(self.click_num)  # !

        # математические операции
        self.pushButton_add.clicked.connect(self.operations_print)  # +
        self.pushButton_minus.clicked.connect(self.operations_print)  # -
        self.pushButton_div.clicked.connect(self.operations_print)  # /
        self.pushButton_multiplication.clicked.connect(self.operations_print)  # *
        self.pushButton_grade.clicked.connect(self.operations_print)  # ^

        # действие
        self.pushButton_AC.clicked.connect(self.clear)  # AC
        self.pushButton_equally.clicked.connect(self.result)  # =

    def click_num(self):
        button = self.sender()
        if self.lineEdit.text() == '' or self.lineEdit.text() == str(self.res):
            # Если поле пустое, то заменяем его на текст, который написан на кнопке
            # Если до этого был выведен результат, то выводим текст на кнопке
            self.lineEdit.setText(button.text())
        else:
            if self.equal == self.lineEdit.text():
                self.lineEdit.setText(button.text())
            else:
                self.lineEdit.setText(self.lineEdit.text() + button.text())

    # Вывод операции
    def operations_print(self):
        button = self.sender()
        if self.equal == "":
            self.equal = button.text()
            last_val = self.lineEdit.text()
            self.lineEdit.clear()
            self.lineEdit.setText(str(last_val) + button.text())
        else:
            first = self.equal
            self.equal = button.text()
            self.operation[first]()

    def clear(self):
        self.lineEdit.clear()

    def result(self):
        if self.lineEdit.text()[-1] in self.action.keys():
            self.action[self.lineEdit.text()[-1]]()
        else:
            first = self.equal
            self.equal = ''
            self.operation[first]()

    def add(self):
        row_res = self.lineEdit.text().split('+')
        self.res = float(row_res[0])
        if row_res[1]:
            self.res += float(row_res[1])
        self.res_type()

    def minus(self):
        row_res = self.lineEdit.text().split('-')
        self.res = float(row_res[0])
        if row_res[1]:
            self.res -= float(row_res[1])
        self.res_type()

    def div(self):
        row_res = self.lineEdit.text().split('/')
        self.res = float(row_res[0])
        if row_res[1]:
            self.res /= float(row_res[1])
        self.res_type()

    def multy(self):
        row_res = self.lineEdit.text().split('*')
        self.res = float(row_res[0])
        if row_res[1]:
            self.res *= float(row_res[1])
        self.res_type()

    def percent(self):
        row_res = self.lineEdit.text().split('%')[0]
        self.res = float(row_res)/100
        self.res_type()

    def factorial(self):
        row_res = self.lineEdit.text().split('!')[0]
        print(row_res)
        f = 1
        for i in range(1, int(row_res)+1):
            f *= i
        self.res = f
        self.res_type()

    def grade(self):
        row_res = self.lineEdit.text().split('^')
        s = float(row_res[0])
        for i in range(1, int(row_res[1])):
            s *= float(row_res[0])
        self.res = s
        self.res_type()

    def res_type(self):
        if float(self.res).is_integer():
            self.res = int(self.res)
            self.lineEdit.setText(str(self.res) + self.equal)
        else:
            self.res = round(float(self.res), 4)
            self.lineEdit.setText(str(self.res) + self.equal)



if __name__ == '__main__':
    # Application
    app = QtWidgets.QApplication(sys.argv)
    calc = Calculator()
    # Запуск
    sys.exit(app.exec_())

