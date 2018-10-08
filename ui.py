from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
import os
import ascii


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.file_path = ''
        self.file_name = ''
        self.setupUi(self)

    def resizeEvent(self, QResizeEvent):
        targetWidth = self.Form.width() / 2 - 14
        self.image_display.setFixedWidth(targetWidth)
        QtWidgets.QWidget.resizeEvent(self, QResizeEvent)

    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(600, 400)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.grayscale_checkbox = QtWidgets.QCheckBox(Form)
        self.grayscale_checkbox.setObjectName("grayscale_checkbox")
        self.gridLayout.addWidget(self.grayscale_checkbox, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.image_display = QtWidgets.QLabel(Form)
        self.image_display.setObjectName("image_display")
        self.image_display.setScaledContents(True)
        self.image_display.setPixmap(QtGui.QPixmap('temp.png').scaled(self.image_display.height(), self.image_display.width()))
        self.gridLayout.addWidget(self.image_display, 3, 0, 1, 1)
        self.file_label = QtWidgets.QLabel(Form)
        self.file_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.file_label.setObjectName("file_label")
        self.gridLayout.addWidget(self.file_label, 0, 0, 1, 1)
        self.text_display = QtWidgets.QPlainTextEdit(Form)
        self.text_display.setLineWrapMode(0)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(4)
        self.text_display.setFont(font)
        self.text_display.setObjectName("text_display")
        self.gridLayout.addWidget(self.text_display, 3, 1, 1, 1)
        self.file_btn = QtWidgets.QPushButton(Form)
        self.file_btn.setObjectName("file_btn")
        self.gridLayout.addWidget(self.file_btn, 0, 1, 1, 1)
        self.begin_btn = QtWidgets.QPushButton(Form)
        self.begin_btn.setObjectName("begin_btn")
        self.gridLayout.addWidget(self.begin_btn, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        self.bind_buttons()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ASCII Art Creator"))
        self.grayscale_checkbox.setText(_translate("Form", "Simple Grey-scale"))
        self.file_label.setText(_translate("Form", "Selected file: <none>"))
        self.file_btn.setText(_translate("Form", "Select file"))
        self.begin_btn.setText(_translate("Form", "Create ASCII Art"))

    def bind_buttons(self):
        self.file_btn.clicked.connect(self.select_file)
        self.begin_btn.clicked.connect(lambda: self.convert_to_ascii(self.file_path))

    def convert_to_ascii(self, file):
        ascii.start_converting(file, self.grayscale_checkbox.isChecked())
        ascii_txt = open(os.path.basename(file).split('.')[0] + '.txt').read()
        self.text_display.setPlainText(ascii_txt)

    def select_file(self):
        root = tk.Tk()
        root.withdraw()
        self.file_path = filedialog.askopenfilename(initialdir='.', filetypes=(("Graphic files",'*.jpg;*.png'), ('All files', '*.*')))
        root.destroy()

        self.file_label.setText('Selected file: ' + os.path.basename(self.file_path))
        height = self.image_display.height()
        width = self.image_display.width()
        if height > 500 or width > 500:
            ratio = width / height
            if ratio > 1:
                width = 500
                height = 500/ratio
            else:
                width = 500/ratio
                height = 500

        pixmap = QtGui.QPixmap(self.file_path).scaled(height, width)
        self.image_display.setPixmap(pixmap)


