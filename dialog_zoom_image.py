from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ZoomImage(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(348, 316)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        # Use QLineEdit for number input
        self.inpX_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.inpX_2.setGeometry(QtCore.QRect(10, 140, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inpX_2.setFont(font)
        self.inpX_2.setText("1")
        self.inpX_2.setObjectName("inpX_2")

        # Set integer validator for QLineEdit to allow only integer input
        self.inpX_2.setValidator(QtGui.QIntValidator())

        self.btnOk_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk_2.setGeometry(QtCore.QRect(200, 210, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnOk_2.setFont(font)
        self.btnOk_2.setObjectName("btnOk_2")
        self.btnOk_2.clicked.connect(Dialog.accept)  # Connect button click to Dialog's accept method

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        Dialog.setLayout(QtWidgets.QVBoxLayout())
        Dialog.layout().addWidget(self.centralwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Zoom Image"))
        self.label_4.setText(_translate("Dialog", "Zoom Image"))
        self.btnOk_2.setText(_translate("Dialog", "OK"))
        self.label_5.setText(_translate("Dialog", "Zoom Factor : "))

    def get_zoom_level(self):
        try:
            return int(self.inpX_2.text())
        except ValueError:
            return 0 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()  # Create a QDialog instance
    ui = Ui_ZoomImage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
