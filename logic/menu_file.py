from PyQt5 import QtCore, QtGui, QtWidgets

class MenuFile:

    outputPath = r"output\output.png"

    def openFile(self):
        # Open file dialog
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        
        if file_path:
            # Load image
            pixmap = QtGui.QPixmap(file_path)
            
            if pixmap.isNull():
                # Display error message in a message box
                error_message = QtWidgets.QMessageBox()
                error_message.setIcon(QtWidgets.QMessageBox.Critical)
                error_message.setText("Error: Failed to load image.")
                error_message.setWindowTitle("Error")
                error_message.exec_()
            else:
                # Display image
                scene = QtWidgets.QGraphicsScene()
                scene.addPixmap(pixmap)
                self.imageInput.setScene(scene)
                self.toolStripLabel.setText(rf"file : ${file_path}")
                file_path = file_path.replace("\\", "/")
                print("FILE : " + file_path)
                return file_path;
        else:
            # Display error message in a message box
            error_message = QtWidgets.QMessageBox()
            error_message.setIcon(QtWidgets.QMessageBox.Critical)
            error_message.setText("Error: Failed to load path.")
            error_message.setWindowTitle("Error")
            error_message.exec_()

        return None

    def clearImage(self):
        if self.imageInput.scene():
            self.imageInput.scene().clear()
        if self.imageOutput.scene():
            self.imageOutput.scene().clear()