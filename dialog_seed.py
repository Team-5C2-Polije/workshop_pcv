from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegionGrowing(object):
    def setupUi(self, RegionGrowing):
        RegionGrowing.setObjectName("RegionGrowing")
        RegionGrowing.resize(323, 250)
        
        # Buat widget utama tanpa menggunakan setCentralWidget
        self.centralwidget = QtWidgets.QWidget(RegionGrowing)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # inpSeed1: hanya menerima input berupa angka
        self.inpSeed1 = QtWidgets.QLineEdit(self.centralwidget)
        self.inpSeed1.setGeometry(QtCore.QRect(80, 20, 61, 41))
        font.setPointSize(14)
        self.inpSeed1.setFont(font)
        self.inpSeed1.setObjectName("inpSeed1")
        self.inpSeed1.setText("10")
        self.inpSeed1.setValidator(QtGui.QIntValidator())  # Validasi hanya integer

        # inpSeed2: hanya menerima input berupa angka
        self.inpSeed2 = QtWidgets.QLineEdit(self.centralwidget)
        self.inpSeed2.setGeometry(QtCore.QRect(150, 20, 61, 41))
        self.inpSeed2.setFont(font)
        self.inpSeed2.setObjectName("inpSeed2")
        self.inpSeed2.setValidator(QtGui.QIntValidator())  # Validasi hanya integer
        self.inpSeed2.setText("10")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 81, 41))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # inpThresold: hanya menerima input berupa angka
        self.inpThresold = QtWidgets.QLineEdit(self.centralwidget)
        self.inpThresold.setGeometry(QtCore.QRect(110, 80, 101, 41))
        self.inpThresold.setFont(font)
        self.inpThresold.setObjectName("inpThresold")
        self.inpThresold.setValidator(QtGui.QIntValidator())  # Validasi hanya integer
        self.inpThresold.setText("20") 

        self.btnOk = QtWidgets.QPushButton(self.centralwidget)
        self.btnOk.setGeometry(QtCore.QRect(180, 150, 121, 51))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")
        self.btnOk.clicked.connect(RegionGrowing.accept)  # Menghubungkan ke accept() dialog

        # Atur layout secara manual
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.inpSeed1)
        layout.addWidget(self.inpSeed2)
        layout.addWidget(self.label_2)
        layout.addWidget(self.inpThresold)
        layout.addWidget(self.btnOk)
        
        # Set layout ke QDialog
        RegionGrowing.setLayout(layout)

        self.retranslateUi(RegionGrowing)
        QtCore.QMetaObject.connectSlotsByName(RegionGrowing)

    def retranslateUi(self, RegionGrowing):
        _translate = QtCore.QCoreApplication.translate
        RegionGrowing.setWindowTitle(_translate("RegionGrowing", "Region Growing"))
        self.label.setText(_translate("RegionGrowing", "Seed"))
        self.label_2.setText(_translate("RegionGrowing", "Thresold"))
        self.btnOk.setText(_translate("RegionGrowing", "OK"))

    # Method untuk mendapatkan nilai dari inpSeed1
    def get_inpSeed1(self):
        return int(self.inpSeed1.text())  # Mengembalikan nilai sebagai integer

    # Method untuk mendapatkan nilai dari inpSeed2
    def get_inpSeed2(self):
        return int(self.inpSeed2.text())  # Mengembalikan nilai sebagai integer

    # Method untuk mendapatkan nilai dari inpThresold
    def get_inpThresold(self):
        return int(self.inpThresold.text())  # Mengembalikan nilai sebagai integer
