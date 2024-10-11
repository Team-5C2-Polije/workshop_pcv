from PIL import Image
import numpy as np
import cv2
import numpy as np
import os


class MenuColorRGB:

    outputPath = ".output"
    outputFile = rf"{outputPath}\output.png"

    def filter_kuning(self, imagefile):
        # Membaca gambar menggunakan PIL
        image = Image.open(imagefile)
        
        # Jika gambar tidak memiliki 3 channel (RGB), konversikan ke RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Mengubah gambar ke numpy array
        image_np = np.array(image)
        
        # Menghapus channel warna biru (nilai B diatur menjadi 0)
        image_np[:, :, 2] = 0  # Channel biru diindeks dengan 2 pada array RGB
        
        # Mengonversi kembali ke format gambar (Image) dari numpy array
        image_out = Image.fromarray(image_np.astype(np.uint8))
        
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        
        # Menyimpan gambar ke output file
        image_out.save(self.outputFile)
        
        # Mengembalikan path dari file yang disimpan
        return self.outputFile

    def filter_orange(self, imagefile):
        # Membaca gambar dari file jika imagefile adalah path
        if isinstance(imagefile, str):
            image = Image.open(imagefile)
        else:
            image = imagefile  # Jika sudah berupa image
        
        # Konversikan gambar menjadi RGB jika tidak dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Mengubah gambar menjadi numpy array
        image_np = np.array(image)

        # Terapkan filter oranye (kurangi komponen biru)
        image_np[:, :, 2] = image_np[:, :, 2] // 2  # Kurangi komponen biru

        # Mengonversi kembali ke format gambar (Image) dari numpy array
        image_out = Image.fromarray(image_np.astype(np.uint8))

        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)

        # Menyimpan gambar ke output file
        image_out.save(self.outputFile)

        # Mengembalikan path dari file yang disimpan
        return self.outputFile
    
    def filter_cyan(self, imagefile):
        # Membaca gambar dari file jika imagefile adalah path
        if isinstance(imagefile, str):
            image = Image.open(imagefile)
        else:
            image = imagefile  # Jika sudah berupa image

        # Konversikan gambar menjadi RGB jika tidak dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Mengubah gambar menjadi numpy array
        image_np = np.array(image)

        # Terapkan filter cyan (hilangkan komponen merah)
        image_np[:, :, 0] = 0  # Hilangkan komponen merah

        # Mengonversi kembali ke format gambar (Image) dari numpy array
        image_out = Image.fromarray(image_np.astype(np.uint8))

        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)

        # Menyimpan gambar ke output file
        image_out.save(self.outputFile)

        # Mengembalikan path dari file yang disimpan
        return self.outputFile

    def ensure_output_path(self):
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)

    def filter_purple(self, imagefile):
        # Jika imagefile adalah path, baca gambar menggunakan PIL
        if isinstance(imagefile, str):
            image = Image.open(imagefile)
        else:
            image = imagefile  # Jika sudah berupa image

        # Konversikan gambar menjadi RGB jika tidak dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Mengubah gambar menjadi numpy array
        image_np = np.array(image)

        # Terapkan filter purple (hilangkan komponen hijau)
        image_np[:, :, 1] = 0  # Hilangkan komponen hijau

        # Mengonversi kembali ke format gambar (Image) dari numpy array
        image_out = Image.fromarray(image_np.astype(np.uint8))

        # Memastikan direktori output ada
        self.ensure_output_path()

        # Menyimpan gambar ke output file
        image_out.save(self.outputFile)

        # Mengembalikan path dari file yang disimpan
        return self.outputFile
    
    def filter_grey(self, imagefile):
        # Jika imagefile adalah path, baca gambar menggunakan PIL
        if isinstance(imagefile, str):
            image = Image.open(imagefile)
        else:
            image = imagefile  # Jika sudah berupa image

        # Konversikan gambar menjadi RGB jika tidak dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Mengubah gambar menjadi numpy array
        image_np = np.array(image)

        # Konversi ke greyscale
        grey_image = np.mean(image_np, axis=2).astype(np.uint8)

        # Mengonversi kembali ke format gambar (Image) dari numpy array
        image_out = Image.fromarray(grey_image)

        # Memastikan direktori output ada
        self.ensure_output_path()

        # Menyimpan gambar ke output file
        image_out.save(self.outputFile)

        # Mengembalikan path dari file yang disimpan
        return self.outputFile

    def filter_coklat(self, imagefile):
        # Jika imagefile adalah path, baca gambar menggunakan PIL
        if isinstance(imagefile, str):
            image = Image.open(imagefile)
        else:
            image = imagefile  # Jika sudah berupa image

        # Konversikan gambar menjadi RGB jika tidak dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Mengubah gambar menjadi numpy array
        image_np = np.array(image)

        # Adjust red, green, and blue components to produce a brownish hue
        brown_filter = image_np.copy()
        brown_filter[:, :, 0] = brown_filter[:, :, 0] // 1.5  # Slightly reduce red
        brown_filter[:, :, 1] = brown_filter[:, :, 1] // 2.5  # Further reduce green
        brown_filter[:, :, 2] = brown_filter[:, :, 2] // 3  # Reduce blue even more

        # Mengonversi kembali ke format gambar (Image) dari numpy array
        image_out = Image.fromarray(brown_filter.astype(np.uint8))

        # Memastikan direktori output ada
        self.ensure_output_path()

        # Menyimpan gambar ke output file
        image_out.save(self.outputFile)

        # Mengembalikan path dari file yang disimpan
        return self.outputFile
    
    def ensure_output_path(self):
        # Memastikan direktori output ada
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)

    def filter_merah(self, imagefile):
        # Jika imagefile adalah path, baca gambar menggunakan PIL
        if isinstance(imagefile, str):
            image = Image.open(imagefile)
        else:
            image = imagefile  # Jika sudah berupa image

        # Konversikan gambar menjadi RGB jika tidak dalam mode RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Mengubah gambar menjadi numpy array
        image_np = np.array(image)

        # Terapkan filter merah (hilangkan komponen hijau dan biru)
        image_np[:, :, 1] = 0  # Hilangkan komponen hijau
        image_np[:, :, 2] = 0  # Hilangkan komponen biru

        # Mengonversi kembali ke format gambar (Image) dari numpy array
        image_out = Image.fromarray(image_np.astype(np.uint8))

        # Memastikan direktori output ada
        self.ensure_output_path()

        # Menyimpan gambar ke output file
        image_out.save(self.outputFile)

        # Mengembalikan path dari file yang disimpan
        return self.outputFile

menu_color = MenuColorRGB()
menu_color.filter_merah(r'C:\Users\Achmad Baihaqi\Pictures\PCV\anggur.jpg')