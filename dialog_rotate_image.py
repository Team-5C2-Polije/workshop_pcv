from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RotateImage(QtWidgets.QDialog):
    def setupUi(self, RotateImage):
        RotateImage.setObjectName("RotateImage")
        RotateImage.resize(817, 261)
        
        self.label_4 = QtWidgets.QLabel(RotateImage)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.horizontalSlider = QtWidgets.QSlider(RotateImage)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 100, 591, 22))
        self.horizontalSlider.setMinimum(-360)
        self.horizontalSlider.setMaximum(360)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        
        self.btnOk_2 = QtWidgets.QPushButton(RotateImage)
        self.btnOk_2.setGeometry(QtCore.QRect(30, 140, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnOk_2.setFont(font)
        self.btnOk_2.setObjectName("btnOk_2")
        self.btnOk_2.clicked.connect(RotateImage.accept)
        
        self.inpY_2 = QtWidgets.QLineEdit(RotateImage)
        self.inpY_2.setGeometry(QtCore.QRect(650, 90, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inpY_2.setFont(font)
        self.inpY_2.setText('0')
        self.inpY_2.setObjectName("inpY_2")
        self.inpY_2.setValidator(QtGui.QIntValidator())

        self.action()

        self.retranslateUi(RotateImage)
        QtCore.QMetaObject.connectSlotsByName(RotateImage)

    def retranslateUi(self, RotateImage):
        _translate = QtCore.QCoreApplication.translate
        RotateImage.setWindowTitle(_translate("RotateImage", "Rotate Image"))
        self.label_4.setText(_translate("RotateImage", "Rotate Image"))
        self.btnOk_2.setText(_translate("RotateImage", "OK"))

    def action(self):
        self.horizontalSlider.valueChanged.connect(self.slider)

    def slider(self):
        value = self.horizontalSlider.value()
        self.inpY_2.setText(str(value))

    def get_rotate(self):
        try:
            return int(self.inpY_2.text())
        except ValueError:
            return 0 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RotateImage = QtWidgets.QDialog()  # Use QDialog here
    ui = Ui_RotateImage()
    ui.setupUi(RotateImage)
    RotateImage.show()
    sys.exit(app.exec_())
