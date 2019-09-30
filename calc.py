# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui',
# licensing of 'calc.ui' applies.
#
# Created: Sun Sep 29 18:07:53 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 321)
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(16)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtCore.Qt.PointingHandCursor)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Изображения/img_457687.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(210, 40))
        self.lineEdit.setStyleSheet("border: 1px solid rgb(220, 218, 218); \n"
"border-radius: 15px; \n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_AC = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_AC.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_AC.setStyleSheet("QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_AC.setAutoRepeatDelay(294)
        self.pushButton_AC.setObjectName("pushButton_AC")
        self.horizontalLayout_5.addWidget(self.pushButton_AC)
        self.pushButton_grade = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_grade.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_grade.setStyleSheet("QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_grade.setObjectName("pushButton_grade")
        self.horizontalLayout_5.addWidget(self.pushButton_grade)
        self.pushButton_percent = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_percent.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_percent.setStyleSheet("QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.horizontalLayout_5.addWidget(self.pushButton_percent)
        self.pushButton_div = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_div.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_div.setStyleSheet("QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_div.setObjectName("pushButton_div")
        self.horizontalLayout_5.addWidget(self.pushButton_div)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_1.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_1.setStyleSheet("QPushButton::hover{\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.505682, stop:0.596154 rgba(255, 242, 242, 246), stop:1 rgba(209, 209, 209, 210)); \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton:focus { outline: 0 }\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 202, 203);\n"
"}")
        self.pushButton_1.setAutoRepeatDelay(294)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_7.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_2.setStyleSheet("QPushButton::hover{\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.505682, stop:0.596154 rgba(255, 242, 242, 246), stop:1 rgba(209, 209, 209, 210)); \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton:focus { outline: 0 }\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 202, 203);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_3.setStyleSheet("QPushButton::hover{\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.505682, stop:0.596154 rgba(255, 242, 242, 246), stop:1 rgba(209, 209, 209, 210)); \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton:focus { outline: 0 }\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 202, 203);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.pushButton_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_add.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_add.setStyleSheet("QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_7.addWidget(self.pushButton_add)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_4.setStyleSheet("QPushButton::hover{\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.505682, stop:0.596154 rgba(255, 242, 242, 246), stop:1 rgba(209, 209, 209, 210)); \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton:focus { outline: 0 }\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 202, 203);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_5.setStyleSheet("QPushButton::hover{\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.505682, stop:0.596154 rgba(255, 242, 242, 246), stop:1 rgba(209, 209, 209, 210)); \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton:focus { outline: 0 }\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 202, 203);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_6.setStyleSheet("QPushButton::hover{\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.505682, stop:0.596154 rgba(255, 242, 242, 246), stop:1 rgba(209, 209, 209, 210)); \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton:focus { outline: 0 }\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 202, 203);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_minus = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_minus.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_minus.setStyleSheet("QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.horizontalLayout_2.addWidget(self.pushButton_minus)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_7.setStyleSheet("QPushButton::hover{\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.505682, stop:0.596154 rgba(255, 242, 242, 246), stop:1 rgba(209, 209, 209, 210)); \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton:focus { outline: 0 }\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 202, 203);\n"
"}")
        self.pushButton_7.setAutoRepeatDelay(294)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_8.setStyleSheet("QPushButton::hover{\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.505682, stop:0.596154 rgba(255, 242, 242, 246), stop:1 rgba(209, 209, 209, 210)); \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton:focus { outline: 0 }\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 202, 203);\n"
"}")
        self.pushButton_8.setAutoRepeatDelay(294)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_9.setStyleSheet("QPushButton::hover{\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.505682, stop:0.596154 rgba(255, 242, 242, 246), stop:1 rgba(209, 209, 209, 210)); \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton:focus { outline: 0 }\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 202, 203);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_multiplication = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_multiplication.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_multiplication.setStyleSheet("QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_multiplication.setObjectName("pushButton_multiplication")
        self.horizontalLayout_3.addWidget(self.pushButton_multiplication)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setStyleSheet("QPushButton:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_0 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_0.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_0.setStyleSheet("QPushButton::hover{\n"
"    background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.734, fx:0.5, fy:0.505682, stop:0.596154 rgba(255, 242, 242, 246), stop:1 rgba(209, 209, 209, 210)); \n"
"    border-radius: 15px; \n"
"}\n"
"QPushButton:focus { outline: 0 }\n"
"QPushButton{\n"
"    border: 1px solid rgb(220, 218, 218); \n"
"    border-radius: 15px; \n"
"    background-color: rgb(255, 202, 203);\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.horizontalLayout_6.addWidget(self.pushButton_0)
        self.pushButton_factorial = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_factorial.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_factorial.setStyleSheet("QPushButton:hover{\n"
        "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "}\n"
        "QPushButton{\n"
        "    border: 1px solid rgb(220, 218, 218); \n"
        "    border-radius: 15px; \n"
        "    background-color: rgb(255, 255, 255);\n"
        "}\n"
        "")
        self.pushButton_factorial.setObjectName("pushButton_factorial")
        self.horizontalLayout_6.addWidget(self.pushButton_factorial)
        self.pushButton_equally = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_equally.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_equally.setStyleSheet("QPushButton:hover{\n"
        "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "}\n"
        "QPushButton{\n"
        "    border: 1px solid rgb(220, 218, 218); \n"
        "    border-radius: 15px; \n"
        "    background-color: rgb(255, 255, 255);\n"
        "}\n"
        "")
        self.pushButton_equally.setObjectName("pushButton_equally")
        self.horizontalLayout_6.addWidget(self.pushButton_equally)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Калькулятор", None, -1))
        self.pushButton_AC.setText(QtWidgets.QApplication.translate("MainWindow", "AC", None, -1))
        self.pushButton_grade.setText(QtWidgets.QApplication.translate("MainWindow", "^", None, -1))
        self.pushButton_percent.setText(QtWidgets.QApplication.translate("MainWindow", "%", None, -1))
        self.pushButton_div.setText(QtWidgets.QApplication.translate("MainWindow", "/", None, -1))
        self.pushButton_1.setText(QtWidgets.QApplication.translate("MainWindow", "1", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.pushButton_add.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "4", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "5", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "6", None, -1))
        self.pushButton_minus.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("MainWindow", "7", None, -1))
        self.pushButton_8.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.pushButton_9.setText(QtWidgets.QApplication.translate("MainWindow", "9", None, -1))
        self.pushButton_multiplication.setText(QtWidgets.QApplication.translate("MainWindow", "*", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", ".", None, -1))
        self.pushButton_0.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.pushButton_factorial.setText(QtWidgets.QApplication.translate("MainWindow", "!", None, -1))
        self.pushButton_equally.setText(QtWidgets.QApplication.translate("MainWindow", "=", None, -1))


