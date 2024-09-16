from PyQt5 import QtGui, QtWidgets
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
from matplotlib import pyplot as plt

import os

class MenuView:
    outputPath = ".output"
    outputFile = rf"{outputPath}\output.png"

    def showHistogram(imagePath, title):
        # Membaca gambar menggunakan OpenCV
        image = cv2.imread(imagePath)
        
        plt.figure(figsize=(8, 6))

        # Menghitung histogram untuk channel 0 (Red)
        histogram_image = cv2.calcHist([image], [0], None, [256], [0, 256])

        # Membuat subplot dengan benar
        plt.subplot(1, 1, 1)  # 1 baris, 1 kolom, subplot pertama
        plt.title(title)
        plt.plot(histogram_image)
        plt.xlim([0, 256])
        plt.show()

