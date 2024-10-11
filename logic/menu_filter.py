import cv2
import numpy as np
import os

class MenuFilter:
    
    outputPath = ".output"
    outputFile = rf"{outputPath}\output.png"

    def identity_filter(self, imagefile):
        image = imagefile
        image_np = np.array(image)
        identity_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        result = cv2.filter2D(image_np, -1, identity_kernel)
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        cv2.imwrite(self.outputFile, result)
        return self.outputFile

    def sharpen_filter(self, imagefile):
        image = imagefile
        image_np = np.array(image)
        
        # Kernel sharpening
        sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        result = cv2.filter2D(image_np, -1, sharpen_kernel)
        
        return result

    def unsharp_masking(self, imagefile):
        image = imagefile
        image_np = np.array(image)
        
        # Gaussian blur for unsharp masking
        blurred = cv2.GaussianBlur(image_np, (9, 9), 10.0)
        result = cv2.addWeighted(image_np, 1.5, blurred, -0.5, 0)
        
        return result

    def average_filter(self, imagefile):
        image = imagefile
        image_np = np.array(image)
        
        # Menggunakan filter rata-rata
        result = cv2.blur(image_np, (3, 3))
        
        return result

    def low_pass_filter(self, imagefile):
        image = imagefile
        image_np = np.array(image)
        
        # Menggunakan filter Gaussian untuk low-pass filter
        result = cv2.GaussianBlur(image_np, (5, 5), 0)
        
        return result

    def high_pass_filter(self, imagefile):
        image = imagefile
        image_np = np.array(image)
        
        # Filter high-pass (deteksi tepi sederhana)
        kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        result = cv2.filter2D(image_np, -1, kernel)
        
        return result

    def bandstop_filter(self, imagefile):
        image = imagefile.convert("L")
        image_np = np.array(image)
        
        # Konversi ke frekuensi dengan DFT
        dft = cv2.dft(np.float32(image_np), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        
        # Membuat mask bandstop (sederhana)
        rows, cols = image_np.shape
        crow, ccol = rows // 2, cols // 2
        mask = np.ones((rows, cols, 2), np.uint8)
        r = 30  # Radius mask
        mask[crow-r:crow+r, ccol-r:ccol+r] = 0
        
        # Aplikasi mask pada DFT
        fshift = dft_shift * mask
        f_ishift = np.fft.ifftshift(fshift)
        result = cv2.idft(f_ishift)
        result = cv2.magnitude(result[:, :, 0], result[:, :, 1])
        
        return result

    def gaussian_blur_3x3(self, imagefile):
        image = imagefile
        image_np = np.array(image)
        
        # Gaussian blur dengan kernel 3x3
        result = cv2.GaussianBlur(image_np, (3, 3), 0)
        
        return result

    def gaussian_blur_3x5(self, imagefile):
        image = imagefile
        image_np = np.array(image)
        
        # Gaussian blur dengan kernel 3x5
        result = cv2.GaussianBlur(image_np, (3, 5), 0)
        
        return result