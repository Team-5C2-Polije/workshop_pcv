from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QAction, QApplication, QMainWindow
import cv2
import numpy as np
import os

class Ui_AricmaticWindow(object):

    image1 = None
    image2 = None
    outputPath = ".output"
    outputFile = rf"{outputPath}\output.png"

    def setupUi(self, AricmaticWindow):
        AricmaticWindow.setObjectName("AricmaticWindow")
        AricmaticWindow.resize(1254, 444)
        self.centralwidget = QtWidgets.QWidget(AricmaticWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photoInput1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.photoInput1.setGeometry(QtCore.QRect(20, 50, 391, 341))
        self.photoInput1.setObjectName("photoInput1")
        self.photoInput2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.photoInput2.setGeometry(QtCore.QRect(430, 50, 391, 341))
        self.photoInput2.setObjectName("photoInput2")
        self.photoOutput = QtWidgets.QGraphicsView(self.centralwidget)
        self.photoOutput.setGeometry(QtCore.QRect(840, 50, 391, 341))
        self.photoOutput.setObjectName("photoOutput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 20, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(840, 20, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        AricmaticWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AricmaticWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1254, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuClear_2 = QtWidgets.QMenu(self.menuFile)
        self.menuClear_2.setObjectName("menuClear_2")
        self.menuAritmatika = QtWidgets.QMenu(self.menubar)
        self.menuAritmatika.setObjectName("menuAritmatika")
        self.menu0perations = QtWidgets.QMenu(self.menubar)
        self.menu0perations.setObjectName("menu0perations")
        self.menuClear = QtWidgets.QMenu(self.menubar)
        self.menuClear.setTitle("")
        self.menuClear.setObjectName("menuClear")
        AricmaticWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AricmaticWindow)
        self.statusbar.setObjectName("statusbar")
        AricmaticWindow.setStatusBar(self.statusbar)
        self.actionImage_1 = QtWidgets.QAction(AricmaticWindow)
        self.actionImage_1.setObjectName("actionImage_1")
        self.actionImage_2 = QtWidgets.QAction(AricmaticWindow)
        self.actionImage_2.setObjectName("actionImage_2")
        self.actionClear_Image_1 = QtWidgets.QAction(AricmaticWindow)
        self.actionClear_Image_1.setObjectName("actionClear_Image_1")
        self.actionClear_Image_2 = QtWidgets.QAction(AricmaticWindow)
        self.actionClear_Image_2.setObjectName("actionClear_Image_2")
        self.actionInput_1 = QtWidgets.QAction(AricmaticWindow)
        self.actionInput_1.setObjectName("actionInput_1")
        self.actionInput_2 = QtWidgets.QAction(AricmaticWindow)
        self.actionInput_2.setObjectName("actionInput_2")
        self.actionClear_All = QtWidgets.QAction(AricmaticWindow)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionClear_Image1 = QtWidgets.QAction(AricmaticWindow)
        self.actionClear_Image1.setObjectName("actionClear_Image1")
        self.actionClear_Image2 = QtWidgets.QAction(AricmaticWindow)
        self.actionClear_Image2.setObjectName("actionClear_Image2")
        self.actionAddition = QtWidgets.QAction(AricmaticWindow)
        self.actionAddition.setObjectName("actionAddition")
        self.actionSubtraction = QtWidgets.QAction(AricmaticWindow)
        self.actionSubtraction.setObjectName("actionSubtraction")
        self.actionMultiplication = QtWidgets.QAction(AricmaticWindow)
        self.actionMultiplication.setObjectName("actionMultiplication")
        self.actionDivision = QtWidgets.QAction(AricmaticWindow)
        self.actionDivision.setObjectName("actionDivision")
        self.actionOR = QtWidgets.QAction(AricmaticWindow)
        self.actionOR.setObjectName("actionOR")
        self.actionAND = QtWidgets.QAction(AricmaticWindow)
        self.actionAND.setObjectName("actionAND")
        self.actionXOR = QtWidgets.QAction(AricmaticWindow)
        self.actionXOR.setObjectName("actionXOR")
        self.actionSave_Output = QtWidgets.QAction(AricmaticWindow)
        self.actionSave_Output.setObjectName("actionSave_Output")
        self.actionClear_All_2 = QtWidgets.QAction(AricmaticWindow)
        self.actionClear_All_2.setObjectName("actionClear_All_2")
        self.actionOpen_Output_to_Photo = QtWidgets.QAction(AricmaticWindow)
        self.actionOpen_Output_to_Photo.setObjectName("actionOpen_Output_to_Photo")
        self.actionSave_As = QtWidgets.QAction(AricmaticWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.menuOpen.addAction(self.actionInput_1)
        self.menuOpen.addAction(self.actionInput_2)
        self.menuOpen.addAction(self.actionOpen_Output_to_Photo)
        self.menuClear_2.addAction(self.actionClear_All_2)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.menuClear_2.menuAction())
        self.menuFile.addAction(self.actionSave_As)
        self.menuAritmatika.addAction(self.actionAddition)
        self.menuAritmatika.addAction(self.actionSubtraction)
        self.menuAritmatika.addAction(self.actionMultiplication)
        self.menuAritmatika.addAction(self.actionDivision)
        self.menu0perations.addAction(self.actionOR)
        self.menu0perations.addAction(self.actionAND)
        self.menu0perations.addAction(self.actionXOR)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAritmatika.menuAction())
        self.menubar.addAction(self.menu0perations.menuAction())
        self.menubar.addAction(self.menuClear.menuAction())

        self.action(AricmaticWindow)

        self.retranslateUi(AricmaticWindow)
        QtCore.QMetaObject.connectSlotsByName(AricmaticWindow)

    def retranslateUi(self, AricmaticWindow):
        _translate = QtCore.QCoreApplication.translate
        AricmaticWindow.setWindowTitle(_translate("AricmaticWindow", "AricmaticWindow"))
        self.label.setText(_translate("AricmaticWindow", "Input 1"))
        self.label_2.setText(_translate("AricmaticWindow", "Input 2"))
        self.label_3.setText(_translate("AricmaticWindow", "Output"))
        self.menuFile.setTitle(_translate("AricmaticWindow", "File"))
        self.menuOpen.setTitle(_translate("AricmaticWindow", "Open"))
        self.menuClear_2.setTitle(_translate("AricmaticWindow", "Clear"))
        self.menuAritmatika.setTitle(_translate("AricmaticWindow", "Aritmatika 0perations"))
        self.menu0perations.setTitle(_translate("AricmaticWindow", "Logical 0perations"))
        self.actionImage_1.setText(_translate("AricmaticWindow", "Image 1"))
        self.actionImage_2.setText(_translate("AricmaticWindow", "Image 2"))
        self.actionClear_Image_1.setText(_translate("AricmaticWindow", "Clear Image 1"))
        self.actionClear_Image_2.setText(_translate("AricmaticWindow", "Clear Image 2"))
        self.actionInput_1.setText(_translate("AricmaticWindow", "Input 1"))
        self.actionInput_2.setText(_translate("AricmaticWindow", "Input 2"))
        self.actionClear_All.setText(_translate("AricmaticWindow", "Clear All"))
        self.actionClear_Image1.setText(_translate("AricmaticWindow", "Clear Image 1"))
        self.actionClear_Image2.setText(_translate("AricmaticWindow", "Clear Image 2"))
        self.actionAddition.setText(_translate("AricmaticWindow", "Addition"))
        self.actionSubtraction.setText(_translate("AricmaticWindow", "Subtraction"))
        self.actionMultiplication.setText(_translate("AricmaticWindow", "Multiplication"))
        self.actionDivision.setText(_translate("AricmaticWindow", "Division"))
        self.actionOR.setText(_translate("AricmaticWindow", "OR"))
        self.actionAND.setText(_translate("AricmaticWindow", "AND"))
        self.actionXOR.setText(_translate("AricmaticWindow", "XOR"))
        self.actionSave_Output.setText(_translate("AricmaticWindow", "Save Output"))
        self.actionClear_All_2.setText(_translate("AricmaticWindow", "Clear All"))
        self.actionOpen_Output_to_Photo.setText(_translate("AricmaticWindow", "Open Output to Photo"))
        self.actionSave_As.setText(_translate("AricmaticWindow", "Save As"))

    def action(self, AricmaticWindow):
        self.actionInput_1.triggered.connect(self.openFileImage1)
        self.actionInput_2.triggered.connect(self.openFileImage2)
        self.actionAddition.triggered.connect(self.addition)
        self.actionSubtraction.triggered.connect(self.subtract)
        self.actionMultiplication.triggered.connect(self.multiply)
        self.actionDivision.triggered.connect(self.division)
        self.actionOR.triggered.connect(self.bitwise_or)
        self.actionAND.triggered.connect(self.bitwise_and)
        self.actionXOR.triggered.connect(self.bitwise_xor)
        self.actionClear_All_2.triggered.connect(self.clear_all)
        self.actionOpen_Output_to_Photo.triggered.connect(self.open_ouput_in_photo)
        self.actionSave_As.triggered.connect(self.saveAs)

    def openFileImage(self, target_view):
        # Open file dialog
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        
        if file_path:
            # Load and convert image to grayscale
            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # Convert to grayscale
            if image is None:
                self.showErrorMessage("Error: Failed to load image.")
                return None
            
            # Resize the grayscale image to 800x800
            image_resized = cv2.resize(image, (800, 800))

            # Save the converted image to the global variable
            if target_view == 1:
                self.image1 = image_resized
            elif target_view == 2:
                self.image2 = image_resized

            # Convert resized grayscale image to QPixmap for display
            height, width = image_resized.shape
            bytes_per_line = width
            q_image = QtGui.QImage(image_resized.data, width, height, bytes_per_line, QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap.fromImage(q_image)

            # Display the image in the target view
            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(pixmap)
        if target_view == 1:
            self.photoInput1.setScene(scene)
        elif target_view == 2:
            self.photoInput2.setScene(scene)

            file_path = file_path.replace("\\", "/")
            print("FILE : " + file_path)
            return file_path
        else:
            self.showErrorMessage("Error: Failed to load path.")
            return None

    def displayResult(self, image, target_view):
        # Convert OpenCV image (which is in numpy array format) to QImage
        height, width = image.shape
        bytes_per_line = width
        q_image = QtGui.QImage(image.data, width, height, bytes_per_line, QtGui.QImage.Format_Grayscale8)

        # Convert QImage to QPixmap for displaying in QGraphicsView
        pixmap = QtGui.QPixmap.fromImage(q_image)
        scene = QtWidgets.QGraphicsScene()
        scene.addPixmap(pixmap)

        # Set the scene in the target QGraphicsView (e.g., photoOutput)
        target_view.setScene(scene)

    def showErrorMessage(self, message):
        # Display error message in a message box
        error_message = QtWidgets.QMessageBox()
        error_message.setIcon(QtWidgets.QMessageBox.Critical)
        error_message.setText(message)
        error_message.setWindowTitle("Error")
        error_message.exec_()

    def openFileImage1(self):
        return self.openFileImage(1)

    def openFileImage2(self):
        return self.openFileImage(2)
    
    def addition(self):
        if self.image1 is not None and self.image2 is not None:
            addition_result = cv2.add(self.image1, self.image2)
            cv2.imwrite(self.outputFile, addition_result)
            self.displayResult(addition_result, self.photoOutput)
        else:
            self.showErrorMessage("Error: One or both images are not loaded.")

    def subtract(self):
        if self.image1 is not None and self.image2 is not None:
            addition_result = cv2.subtract(self.image1, self.image2)
            cv2.imwrite(self.outputFile, addition_result)
            self.displayResult(addition_result, self.photoOutput)
        else:
            self.showErrorMessage("Error: One or both images are not loaded.")

    def multiply(self):
        if self.image1 is not None and self.image2 is not None:
            addition_result = cv2.multiply(self.image1, self.image2)
            cv2.imwrite(self.outputFile, addition_result)
            self.displayResult(addition_result, self.photoOutput)
        else:
            self.showErrorMessage("Error: One or both images are not loaded.")

    def division(self):
        if self.image1 is not None and self.image2 is not None:
            with np.errstate(divide='ignore', invalid='ignore'):
                division_result = cv2.divide(self.image1.astype('float'), self.image2.astype('float'))
                division_result = np.nan_to_num(division_result).astype('uint8')
            cv2.imwrite(self.outputFile, division_result)
            self.displayResult(division_result, self.photoOutput)
        else:
            self.showErrorMessage("Error: One or both images are not loaded.")

    def bitwise_or(self):
        if self.image1 is not None and self.image2 is not None:
            addition_result = cv2.bitwise_or(self.image1, self.image2)
            cv2.imwrite(self.outputFile, addition_result)
            self.displayResult(addition_result, self.photoOutput)
        else:
            self.showErrorMessage("Error: One or both images are not loaded.")

    def bitwise_and(self):
        if self.image1 is not None and self.image2 is not None:
            addition_result = cv2.bitwise_and(self.image1, self.image2)
            cv2.imwrite(self.outputFile, addition_result)
            self.displayResult(addition_result, self.photoOutput)
        else:
            self.showErrorMessage("Error: One or both images are not loaded.")

    def bitwise_xor(self):
        if self.image1 is not None and self.image2 is not None:
            addition_result = cv2.bitwise_xor(self.image1, self.image2)
            cv2.imwrite(self.outputFile, addition_result)
            self.displayResult(addition_result, self.photoOutput)
        else:
            self.showErrorMessage("Error: One or both images are not loaded.")

    def clear_all(self):
        # Clear the scenes in photoOutput, photoInput1, and photoInput2
        self.photoOutput.setScene(None)
        self.photoInput1.setScene(None)
        self.photoInput2.setScene(None)

        # Reset image1 and image2 to None
        self.image1 = None
        self.image2 = None

        print("All images cleared.")

    def open_ouput_in_photo(self):
        image_path = self.outputFile
        # Cek apakah file gambar ada
        if os.path.exists(image_path):
            try:
                # Membuka gambar dengan aplikasi Photo
                os.startfile(image_path)
                print(f"Gambar {image_path} dibuka di Photo.")
            except Exception as e:
                print(f"Error saat membuka gambar: {e}")
        else:
            print(f"File {image_path} tidak ditemukan.")

    # digunakan untuk menyimpan hasil output dari processing
    def saveAs(self):
        if not os.path.exists(self.outputFile):
            QMessageBox.warning(None, "Warning", "Output file does not exist.")
            return

        # Open Save As dialog
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(None, "Save Image As", "", 
                                                "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)", 
                                                options=options)
        if filePath:
            try:
                # Save the file to the chosen path
                image = Image.open(self.outputFile)
                image.save(filePath)
                QMessageBox.information(None, "Success", "Image saved successfully.")
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Failed to save the image: {str(e)}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AricmaticWindow = QtWidgets.QMainWindow()
    ui = Ui_AricmaticWindow()
    ui.setupUi(AricmaticWindow)
    AricmaticWindow.show()
    sys.exit(app.exec_())
