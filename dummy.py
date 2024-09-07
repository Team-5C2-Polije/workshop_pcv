from PyQt5 import QtCore, QtGui, QtWidgets
from dialog_factor_linear import Ui_SliderPop


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 120, 161, 81))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionShow = QtWidgets.QAction(MainWindow)
        self.actionShow.setObjectName("actionShow")
        self.menuFile.addAction(self.actionShow)
        self.menubar.addAction(self.menuFile.menuAction())

        # // TODO : tampilkan Ui_SliderPop saat saya mengklik tombol actionShow
        # // tampilkan Ui_SliderPop dan jangan tutup window MainWindow
        # self.actionShow.triggered.connect()

        # Connect the actionShow trigger to the method that shows SliderPop
        self.actionShow.triggered.connect(self.show_slider_pop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Show Dialog"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionShow.setText(_translate("MainWindow", "show"))

        # Method to show the SliderPop window
    def show_slider_pop(self):
        self.slider_pop_window = QtWidgets.QMainWindow()
        self.ui = Ui_SliderPop('PUT YOUR IMAGE') 
        self.ui.setupUi(self.slider_pop_window)
        self.slider_pop_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
