from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TranslateImage(QtWidgets.QDialog):
    def setupUi(self, TranslateImage):
        TranslateImage.setObjectName("TranslateImage")
        TranslateImage.resize(347, 303)
        
        # Buat QLabel untuk judul
        self.label = QtWidgets.QLabel(TranslateImage)
        self.label.setGeometry(QtCore.QRect(20, 10, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # QLabel untuk label X
        self.label_2 = QtWidgets.QLabel(TranslateImage)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # QLabel untuk label Y
        self.label_3 = QtWidgets.QLabel(TranslateImage)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # QLineEdit untuk inpX, hanya menerima integer
        self.inpX = QtWidgets.QLineEdit(TranslateImage)
        self.inpX.setGeometry(QtCore.QRect(80, 70, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inpX.setText('0')
        self.inpX.setFont(font)
        self.inpX.setObjectName("inpX")
        self.inpX.setValidator(QtGui.QIntValidator())  # Validator untuk input integer

        # QLineEdit untuk inpY, hanya menerima integer
        self.inpY = QtWidgets.QLineEdit(TranslateImage)
        self.inpY.setGeometry(QtCore.QRect(80, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inpY.setText('0')
        self.inpY.setFont(font)
        self.inpY.setObjectName("inpY")
        self.inpY.setValidator(QtGui.QIntValidator())  # Validator untuk input integer

        # QPushButton untuk OK
        self.btnOk = QtWidgets.QPushButton(TranslateImage)
        self.btnOk.setGeometry(QtCore.QRect(200, 200, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")

        self.btnOk.clicked.connect(TranslateImage.accept)

        self.retranslateUi(TranslateImage)
        QtCore.QMetaObject.connectSlotsByName(TranslateImage)

    def retranslateUi(self, TranslateImage):
        _translate = QtCore.QCoreApplication.translate
        TranslateImage.setWindowTitle(_translate("TranslateImage", "TranslateImage"))
        self.label.setText(_translate("TranslateImage", "Translate Image"))
        self.label_2.setText(_translate("TranslateImage", "X : "))
        self.label_3.setText(_translate("TranslateImage", "Y : "))
        self.btnOk.setText(_translate("TranslateImage", "OK"))

    def get_x(self):
        try:
            return int(self.inpX.text())
        except ValueError:
            return 0 
        
    def get_y(self):
        try:
            return int(self.inpY.text())
        except ValueError:
            return 0 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TranslateImage = QtWidgets.QMainWindow()
    ui = Ui_TranslateImage()
    ui.setupUi(TranslateImage)
    TranslateImage.show()
    sys.exit(app.exec_())
