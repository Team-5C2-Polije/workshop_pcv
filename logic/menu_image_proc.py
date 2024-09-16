from PyQt5 import QtGui, QtWidgets
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
from matplotlib import pyplot as plt
from PyQt5.QtGui import QImage, QColor, QPixmap
from PyQt5.QtCore import Qt

class MenuImageProc:

    outputPath = ".output"
    outputFile = rf"{outputPath}\output.png"

    def histogram_citra(image_path):
        # Membaca citra dari path direktori
        image = cv2.imread(image_path)
        
        # Konversi citra dari BGR (format default OpenCV) ke RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Memisahkan kanal warna
        channels = ('r', 'g', 'b')
        colors = ('red', 'green', 'blue')

        plt.figure(figsize=(10, 5))

        for i, color in enumerate(colors):
            histogram = cv2.calcHist([image_rgb], [i], None, [256], [0, 256])
            plt.plot(histogram, color=color)
        
        plt.xlim([0, 256])
        plt.title('Histogram untuk setiap kanal warna')
        plt.xlabel('Intensitas Pixel')
        plt.ylabel('Jumlah Pixel')

        # Simpan histogram ke file
        plt.savefig(MenuImageProc.outputFile)

        # Tampilkan histogram
        plt.show()

        return MenuImageProc.outputFile
    
    def histogram_equalization(image_path):
        image_asli = cv2.imread(image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        equalized_image = cv2.equalizeHist(image)
        cv2.imwrite(MenuImageProc.outputFile, equalized_image)

        histogram_image = cv2.calcHist([image], [0], None, [256], [0, 256])
        histogram_equalized_image = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

        plt.figure(figsize=(12, 6))

        plt.subplot(2, 2, 1)
        plt.title('Original Image')
        plt.imshow(cv2.cvtColor(image_asli, cv2.COLOR_BGR2RGB))
        plt.axis('off')

        plt.subplot(2, 2, 2)
        plt.title('Equalization Image')
        plt.imshow(equalized_image, cmap='gray')
        plt.axis('off')

        plt.subplot(2, 2, 3)
        plt.title('Original Image Histogram')
        plt.plot(histogram_image)
        plt.xlim([0, 256])

        plt.subplot(2, 2, 4)
        plt.title('Equalized Image Histogram')
        plt.plot(histogram_equalized_image)
        plt.xlim([0, 256])

        plt.show()

        return MenuImageProc.outputFile

    def __fuzzy_membership_function__(x, mean, stddev):
        return np.exp(-((x - mean) ** 2) / (2 * (stddev ** 2)))

    def __fuzzy_grayscale_proc__(image, block_size=16):
        # Konversi gambar ke grayscale jika diperlukan
        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Dapatkan dimensi gambar
        height, width = image.shape

        # Buat gambar yang telah di-equalize
        equalized_image = np.zeros_like(image, dtype=np.uint8)

        # Ukuran blok
        block_height = block_size
        block_width = block_size

        for y in range(0, height, block_height):
            for x in range(0, width, block_width):
                # Definisikan batas blok
                block = image[y:y+block_height, x:x+block_width]
                if block.size == 0:
                    continue

                # Hitung histogram lokal
                hist, bins = np.histogram(block.flatten(), bins=256, range=[0, 256])
                cdf = hist.cumsum()
                cdf_normalized = cdf * 255 / cdf[-1]
                equalized_block = np.interp(block.flatten(), bins[:-1], cdf_normalized).reshape(block.shape)

                # Hitung keanggotaan fuzzy
                mean = np.mean(equalized_block)
                stddev = np.std(equalized_block)
                membership = MenuImageProc.__fuzzy_membership_function__(equalized_block, mean, stddev)

                # Terapkan penyesuaian kontras fuzzy
                equalized_image[y:y+block_height, x:x+block_width] = np.clip(equalized_block * membership, 0, 255)

        return equalized_image
    
    def fuzzy_grayscale(image_path):
        # Memuat gambar
        image = cv2.imread(image_path)

        # Terapkan Fuzzy Histogram Equalization
        fhe_image = MenuImageProc.__fuzzy_grayscale_proc__(image)
        cv2.imwrite(MenuImageProc.outputFile, fhe_image)

        histogram_image = cv2.calcHist([image], [0], None, [256], [0, 256])
        histogram_equalized_image = cv2.calcHist([fhe_image], [0], None, [256], [0, 256])

        # Menampilkan gambar asli dan yang telah di FHE
        plt.figure(figsize=(12, 6))

        plt.subplot(2, 2, 1)
        plt.title('Original Image')
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.axis('off')

        plt.subplot(2, 2, 2)
        plt.title('Fuzzy Histogram Equalization Image')
        plt.imshow(fhe_image, cmap='gray')
        plt.axis('off')

        plt.subplot(2, 2, 3)
        plt.title('Origninal Image Histogram')
        plt.plot(histogram_image)
        plt.xlim([0, 256])

        plt.subplot(2, 2, 4)
        plt.title('Equalization Image Histogram')
        plt.plot(histogram_equalized_image)
        plt.xlim([0, 256])

        plt.show()

        return MenuImageProc.outputFile

    def __apply_fuzzy_he_rgb__(value):
        if value < 128:
            return int(2 * (value ** 2) / 255.0)
        else:
            return int(255 - 2 * ((255 - value) ** 2) / 255.0)

    def fuzzy_he_rgb(input_image_path):
        # Buka gambar input menggunakan PIL
        input_image = Image.open(input_image_path)
        input_image = input_image.convert("RGB")

        # Ambil ukuran gambar
        width, height = input_image.size

        # Buat gambar output
        output_image = Image.new("RGB", (width, height))

        # Proses setiap piksel
        for y in range(height):
            for x in range(width):
                # Ambil nilai R, G, B dari input_image
                r, g, b = input_image.getpixel((x, y))

                # Terapkan fuzzy histogram equalization pada masing-masing channel
                r = MenuImageProc.__apply_fuzzy_he_rgb__(r)
                g = MenuImageProc.__apply_fuzzy_he_rgb__(g)
                b = MenuImageProc.__apply_fuzzy_he_rgb__(b)

                # Set piksel baru ke output_image
                output_image.putpixel((x, y), (r, g, b))

        # Simpan gambar hasil ke file
        output_image.save(MenuImageProc.outputFile)

        image_input_plot = cv2.imread(input_image_path)
        image_output_plot = cv2.imread(MenuImageProc.outputFile)

        histogram_image = cv2.calcHist([image_input_plot], [0], None, [256], [0, 256])
        histogram_equalized_image = cv2.calcHist([image_output_plot], [0], None, [256], [0, 256])

        # Menampilkan gambar asli dan yang telah di FHE
        plt.figure(figsize=(12, 6))

        plt.subplot(2, 2, 1)
        plt.title('Original Image')
        plt.imshow(cv2.cvtColor(image_input_plot, cv2.COLOR_BGR2RGB))
        plt.axis('off')

        plt.subplot(2, 2, 2)
        plt.title('Fuzzy HE RGB Image')
        plt.imshow(cv2.cvtColor(image_output_plot, cv2.COLOR_BGR2RGB))
        plt.axis('off')

        plt.subplot(2, 2, 3)
        plt.title('Origninal Image Histogram')
        plt.plot(histogram_image)
        plt.xlim([0, 256])

        plt.subplot(2, 2, 4)
        plt.title('Fuzzy HE RGB Histogram')
        plt.plot(histogram_equalized_image)
        plt.xlim([0, 256])

        plt.show()

        return MenuImageProc.outputFile
