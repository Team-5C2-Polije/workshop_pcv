from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GlobalThres(object):
    def setupUi(self, GlobalThresDialog):
        GlobalThresDialog.setObjectName("GlobalThresDialog")
        GlobalThresDialog.resize(271, 193)

        # Widget utama tanpa menggunakan setCentralWidget
        self.centralwidget = QtWidgets.QWidget(GlobalThresDialog)
        self.centralwidget.setObjectName("centralwidget")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Input Text untuk Threshold Value
        self.inpThres = QtWidgets.QLineEdit(self.centralwidget)
        self.inpThres.setGeometry(QtCore.QRect(170, 20, 61, 41))
        font.setPointSize(14)
        self.inpThres.setFont(font)
        self.inpThres.setObjectName("inpThres")
        self.inpThres.setValidator(QtGui.QIntValidator())  # Validasi hanya angka
        self.inpThres.setText("100")

        # Tombol OK
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(20, 90, 121, 51))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(GlobalThresDialog.accept)  # Menutup dialog saat OK

        # Menambahkan layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label_3)
        layout.addWidget(self.inpThres)
        layout.addWidget(self.btnOk)

        # Set layout ke QDialog
        GlobalThresDialog.setLayout(layout)

        self.retranslateUi(GlobalThresDialog)
        QtCore.QMetaObject.connectSlotsByName(GlobalThresDialog)

    def retranslateUi(self, GlobalThresDialog):
        _translate = QtCore.QCoreApplication.translate
        GlobalThresDialog.setWindowTitle(_translate("GlobalThresDialog", "Global Thresholding"))
        self.label_3.setText(_translate("GlobalThresDialog", "Threshold Value"))
        self.btnOk.setText(_translate("GlobalThresDialog", "OK"))

    # Method untuk mendapatkan nilai input Threshold
    def get_inpThres(self):
        return int(self.inpThres.text())  # Mengembalikan nilai threshold sebagai integer
