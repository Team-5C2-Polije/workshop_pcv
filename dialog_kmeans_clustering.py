from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KmeansCLus(object):
    def setupUi(self, KmeansCLusDialog):
        KmeansCLusDialog.setObjectName("KmeansCLusDialog")
        KmeansCLusDialog.resize(254, 194)
        
        # Widget utama tidak menggunakan setCentralWidget
        self.centralwidget = QtWidgets.QWidget(KmeansCLusDialog)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        # Input Text untuk K
        self.inpK = QtWidgets.QLineEdit(self.centralwidget)
        self.inpK.setGeometry(QtCore.QRect(80, 10, 61, 41))
        font.setPointSize(14)
        self.inpK.setFont(font)
        self.inpK.setObjectName("inpK")
        self.inpK.setValidator(QtGui.QIntValidator())  # Validasi hanya angka
        self.inpK.setText("2")
        
        # Tombol OK
        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(20, 80, 121, 51))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(KmeansCLusDialog.accept)  # Menutup dialog saat OK
        
        # Menambahkan layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label_3)
        layout.addWidget(self.inpK)
        layout.addWidget(self.btnOk)
        
        # Set layout ke QDialog
        KmeansCLusDialog.setLayout(layout)

        self.retranslateUi(KmeansCLusDialog)
        QtCore.QMetaObject.connectSlotsByName(KmeansCLusDialog)

    def retranslateUi(self, KmeansCLusDialog):
        _translate = QtCore.QCoreApplication.translate
        KmeansCLusDialog.setWindowTitle(_translate("KmeansCLusDialog", "Kmeans Clustering"))
        self.label_3.setText(_translate("KmeansCLusDialog", "K"))
        self.btnOk.setText(_translate("KmeansCLusDialog", "OK"))

    # Method untuk mendapatkan nilai input K
    def get_inpK(self):
        return int(self.inpK.text())  # Mengembalikan nilai K sebagai integer
