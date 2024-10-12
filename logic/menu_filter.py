import cv2
import numpy as np
import os

class MenuFilter:
    
    outputPath = ".output"
    outputFile = rf"{outputPath}\output.png"

    def identity_filter(self, imagefile):
        image = cv2.imread(imagefile)
        if image is None:
            raise ValueError(f"Gambar tidak ditemukan atau tidak bisa dibuka: {imagefile}")
        image_np = np.array(image)
        identity_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        result = cv2.filter2D(image_np, -1, identity_kernel)
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        cv2.imwrite(self.outputFile, result)
        return self.outputFile

    def sharpen_filter(self, imagefile):
        # Membaca file gambar menggunakan OpenCV
        image = cv2.imread(imagefile)
        
        if image is None:
            raise ValueError(f"Gambar tidak ditemukan atau tidak bisa dibuka: {imagefile}")
        
        image_np = np.array(image)
        
        # Kernel sharpen
        sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        
        # Menerapkan filter
        result = cv2.filter2D(image_np, -1, sharpen_kernel)
        
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        
        # Menyimpan hasilnya
        sharpened_output_path = os.path.join(self.outputFile)
        cv2.imwrite(sharpened_output_path, result)
        
        return sharpened_output_path


    def unsharp_masking(self, imagefile):
        # Membaca file gambar menggunakan OpenCV
        image = cv2.imread(imagefile)
        
        if image is None:
            raise ValueError(f"Gambar tidak ditemukan atau tidak bisa dibuka: {imagefile}")
        
        image_np = np.array(image)
        
        # Gaussian blur untuk unsharp masking
        blurred = cv2.GaussianBlur(image_np, (9, 9), 10.0)
        
        # Menggunakan addWeighted untuk unsharp masking
        result = cv2.addWeighted(image_np, 1.5, blurred, -0.5, 0)
        
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        
        # Menyimpan hasilnya
        unsharp_output_path = os.path.join(self.outputFile)
        cv2.imwrite(unsharp_output_path, result)
        
        return unsharp_output_path


    def average_filter(self, imagefile):
        # Membaca file gambar menggunakan OpenCV
        image = cv2.imread(imagefile)
        
        if image is None:
            raise ValueError(f"Gambar tidak ditemukan atau tidak bisa dibuka: {imagefile}")
        
        image_np = np.array(image)
        
        # Menggunakan filter rata-rata
        result = cv2.blur(image_np, (3, 3))
        
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        
        # Menyimpan hasilnya
        average_output_path = os.path.join(self.outputFile)
        cv2.imwrite(average_output_path, result)
        
        return average_output_path


    def low_pass_filter(self, imagefile):
        # Membaca file gambar menggunakan OpenCV
        image = cv2.imread(imagefile)
        
        if image is None:
            raise ValueError(f"Gambar tidak ditemukan atau tidak bisa dibuka: {imagefile}")
        
        image_np = np.array(image)
        
        # Menggunakan filter Gaussian untuk low-pass filter
        result = cv2.GaussianBlur(image_np, (5, 5), 0)
        
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        
        # Menyimpan hasilnya
        lowpass_output_path = os.path.join(self.outputFile)
        cv2.imwrite(lowpass_output_path, result)
        
        return lowpass_output_path


    def high_pass_filter(self, imagefile):
        # Membaca file gambar menggunakan OpenCV
        image = cv2.imread(imagefile)
        
        if image is None:
            raise ValueError(f"Gambar tidak ditemukan atau tidak bisa dibuka: {imagefile}")
        
        image_np = np.array(image)
        
        # Filter high-pass (deteksi tepi sederhana)
        kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        result = cv2.filter2D(image_np, -1, kernel)
        
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        
        # Menyimpan hasilnya
        highpass_output_path = os.path.join(self.outputFile)
        cv2.imwrite(highpass_output_path, result)
        
        return highpass_output_path


    def bandstop_filter(self, imagefile):
        # Membaca file gambar menggunakan OpenCV
        image = cv2.imread(imagefile, cv2.IMREAD_GRAYSCALE)
        
        if image is None:
            raise ValueError(f"Gambar tidak ditemukan atau tidak bisa dibuka: {imagefile}")
        
        # Konversi ke domain frekuensi dengan DFT
        dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        
        # Membuat mask bandstop sederhana
        rows, cols = image.shape
        crow, ccol = rows // 2, cols // 2
        mask = np.ones((rows, cols, 2), np.uint8)
        r = 30  # Radius untuk bandstop mask
        mask[crow-r:crow+r, ccol-r:ccol+r] = 0
        
        # Aplikasi mask pada domain frekuensi
        fshift = dft_shift * mask
        f_ishift = np.fft.ifftshift(fshift)
        result = cv2.idft(f_ishift)
        result = cv2.magnitude(result[:, :, 0], result[:, :, 1])
        
        # Normalisasi hasil untuk menghindari nilai terlalu besar
        cv2.normalize(result, result, 0, 255, cv2.NORM_MINMAX)
        result = np.uint8(result)
        
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        
        # Menyimpan hasilnya
        bandstop_output_path = os.path.join(self.outputFile)
        cv2.imwrite(bandstop_output_path, result)
        
        return bandstop_output_path

    def gaussian_blur_3x3(self, imagefile):
        # Membaca file gambar menggunakan OpenCV
        image = cv2.imread(imagefile)
        
        if image is None:
            raise ValueError(f"Gambar tidak ditemukan atau tidak bisa dibuka: {imagefile}")
        
        image_np = np.array(image)
        
        # Gaussian blur dengan kernel 3x3
        result = cv2.GaussianBlur(image_np, (3, 3), 0)
        
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        
        # Menyimpan hasilnya
        gaussian_output_path = os.path.join(self.outputFile)
        cv2.imwrite(gaussian_output_path, result)
        
        return gaussian_output_path

    def gaussian_blur_3x5(self, imagefile):
        # Mengecek apakah imagefile adalah path (string) atau sudah berupa gambar
        if isinstance(imagefile, str):
            # Membaca file gambar dari path
            image = cv2.imread(imagefile)
            if image is None:
                raise ValueError(f"Gambar tidak ditemukan atau tidak bisa dibuka: {imagefile}")
        else:
            # Jika bukan path, asumsikan bahwa imagefile sudah berupa numpy array
            image = np.array(imagefile)
        
        # Gaussian blur dengan kernel 3x5
        result = cv2.GaussianBlur(image, (3, 5), 0)
        
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        
        # Menyimpan hasilnya
        gaussian_output_path = os.path.join(self.outputFile)
        cv2.imwrite(gaussian_output_path, result)
        
        return gaussian_output_path


    

# menu_filter = MenuFilter()
# menu_filter.identity_filter(r'C:\Users\Achmad Baihaqi\Pictures\PCV\anggur.jpg')