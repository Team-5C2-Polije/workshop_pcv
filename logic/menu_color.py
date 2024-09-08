from PyQt5 import QtGui, QtWidgets
from PIL import Image
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

class MenuColor:

    outputPath = ".output"
    outputFile = rf"{outputPath}\output.png"

    def __quantize__(image, intervals, interval_size, mid_values):
        quantized_image = np.zeros_like(image)
        for i in range(len(intervals)):
            lower_bound = intervals[i]
            upper_bound = lower_bound + interval_size - 1
            mask = (image >= lower_bound) & (image <= upper_bound)
            quantized_image[mask] = mid_values[i]
        return quantized_image

    def quantize_grayscale_level(image_path, level):
        # Membaca gambar
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Menghitung ukuran interval
        interval_size = 256 // level
        
        # Menghitung interval dan nilai tengah
        intervals = [i * interval_size for i in range(level)]
        mid_values = [((i * interval_size) + ((i + 1) * interval_size - 1)) // 2 for i in range(level)]

        # Terapkan kuantisasi pada gambar
        quantized_image = MenuColor.__quantize__(image, intervals, interval_size, mid_values)

        # Membuat direktori output jika belum ada
        if not os.path.exists(MenuColor.outputPath):
            os.makedirs(MenuColor.outputPath)

        # Tampilkan gambar asli dan hasil kuantisasi
        plt.figure(figsize=(10, 4))

        plt.subplot(1, 2, 1)
        plt.title("Gambar Asli")
        plt.imshow(image, cmap='gray', vmin=0, vmax=255)
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.title("Setelah Kuantisasi")
        plt.imshow(quantized_image, cmap='gray', vmin=0, vmax=255)
        plt.axis('off')

        plt.show()

        # Membuat nama file untuk gambar yang disimpan
        output_path = os.path.join(MenuColor.outputFile)
        cv2.imwrite(output_path, quantized_image)

        return output_path

    def quantize_color_level(image_path, level):
        image = Image.open(image_path)
        image = image.convert('RGB')

        img_array = np.array(image)

        min_val = img_array.min()
        max_val = img_array.max()

        step_size = (max_val - min_val) / level

        quantize_array = (img_array // step_size) * step_size

        quantize_image = Image.fromarray(quantize_array.astype('uint8'))

        new_image_path = os.path.join(MenuColor.outputFile)
        quantize_image.save(new_image_path)
        return new_image_path

    def rgb_to_grayscale_average(input_path):
        img = Image.open(input_path)
        img_np = np.array(img)

        # konversi rgb to grayscale lightness
        result = np.mean(img_np, axis=2).astype(np.uint8)

        output_file = os.path.join(MenuColor.outputFile)
        Image.fromarray(result).save(output_file)
        return output_file

    def rgb_to_grayscale_lightness(input_path):
        img = Image.open(input_path)
        img_np = np.array(img)

        # konversi rgb to grayscale lightness
        max_rgb = np.max(img_np, axis=2)
        min_rgb = np.min(img_np, axis=2)
        result = ((max_rgb + min_rgb) / 2).astype(np.uint8)

        output_file = os.path.join(MenuColor.outputFile)
        Image.fromarray(result).save(output_file)
        return output_file

    def rgb_to_grayscale_luminance(image):
        img = Image.open(image)
        img_np = np.array(img)

        # konversi rgb to grayscale luminance
        result =  (0.2989 * img_np[:,:,0] + 0.5870 * img_np[:,:,1] + 0.1140 * img_np[:,:,2]).astype(np.uint8)

        output_file = os.path.join(MenuColor.outputFile)
        Image.fromarray(result).save(output_file)
        return output_file
    
    def linear_brightness(input_path, brightness_factor):
        img = Image.open(rf"{input_path}")

        # Konversi gambar ke array numpy dengan tipe int16 untuk menghindari overflow
        img_np = np.array(img, dtype=np.int16)

        # Menambahkan brightness_factor
        img_np = img_np + brightness_factor

        # Melakukan clipping pada nilai untuk menjaga nilai pixel antara 0 dan 255
        img_np = np.clip(img_np, 0, 255).astype(np.uint8)

        # Mengonversi kembali array numpy ke gambar
        img_out = Image.fromarray(img_np)

        # Menyimpan gambar yang telah diedit, memastikan output_path adalah direktori
        if not os.path.exists(MenuColor.outputPath):
            os.makedirs(MenuColor.outputPath)

        output_file_path = os.path.join(MenuColor.outputFile)
        img_out.save(output_file_path)
        return output_file_path
    
    def linear_contrast(input_image_path, contrast_factor):
        # Membuka gambar
        img = Image.open(input_image_path)

        # Mengubah gambar ke array numpy
        img_np = np.array(img, dtype=np.float32)

        # Mengalikan semua piksel dengan contrast_factor
        img_np = img_np * contrast_factor

        # Memastikan nilai piksel tetap dalam rentang [0, 255]
        img_np = np.clip(img_np, 0, 255).astype(np.uint8)

        # Mengubah array kembali ke gambar
        img_out = Image.fromarray(img_np)

        # Menentukan file output
        output_file = os.path.join(MenuColor.outputFile)
        img_out.save(output_file)
        return output_file
    
    def linear_saturation(input_image_path, saturation_factor):
        # Membuka gambar
        img = Image.open(input_image_path).convert('RGB')

        # Mengubah gambar ke array numpy dan mengubah ke ruang warna HSV
        img_np = np.array(img)
        img_hsv = Image.fromarray(img_np, 'RGB').convert('HSV')
        img_hsv_np = np.array(img_hsv, dtype=np.float32)

        # Meningkatkan komponen saturasi (S channel)
        img_hsv_np[..., 1] = img_hsv_np[..., 1] * saturation_factor

        # Memastikan nilai piksel tetap dalam rentang [0, 255]
        img_hsv_np[..., 1] = np.clip(img_hsv_np[..., 1], 0, 255)

        # Mengubah array kembali ke gambar RGB
        img_out = Image.fromarray(img_hsv_np.astype(np.uint8), 'HSV').convert('RGB')

        # Menyimpan gambar hasil
        output_file = os.path.join(MenuColor.outputFile)
        img_out.save(output_file)
        return output_file

    def inverse(input_image_path):
        # Membuka gambar
        img = Image.open(input_image_path)

        # Mengubah gambar ke array numpy
        img_np = np.array(img)

        # Melakukan invers pada nilai piksel
        img_np = 255 - img_np

        # Mengubah array kembali ke gambar
        img_out = Image.fromarray(img_np.astype(np.uint8))

        output_file = os.path.join(MenuColor.outputFile)
        img_out.save(output_file)
        return output_file

    def log_brightness(image_path):
        image_asli = cv2.imread(image_path)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        c = 255 / np.log(1 + np.max(image))

        # Terapkan transformasi log brightness
        log_transformed = c * np.log(1 + image)

        # Konversi hasil ke format uint8 (gambar 8-bit)
        log_transformed = np.array(log_transformed, dtype=np.uint8)

        # Simpan gambar hasil log brightness
        cv2.imwrite(MenuColor.outputFile, log_transformed)

        # Tampilkan gambar asli dan gambar setelah log brightness
        plt.figure(figsize=(10, 4))

        plt.subplot(1, 2, 1)
        plt.title("Gambar Asli")
        plt.imshow(cv2.cvtColor(image_asli, cv2.COLOR_BGR2RGB), vmin=0, vmax=255)
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.title("Setelah Log Brightness")
        plt.imshow(log_transformed, cmap='gray', vmin=0, vmax=255)
        plt.axis('off')

        plt.show()

        return MenuColor.outputFile

