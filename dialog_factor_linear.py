from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogFactorLinear(object):

    def __init__(self, imageOutputPath=''):
        self._imageOutputPath = imageOutputPath

    brightnessFactor = 0
    constrastFactor = 0
    saturationFactor = 0

    def setupUi(self, DialogFactorLinear):
        DialogFactorLinear.setObjectName("DialogFactorLinear")
        DialogFactorLinear.resize(1076, 339)
        self.centralwidget = QtWidgets.QWidget(DialogFactorLinear)
        self.centralwidget.setObjectName("centralwidget")
        self.inpContrast = QtWidgets.QTextEdit(self.centralwidget)
        self.inpContrast.setGeometry(QtCore.QRect(930, 100, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inpContrast.setFont(font)
        self.inpContrast.setObjectName("inpContrast")
        self.inpBright = QtWidgets.QTextEdit(self.centralwidget)
        self.inpBright.setGeometry(QtCore.QRect(930, 40, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inpBright.setFont(font)
        self.inpBright.setObjectName("inpBright")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.slideContrast = QtWidgets.QSlider(self.centralwidget)
        self.slideContrast.setGeometry(QtCore.QRect(160, 110, 751, 22))
        self.slideContrast.setMinimum(-255)
        self.slideContrast.setMaximum(255)
        self.slideContrast.setProperty("value", 0)
        self.slideContrast.setOrientation(QtCore.Qt.Horizontal)
        self.slideContrast.setObjectName("slideContrast")
        self.slideContrast.setValue(0)
        self.slideBrightness = QtWidgets.QSlider(self.centralwidget)
        self.slideBrightness.setGeometry(QtCore.QRect(160, 50, 751, 22))
        self.slideBrightness.setMinimum(-255)
        self.slideBrightness.setMaximum(255)
        self.slideBrightness.setProperty("value", 0)
        self.slideBrightness.setOrientation(QtCore.Qt.Horizontal)
        self.slideBrightness.setObjectName("slideBrightness")
        self.slideBrightness.setValue(0)
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(480, 240, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.slideSaturation = QtWidgets.QSlider(self.centralwidget)
        self.slideSaturation.setGeometry(QtCore.QRect(160, 170, 751, 22))
        self.slideSaturation.setMinimum(-255)
        self.slideSaturation.setMaximum(255)
        self.slideSaturation.setProperty("value", 0)
        self.slideSaturation.setOrientation(QtCore.Qt.Horizontal)
        self.slideSaturation.setObjectName("slideSaturation")
        self.slideSaturation.setValue(0)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.inpSaturation = QtWidgets.QTextEdit(self.centralwidget)
        self.inpSaturation.setGeometry(QtCore.QRect(930, 160, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inpSaturation.setFont(font)
        self.inpSaturation.setObjectName("inpSaturation")
        DialogFactorLinear.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DialogFactorLinear)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1076, 31))
        self.menubar.setObjectName("menubar")
        DialogFactorLinear.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DialogFactorLinear)
        self.statusbar.setObjectName("statusbar")
        DialogFactorLinear.setStatusBar(self.statusbar)
        self.inpBright.setText("0")
        self.inpContrast.setText("0")
        self.inpSaturation.setText("0")

        # Connect actions to slots
        self.action()

        self.retranslateUi(DialogFactorLinear)
        QtCore.QMetaObject.connectSlotsByName(DialogFactorLinear)

    def retranslateUi(self, DialogFactorLinear):
        _translate = QtCore.QCoreApplication.translate
        DialogFactorLinear.setWindowTitle(_translate("DialogFactorLinear", "Linear Factor Dialog"))
        self.label_2.setText(_translate("DialogFactorLinear", "Contrast : "))
        self.btnOk.setText(_translate("DialogFactorLinear", "OK"))
        self.label.setText(_translate("DialogFactorLinear", "Brightness : "))
        self.label_3.setText(_translate("DialogFactorLinear", "Saturation : "))

    def action(self):
        self.slideBrightness.valueChanged.connect(self.brightness_slider)
        self.slideContrast.valueChanged.connect(self.contrast_slider)
        self.slideSaturation.valueChanged.connect(self.saturation_slider)

    def brightness_slider(self):
        value = self.slideBrightness.value()
        self.inpBright.setText(str(value))

    def contrast_slider(self):
        value = self.slideContrast.value()
        self.inpContrast.setText(str(value))

    def saturation_slider(self):
        value = self.slideSaturation.value()
        self.inpSaturation.setText(str(value))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogFactorLinear = QtWidgets.QMainWindow()
    ui = Ui_DialogFactorLinear()
    ui.setupUi(DialogFactorLinear)
    DialogFactorLinear.show()
    sys.exit(app.exec_())
