# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Client_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Client(object):
    def setupUi(self, Client):
        Client.setObjectName("Client")
        Client.resize(777, 577)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 72))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 72))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 72))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 72))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 72))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 72))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 72))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 72))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(72, 72, 72))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        Client.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Client.setFont(font)
        Client.setStyleSheet("QWidget{\n"
"background:#484848;\n"
"}\n"
"QAbstractButton{\n"
"border-style:none;\n"
"border-radius:0px;\n"
"padding:5px;\n"
"color:#DCDCDC;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);\n"
"}\n"
"QAbstractButton:hover{\n"
"color:#FFFFFF;\n"
"background-color:#00BB9E;\n"
"}\n"
"QAbstractButton:pressed{\n"
"color:#DCDCDC;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 2px;\n"
"padding:4px 4px 4px 2px;\n"
"border-color:#00BB9E;\n"
"background-color:#444444;\n"
"}\n"
"QLabel{\n"
"color:#DCDCDC;\n"
"border:1px solid #242424;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #484848,stop:1 #383838);\n"
"}\n"
"QLabel:focus{\n"
"border:1px solid #00BB9E;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #646464,stop:1 #525252);\n"
"}\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"border:1px solid #242424;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#484848;\n"
"selection-color:#DCDCDC;\n"
"}\n"
"\n"
"QLineEdit:focus,QLineEdit:hover{\n"
"border:1px solid #242424;\n"
"}\n"
"QLineEdit{\n"
"lineedit-password-character:9679;\n"
"}\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal{\n"
"height:3px;\n"
"border-radius:3px;\n"
"background:#18181a;\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"height:8px;\n"
"border-radius:3px;\n"
"background:#008aff;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:12px;\n"
"margin-top:-5px;\n"
"margin-bottom:-4px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #565656,stop:0.8 #565656);\n"
"}\n"
"\n"
"\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical{\n"
"width:3px;\n"
"border-radius:3px;\n"
"background:#18181a;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:3px;\n"
"background:#008aff;\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical{\n"
"height:12px;\n"
"margin-left:-5px;\n"
"margin-right:-4px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #565656,stop:0.8 #565656);\n"
"}\n"
"")
        self.label_Video = QtWidgets.QLabel(Client)
        self.label_Video.setGeometry(QtCore.QRect(0, 0, 400, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Video.sizePolicy().hasHeightForWidth())
        self.label_Video.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Video.setFont(font)
        self.label_Video.setStyleSheet("font: 10pt \"Arial\";")
        self.label_Video.setText("")
        self.label_Video.setObjectName("label_Video")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(Client)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(20, 310, 751, 261))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.IP = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.IP.setFont(font)
        self.IP.setStyleSheet("font: 10pt \"Arial\";")
        self.IP.setObjectName("IP")
        self.horizontalLayout_3.addWidget(self.IP)
        self.Btn_Connect = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Connect.setFont(font)
        self.Btn_Connect.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Connect.setObjectName("Btn_Connect")
        self.horizontalLayout_3.addWidget(self.Btn_Connect)
        self.Btn_Video = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Video.setFont(font)
        self.Btn_Video.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Video.setObjectName("Btn_Video")
        self.horizontalLayout_3.addWidget(self.Btn_Video)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Btn_Turn_Left = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Turn_Left.setFont(font)
        self.Btn_Turn_Left.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Turn_Left.setObjectName("Btn_Turn_Left")
        self.gridLayout.addWidget(self.Btn_Turn_Left, 2, 0, 1, 1)
        self.Btn_Buzzer = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Buzzer.setFont(font)
        self.Btn_Buzzer.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Buzzer.setObjectName("Btn_Buzzer")
        self.gridLayout.addWidget(self.Btn_Buzzer, 2, 1, 1, 1)
        self.Btn_Turn_Right = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Turn_Right.setFont(font)
        self.Btn_Turn_Right.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Turn_Right.setObjectName("Btn_Turn_Right")
        self.gridLayout.addWidget(self.Btn_Turn_Right, 2, 2, 1, 1)
        self.Btn_Backward = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Backward.setFont(font)
        self.Btn_Backward.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Backward.setObjectName("Btn_Backward")
        self.gridLayout.addWidget(self.Btn_Backward, 3, 1, 1, 1)
        self.Btn_Forward = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Forward.setFont(font)
        self.Btn_Forward.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Forward.setObjectName("Btn_Forward")
        self.gridLayout.addWidget(self.Btn_Forward, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.progress_Power = QtWidgets.QProgressBar(self.horizontalLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_Power.sizePolicy().hasHeightForWidth())
        self.progress_Power.setSizePolicy(sizePolicy)
        self.progress_Power.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.progress_Power.setFont(font)
        self.progress_Power.setStyleSheet("QProgressBar {\n"
"border: 2px solid grey;\n"
"border-radius: 5px;\n"
"background-color: #FFFFFF;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background-color:#696969;\n"
"width: 20px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"text-align: center; \n"
"color: rgb(152,251,152);\n"
"}\n"
"font: 10pt \"Arial\";")
        self.progress_Power.setProperty("value", 0)
        self.progress_Power.setObjectName("progress_Power")
        self.horizontalLayout_7.addWidget(self.progress_Power)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_Tracking_Faces = QtWidgets.QCheckBox(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Tracking_Faces.setFont(font)
        self.checkBox_Tracking_Faces.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Tracking_Faces.setObjectName("checkBox_Tracking_Faces")
        self.verticalLayout_4.addWidget(self.checkBox_Tracking_Faces)
        self.Btn_Mode1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Mode1.setFont(font)
        self.Btn_Mode1.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Mode1.setObjectName("Btn_Mode1")
        self.verticalLayout_4.addWidget(self.Btn_Mode1)
        self.Btn_Mode2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Mode2.setFont(font)
        self.Btn_Mode2.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Mode2.setObjectName("Btn_Mode2")
        self.verticalLayout_4.addWidget(self.Btn_Mode2)
        self.Btn_Mode3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Mode3.setFont(font)
        self.Btn_Mode3.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Mode3.setObjectName("Btn_Mode3")
        self.verticalLayout_4.addWidget(self.Btn_Mode3)
        self.Btn_Mode4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Mode4.setFont(font)
        self.Btn_Mode4.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Mode4.setObjectName("Btn_Mode4")
        self.verticalLayout_4.addWidget(self.Btn_Mode4)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Btn_Left = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Left.setFont(font)
        self.Btn_Left.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Left.setObjectName("Btn_Left")
        self.gridLayout_3.addWidget(self.Btn_Left, 1, 0, 1, 1)
        self.Btn_Up = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Up.setFont(font)
        self.Btn_Up.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Up.setObjectName("Btn_Up")
        self.gridLayout_3.addWidget(self.Btn_Up, 0, 1, 1, 1)
        self.Btn_Right = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Right.setFont(font)
        self.Btn_Right.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Right.setObjectName("Btn_Right")
        self.gridLayout_3.addWidget(self.Btn_Right, 1, 2, 1, 1)
        self.Btn_Down = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Down.setFont(font)
        self.Btn_Down.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Down.setObjectName("Btn_Down")
        self.gridLayout_3.addWidget(self.Btn_Down, 2, 1, 1, 1)
        self.Btn_Home = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Home.setFont(font)
        self.Btn_Home.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Home.setObjectName("Btn_Home")
        self.gridLayout_3.addWidget(self.Btn_Home, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.HSlider_Servo1 = QtWidgets.QSlider(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.HSlider_Servo1.setFont(font)
        self.HSlider_Servo1.setStyleSheet("font: 9pt \"Arial\";")
        self.HSlider_Servo1.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.HSlider_Servo1.setObjectName("HSlider_Servo1")
        self.horizontalLayout_6.addWidget(self.HSlider_Servo1)
        self.label_Servo1 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Servo1.setFont(font)
        self.label_Servo1.setStyleSheet("font: 14pt \"Arial\";")
        self.label_Servo1.setObjectName("label_Servo1")
        self.horizontalLayout_6.addWidget(self.label_Servo1)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.VSlider_Servo2 = QtWidgets.QSlider(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.VSlider_Servo2.setFont(font)
        self.VSlider_Servo2.setStyleSheet("font: 9pt \"Arial\";")
        self.VSlider_Servo2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.VSlider_Servo2.setObjectName("VSlider_Servo2")
        self.verticalLayout_2.addWidget(self.VSlider_Servo2)
        self.label_Servo2 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_Servo2.setFont(font)
        self.label_Servo2.setStyleSheet("font: 14pt \"Arial\";")
        self.label_Servo2.setObjectName("label_Servo2")
        self.verticalLayout_2.addWidget(self.label_Servo2)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Servo1 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Servo1.setFont(font)
        self.Servo1.setStyleSheet("font: 10pt \"Arial\";")
        self.Servo1.setObjectName("Servo1")
        self.horizontalLayout_4.addWidget(self.Servo1)
        self.HSlider_FineServo1 = QtWidgets.QSlider(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.HSlider_FineServo1.setFont(font)
        self.HSlider_FineServo1.setStyleSheet("font: 9pt \"Arial\";")
        self.HSlider_FineServo1.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.HSlider_FineServo1.setObjectName("HSlider_FineServo1")
        self.horizontalLayout_4.addWidget(self.HSlider_FineServo1)
        self.label_FineServo1 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_FineServo1.setFont(font)
        self.label_FineServo1.setStyleSheet("font: 14pt \"Arial\";")
        self.label_FineServo1.setObjectName("label_FineServo1")
        self.horizontalLayout_4.addWidget(self.label_FineServo1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Servo2 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Servo2.setFont(font)
        self.Servo2.setStyleSheet("font: 10pt \"Arial\";")
        self.Servo2.setObjectName("Servo2")
        self.horizontalLayout_5.addWidget(self.Servo2)
        self.HSlider_FineServo2 = QtWidgets.QSlider(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.HSlider_FineServo2.setFont(font)
        self.HSlider_FineServo2.setStyleSheet("font: 9pt \"Arial\";")
        self.HSlider_FineServo2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.HSlider_FineServo2.setObjectName("HSlider_FineServo2")
        self.horizontalLayout_5.addWidget(self.HSlider_FineServo2)
        self.label_FineServo2 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_FineServo2.setFont(font)
        self.label_FineServo2.setStyleSheet("font: 14pt \"Arial\";")
        self.label_FineServo2.setObjectName("label_FineServo2")
        self.horizontalLayout_5.addWidget(self.label_FineServo2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_8.addLayout(self.gridLayout_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(Client)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(420, 30, 339, 249))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Btn_Ultrasonic = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Ultrasonic.setFont(font)
        self.Btn_Ultrasonic.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Ultrasonic.setObjectName("Btn_Ultrasonic")
        self.horizontalLayout_2.addWidget(self.Btn_Ultrasonic)
        self.Btn_Light = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Btn_Light.setFont(font)
        self.Btn_Light.setStyleSheet("font: 10pt \"Arial\";")
        self.Btn_Light.setObjectName("Btn_Light")
        self.horizontalLayout_2.addWidget(self.Btn_Light)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.R = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.R.setFont(font)
        self.R.setStyleSheet("font: 10pt \"Arial\";")
        self.R.setObjectName("R")
        self.horizontalLayout.addWidget(self.R)
        self.Color_R = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Color_R.setFont(font)
        self.Color_R.setStyleSheet("font: 10pt \"Arial\";")
        self.Color_R.setObjectName("Color_R")
        self.horizontalLayout.addWidget(self.Color_R)
        self.G = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.G.setFont(font)
        self.G.setStyleSheet("font: 10pt \"Arial\";")
        self.G.setObjectName("G")
        self.horizontalLayout.addWidget(self.G)
        self.Color_G = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Color_G.setFont(font)
        self.Color_G.setStyleSheet("font: 10pt \"Arial\";")
        self.Color_G.setObjectName("Color_G")
        self.horizontalLayout.addWidget(self.Color_G)
        self.B = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.B.setFont(font)
        self.B.setStyleSheet("font: 10pt \"Arial\";")
        self.B.setObjectName("B")
        self.horizontalLayout.addWidget(self.B)
        self.Color_B = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Color_B.setFont(font)
        self.Color_B.setStyleSheet("font: 10pt \"Arial\";")
        self.Color_B.setObjectName("Color_B")
        self.horizontalLayout.addWidget(self.Color_B)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_Led1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led1.setFont(font)
        self.checkBox_Led1.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led1.setObjectName("checkBox_Led1")
        self.gridLayout_2.addWidget(self.checkBox_Led1, 1, 0, 1, 1)
        self.checkBox_Led5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led5.setFont(font)
        self.checkBox_Led5.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led5.setObjectName("checkBox_Led5")
        self.gridLayout_2.addWidget(self.checkBox_Led5, 1, 1, 1, 1)
        self.checkBox_Led7 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led7.setFont(font)
        self.checkBox_Led7.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led7.setObjectName("checkBox_Led7")
        self.gridLayout_2.addWidget(self.checkBox_Led7, 3, 1, 1, 1)
        self.checkBox_Led3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led3.setFont(font)
        self.checkBox_Led3.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led3.setObjectName("checkBox_Led3")
        self.gridLayout_2.addWidget(self.checkBox_Led3, 3, 0, 1, 1)
        self.checkBox_Led2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led2.setFont(font)
        self.checkBox_Led2.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led2.setObjectName("checkBox_Led2")
        self.gridLayout_2.addWidget(self.checkBox_Led2, 2, 0, 1, 1)
        self.checkBox_Led_Mode1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led_Mode1.setFont(font)
        self.checkBox_Led_Mode1.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led_Mode1.setObjectName("checkBox_Led_Mode1")
        self.gridLayout_2.addWidget(self.checkBox_Led_Mode1, 1, 2, 1, 1)
        self.checkBox_Led6 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led6.setFont(font)
        self.checkBox_Led6.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led6.setObjectName("checkBox_Led6")
        self.gridLayout_2.addWidget(self.checkBox_Led6, 2, 1, 1, 1)
        self.checkBox_Led4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led4.setFont(font)
        self.checkBox_Led4.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led4.setObjectName("checkBox_Led4")
        self.gridLayout_2.addWidget(self.checkBox_Led4, 4, 0, 1, 1)
        self.checkBox_Led8 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led8.setFont(font)
        self.checkBox_Led8.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led8.setObjectName("checkBox_Led8")
        self.gridLayout_2.addWidget(self.checkBox_Led8, 4, 1, 1, 1)
        self.checkBox_Led_Mode2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led_Mode2.setFont(font)
        self.checkBox_Led_Mode2.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led_Mode2.setObjectName("checkBox_Led_Mode2")
        self.gridLayout_2.addWidget(self.checkBox_Led_Mode2, 2, 2, 1, 1)
        self.checkBox_Led_Mode3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led_Mode3.setFont(font)
        self.checkBox_Led_Mode3.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led_Mode3.setObjectName("checkBox_Led_Mode3")
        self.gridLayout_2.addWidget(self.checkBox_Led_Mode3, 3, 2, 1, 1)
        self.checkBox_Led_Mode4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_Led_Mode4.setFont(font)
        self.checkBox_Led_Mode4.setStyleSheet("font: 10pt \"Arial\";")
        self.checkBox_Led_Mode4.setObjectName("checkBox_Led_Mode4")
        self.gridLayout_2.addWidget(self.checkBox_Led_Mode4, 4, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Client)
        QtCore.QMetaObject.connectSlotsByName(Client)

    def retranslateUi(self, Client):
        _translate = QtCore.QCoreApplication.translate
        Client.setWindowTitle(_translate("Client", "freenove"))
        self.IP.setText(_translate("Client", "IP Address"))
        self.Btn_Connect.setText(_translate("Client", "Connect"))
        self.Btn_Video.setText(_translate("Client", "Show Video"))
        self.Btn_Turn_Left.setText(_translate("Client", "Turn Left"))
        self.Btn_Buzzer.setText(_translate("Client", "Start"))
        self.Btn_Turn_Right.setText(_translate("Client", "Turn Right"))
        self.Btn_Backward.setText(_translate("Client", "Backward"))
        self.Btn_Forward.setText(_translate("Client", "Forward"))
        self.checkBox_Tracking_Faces.setText(_translate("Client", "FaceTracking"))
        self.Btn_Mode1.setText(_translate("Client", "M-Free"))
        self.Btn_Mode2.setText(_translate("Client", "M-Light"))
        self.Btn_Mode3.setText(_translate("Client", "M-Sonic"))
        self.Btn_Mode4.setText(_translate("Client", "M-Line"))
        self.Btn_Left.setText(_translate("Client", "Left"))
        self.Btn_Up.setText(_translate("Client", "Up"))
        self.Btn_Right.setText(_translate("Client", "Right"))
        self.Btn_Down.setText(_translate("Client", "Down"))
        self.Btn_Home.setText(_translate("Client", "Home"))
        self.label_Servo1.setText(_translate("Client", "90"))
        self.label_Servo2.setText(_translate("Client", "0"))
        self.Servo1.setText(_translate("Client", "Servo H"))
        self.label_FineServo1.setText(_translate("Client", "0"))
        self.Servo2.setText(_translate("Client", "Servo V"))
        self.label_FineServo2.setText(_translate("Client", "0"))
        self.Btn_Ultrasonic.setText(_translate("Client", "Ultrasonic"))
        self.Btn_Light.setText(_translate("Client", "Light"))
        self.R.setText(_translate("Client", "R"))
        self.Color_R.setText(_translate("Client", "255"))
        self.G.setText(_translate("Client", "G"))
        self.Color_G.setText(_translate("Client", "0"))
        self.B.setText(_translate("Client", "B"))
        self.Color_B.setText(_translate("Client", "0"))
        self.checkBox_Led1.setText(_translate("Client", "Led1"))
        self.checkBox_Led5.setText(_translate("Client", "Led5"))
        self.checkBox_Led7.setText(_translate("Client", "Led7"))
        self.checkBox_Led3.setText(_translate("Client", "Led3"))
        self.checkBox_Led2.setText(_translate("Client", "Led2"))
        self.checkBox_Led_Mode1.setText(_translate("Client", "Led_Mode1"))
        self.checkBox_Led6.setText(_translate("Client", "Led6"))
        self.checkBox_Led4.setText(_translate("Client", "Led4"))
        self.checkBox_Led8.setText(_translate("Client", "Led8"))
        self.checkBox_Led_Mode2.setText(_translate("Client", "Led_Mode2"))
        self.checkBox_Led_Mode3.setText(_translate("Client", "Led_Mode3"))
        self.checkBox_Led_Mode4.setText(_translate("Client", "Led_Mode4"))
