from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPen, QPainter
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem
from logic.menu_geometrik import MenuGeometrik

class Ui_CropImage(QtWidgets.QDialog):

    outputPath = ".output"
    outputFile = rf"{outputPath}\temp_crop.png"

    def __init__(self, image_path, parent=None):
        super(Ui_CropImage, self).__init__(parent)
        self.image_path = image_path
        self.start_pos = None
        self.rect_item = None
        self.posTop = 0
        self.posBottom = 0
        self.posRight = 0
        self.posLeft = 0
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(728, 655)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 691, 521))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 560, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.addWidget(self.graphicsView)
        self.verticalLayout.addWidget(self.pushButton)
        self.setLayout(self.verticalLayout)

        # Set the image in the QGraphicsView
        self.set_image(self.image_path)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # Install event filter to handle mouse events
        self.graphicsView.viewport().installEventFilter(self)

        # Connect button click to the validation method
        self.pushButton.clicked.connect(self.validate_crop_area)

    def save_scaled_image(self, output_path):
        # Ambil scene dari QGraphicsView
        scene = self.graphicsView.scene()

        # Buat QPixmap dengan ukuran dari graphicsView
        rect = self.graphicsView.viewport().rect()
        scaled_pixmap = QPixmap(rect.size())

        # Render scene ke QPixmap
        painter = QPainter(scaled_pixmap)
        self.graphicsView.render(painter)
        painter.end()

        # Simpan gambar ke lokasi output
        scaled_pixmap.save(output_path)

    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Error: Could not load image at {image_path}")
            return

        scene = QGraphicsScene(self)
        pixmap_item = QGraphicsPixmapItem(pixmap)

        # Calculate the scale factor to fit the pixmap to the QGraphicsView
        # view_rect = self.graphicsView.rect()
        # pixmap_size = pixmap.size()
        # if pixmap_size.width() == 0 or pixmap_size.height() == 0:
        #     print("Error: Image has zero width or height.")
        #     return

        # scale_x = view_rect.width() / pixmap_size.width()
        # scale_y = view_rect.height() / pixmap_size.height()
        # scale = min(scale_x, scale_y)  # Scale to fit the view

        # pixmap_item.setScale(scale)

        scene.addItem(pixmap_item)
        pixmap.save(Ui_CropImage.outputFile)
        self.graphicsView.setScene(scene)
        # self.save_scaled_image(Ui_CropImage.outputFile)

    def eventFilter(self, source, event):
        if source is self.graphicsView.viewport():
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.start_pos = self.graphicsView.mapToScene(event.pos())
                if self.rect_item:
                    self.graphicsView.scene().removeItem(self.rect_item)
                self.rect_item = QGraphicsRectItem()
                self.rect_item.setPen(QPen(QtGui.QColor('red')))
                self.graphicsView.scene().addItem(self.rect_item)
            elif event.type() == QtCore.QEvent.MouseMove and self.rect_item:
                end_pos = self.graphicsView.mapToScene(event.pos())
                rect = QtCore.QRectF(self.start_pos, end_pos).normalized()
                self.rect_item.setRect(rect)
            elif event.type() == QtCore.QEvent.MouseButtonRelease and self.rect_item:
                self.end_pos = self.graphicsView.mapToScene(event.pos())
                self.rect_item.setRect(QtCore.QRectF(self.start_pos, self.end_pos).normalized())
                self.posTop = self.rect_item.rect().top()
                self.posBottom = self.rect_item.rect().bottom()
                self.posRight = self.rect_item.rect().right()
                self.posLeft = self.rect_item.rect().left()
                self.start_pos = None
        return super(Ui_CropImage, self).eventFilter(source, event)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Crop Image"))
        self.pushButton.setText(_translate("Dialog", "OK"))

    def validate_crop_area(self):
        # Check if the bounding box coordinates are non-zero
        if (self.posTop > 0 and self.posBottom > 0 and
            self.posRight > 0 and self.posLeft > 0):
            print("Bounding Box is valid.")
            print(f"Top: {self.posTop}, Bottom: {self.posBottom}, Right: {self.posRight}, Left: {self.posLeft}")
            # Implement further actions here, like closing the dialog or cropping the image
            MenuGeometrik.crop_image(Ui_CropImage.outputFile, self.posLeft, self.posTop, self.posRight, self.posBottom)
            self.accept()  # Close the dialog with accepted status
        else:
            print("Error: Bounding Box has zero or negative dimensions.")
            # Optionally show an error message or prompt the user to select the bounding box again

    def get_pos_top(self):
        return self.posTop

    def get_pos_bottom(self):
        return self.posBottom

    def get_pos_left(self):
        return self.posLeft

    def get_pos_right(self):
        return self.posRight
    
    def result_image(self):
        return Ui_CropImage.outputFile

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    image_path = 'path_to_your_image.jpg'  # Replace with your image path
    dialog = Ui_CropImage(image_path)
    dialog.exec_()
    sys.exit(app.exec_())
